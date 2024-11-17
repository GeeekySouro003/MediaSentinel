# import torch
# from transformers import BertTokenizer, BertForSequenceClassification
# # from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
# trained_model = BertForSequenceClassification.from_pretrained(r'Backend\Models\Sentiment')

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# trained_model.to(device)

# def analyze_sentiment(text: str) -> str:
#     tokenized_text = tokenizer(text, truncation=True, padding=True, return_tensors="pt")

#     encoded_text = {
#         key: val.to(device)
#         for key, val in tokenized_text.items()
#     }

#     with torch.inference_mode():
#         predicted_scores = trained_model(**encoded_text).logits

#     sentiment_index = predicted_scores.argmax(dim=1).item()
#     sentiment_labels = ["Positive", "Neutral", "Negative"]
#     predicted_sentiment = sentiment_labels[sentiment_index]

#     return predicted_sentiment

# # def analyze_sentiment(text: str) -> str:
# #     analyzer = SentimentIntensityAnalyzer()
# #     sentiment = analyzer.polarity_scores(text)
# #
# #     if sentiment["compound"] >= 0.1:
# #         return "Positive"
# #
# #     elif sentiment["compound"] <= -0.1:
# #         return "Negative"
# #
# #     else:
# #         return "Neutral"
import torch
from transformers import BertTokenizer, BertForSequenceClassification
import pandas as pd
from datasets import Dataset
import os

# Load the tokenizer and model for BERT
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
trained_model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=3)

# Move the model to the appropriate device (GPU or CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
trained_model.to(device)

# Dynamically resolve the path to 'data-2.csv' based on the script location
base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
csv_path = 'D:/FinalYear/MediaSentinel/Backend/Models/data-2.csv'  # Absolute path
 # Go up one directory and then to the correct path

# Load the CSV file using pandas
data = pd.read_csv(csv_path)  # Ensure the path is correct

# Optionally, you can convert your pandas DataFrame to a Hugging Face Dataset
dataset = Dataset.from_pandas(data)

# Preprocessing function to tokenize text data
def preprocess_function(examples):
    return tokenizer(examples['text'], padding=True, truncation=True)

# Apply the preprocessing function to your dataset
encoded_dataset = dataset.map(preprocess_function, batched=True)

# Define the sentiment analysis function using BERT
def analyze_sentiment(text: str) -> str:
    tokenized_text = tokenizer(text, truncation=True, padding=True, return_tensors="pt")

    encoded_text = {
        key: val.to(device)
        for key, val in tokenized_text.items()
    }

    with torch.no_grad():  # Avoid gradient calculations during inference
        predicted_scores = trained_model(**encoded_text).logits

    sentiment_index = predicted_scores.argmax(dim=1).item()
    sentiment_labels = ["Positive", "Neutral", "Negative"]
    predicted_sentiment = sentiment_labels[sentiment_index]

    return predicted_sentiment

# Example usage of the sentiment analysis function
sample_text = "I love using BERT for sentiment analysis!"
sentiment = analyze_sentiment(sample_text)
print(f"Sentiment: {sentiment}")
