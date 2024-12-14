import json
import os
from googletrans import Translator

from sentiment_analyzer import analyze_sentiment
from department_categorizer import categorize_department

def perform_translation(news_source: str, extracted_text: tuple, json_file_path: str, language: str) -> None:
    google_translator = Translator()
    file_name = extracted_text[1]
    extracted_lines = extracted_text[0].split("\n")
    print(f'\nTranslating: {file_name}')

    # Translate the text line by line
    translated_text = " ".join([  
        google_translator.translate(str(line), src=language, dest="en").text
        for line in extracted_lines
        if line is not None and line.strip() != ""
    ])

    print("Done ...")
    print(f'\nSaving data to file: {json_file_path}')

    # Ensure the directory exists
    directory = os.path.dirname(json_file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)  # Create the directory if it doesn't exist

    # Prepare the article data with translated text and sentiment
    article_data = {
        "id": 1,
        "source": news_source,
        "publication_date": None,
        "link": None,
        "title": None,
        "text": translated_text,
        "tone": analyze_sentiment(translated_text),
        "government-body": categorize_department(translated_text)
    }

    # Write the data to the JSON file
    with open(json_file_path, "w", encoding="utf-8") as json_file:
        json.dump(article_data, json_file, ensure_ascii=False, indent=4)

    print("Done ...")
