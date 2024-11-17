import string
import re
import joblib
import nltk
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

# Ensure that NLTK resources are downloaded
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")

# Load the dataset
dataframe = pd.read_csv(r'D:\FinalYear\MediaSentinel\Backend\Models\data-1.csv', usecols=["department", "text"])


# Preprocessing
common_words = set(stopwords.words("english"))
lemmatizer = nltk.WordNetLemmatizer()

def preprocess_text(raw_text: str) -> str:
    raw_text = "".join([character.lower() for character in raw_text if character not in string.punctuation])
    tokenized_text = " ".join([lemmatizer.lemmatize(word) for word in re.split(r'\W+', raw_text) if word not in common_words])
    return tokenized_text

# Clean the 'text' column
dataframe["cleaned_text"] = dataframe["text"].apply(preprocess_text)

# Create the TfidfVectorizer and fit it to the cleaned text
vectorizer = TfidfVectorizer()

# Fit the vectorizer to the cleaned text
X = vectorizer.fit_transform(dataframe["cleaned_text"])

# Save the trained vectorizer
vectorizer_path = r'Backend\Models\Department\TfidfVectorizer.pkl'
joblib.dump(vectorizer, vectorizer_path)
print("Vectorizer saved successfully!")

# Now, train the Support Vector Machine model
y = dataframe["department"]  # Assuming you have the department labels in the 'department' column

# Train an SVM model
trained_model = SVC(kernel="linear")
trained_model.fit(X, y)

# Save the trained model
model_path = r'Backend\Models\Department\SupportVectorMachine.pkl'
joblib.dump(trained_model, model_path)
print("SVM model saved successfully!")
