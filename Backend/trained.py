import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load your dataset (Ensure correct path)
dataframe = pd.read_csv(r'D:\FinalYear\MediaSentinel\Backend\Models\data-1.csv', usecols=["department", "text"])

# Initialize TfidfVectorizer
vectorizer = TfidfVectorizer()

# Fit the vectorizer on your dataset (use the 'text' column for text data)
vectorizer.fit(dataframe["text"])

# Save the fitted vectorizer as a pickle file
joblib.dump(vectorizer, r'D:\FinalYear\MediaSentinel\Backend\Models\Department\TfidfVectorizer.pkl')

print("TfidfVectorizer saved successfully.")
