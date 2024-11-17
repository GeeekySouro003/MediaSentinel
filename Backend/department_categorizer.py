# import string
# import re

# import joblib
# import nltk
# import pandas as pd
# from nltk.corpus import stopwords
# from sklearn.feature_extraction.text import TfidfVectorizer

# trained_model = joblib.load(r'Backend\Models\Department\SupportVectorMachine.pkl')

# pd.set_option("max_colwidth", 500)
# dataframe = pd.read_csv(r'Backend\Models\data-1.csv', usecols = ["department", "text"])

# common_words = set(stopwords.words("english"))
# lemmatizer = nltk.WordNetLemmatizer()
# vectorizer = TfidfVectorizer()

# def categorize_department(text: str) -> str:
#     cleaned_text = preprocess_text(text)
#     processed_text = vectorizer.transform([cleaned_text])
#     predicted_department = trained_model.predict(processed_text)[0]

#     return predicted_department


# def preprocess_text(raw_text: str) -> str:
#     raw_text = "".join([
#         character.lower()
#         for character in raw_text
#         if character not in string.punctuation
#     ])

#     tokenized_text = " ".join([
#         lemmatizer.lemmatize(word)
#         for word in re.split(r'\W+', raw_text)
#         if word not in common_words
#     ])

#     return tokenized_text

# dataframe["cleaned_text"] = dataframe["text"].apply(preprocess_text)
# sparse_matrix = vectorizer.fit_transform(dataframe["cleaned_text"])

import os
import string
import re
import joblib
import nltk
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# Ensure that NLTK resources are downloaded
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")

# Define relative paths for the model and vectorizer
model_path = r'Backend\Models\Department\SupportVectorMachine.pkl'
vectorizer_path = r'Backend\Models\Department\TfidfVectorizer.pkl'

# Print absolute paths for debugging
print("Absolute path to SupportVectorMachine.pkl:", os.path.abspath(model_path))
print("Absolute path to TfidfVectorizer.pkl:", os.path.abspath(vectorizer_path))

# Load the trained SVM model
trained_model = joblib.load(model_path)

# Load the vectorizer (if it exists)
try:
    vectorizer = joblib.load(vectorizer_path)
    print("Vectorizer loaded successfully!")
except FileNotFoundError as e:
    print(f"Error loading vectorizer: {e}")
    # Handle the error: retrain the vectorizer or raise an exception
    # For now, we will proceed with the error handling

# Set pandas option for better column display
pd.set_option("max_colwidth", 500)

# Load dataset
dataframe = pd.read_csv(r'Backend\Models\data-1.csv', usecols=["department", "text"])

# Set of common stopwords
common_words = set(stopwords.words("english"))
lemmatizer = nltk.WordNetLemmatizer()

# Text preprocessing function
def categorize_department(text: str) -> str:
    """
    Given text, preprocess it and predict the department.
    """
    cleaned_text = preprocess_text(text)
    # Transform the cleaned text into the vectorized form
    processed_text = vectorizer.transform([cleaned_text])
    # Predict the department using the trained model
    predicted_department = trained_model.predict(processed_text)[0]
    return predicted_department

def preprocess_text(raw_text: str) -> str:
    """
    Preprocess the input text: lowercasing, removing punctuation, tokenizing, and lemmatizing.
    """
    # Remove punctuation and convert to lowercase
    raw_text = "".join([character.lower() for character in raw_text if character not in string.punctuation])

    # Tokenize, remove stopwords, and lemmatize
    tokenized_text = " ".join([
        lemmatizer.lemmatize(word) for word in re.split(r'\W+', raw_text) if word not in common_words
    ])

    return tokenized_text

# Clean the text column and apply preprocessing
dataframe["cleaned_text"] = dataframe["text"].apply(preprocess_text)

# Use the vectorizer to transform the cleaned text
sparse_matrix = vectorizer.transform(dataframe["cleaned_text"])

# Optionally save the fitted vectorizer for later use (this step is optional if you're not retraining it)
joblib.dump(vectorizer, vectorizer_path)

# If you want to perform predictions:
sample_text = "Sample text to classify"
predicted_dep = categorize_department(sample_text) 
print(f"Predicted Department: {predicted_dep}")
