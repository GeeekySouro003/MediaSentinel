import asyncio
import json
import os

from flask import Flask, request, jsonify
from flask_cors import CORS

from text_crawler import scrape_ndtv_archive
from image_crawler import perform_ocr
from google_translator import perform_translation
from graph_generator import plot_sentiment_graph, plot_department_graph

app = Flask(__name__)
CORS(app, resources = {
        r'/api/*': {"origins": ["http://localhost:3000", ]}  # Allow cross-origin requests from localhost:3000
    }
)

# Media outlets and corresponding languages
media_outlets = {
    "Dainik Jagran": ["Hindi", "hin"],
    "Prajavani": ["Kannada", "kan"],
    "Dinamalar": ["Tamil", "tam"],
    "Mathrubhumi": ["Malayalam", "mal"],
    "Eenadu": ["Telugu", "tel"]
}

@app.route("/api", methods=["POST"])
def process_data() -> str:
    # Extract news source and date from the request body
    news_source = request.json.get("news_source")
    selected_date = request.json.get("selected_date")

    if news_source == "NDTV":
        # Scrape articles from NDTV if the news source is NDTV
        source_url = f'https://archives.ndtv.com/articles/{selected_date}.html'
        max_articles_to_scrape = 500

        # Scrape the data using asynchronous function
        asyncio.run(scrape_ndtv_archive(news_source, selected_date, source_url, max_articles_to_scrape))
        
        # Load scraped data from the json file for NDTV
        with open('Frontend/src/english.json', "r", encoding="utf-8") as json_file:
            scraped_data = json.load(json_file)

        # Plot sentiment graph from the scraped data
        plot_sentiment_graph(scraped_data)
        return jsonify(scraped_data)
    elif news_source in media_outlets:
        # Handle other media outlets
        source_language = media_outlets[news_source][0]
        
        # Dynamically generate the image file path using the media outlet language code
        image_file_path = f'../Backend/Assets/{media_outlets[news_source][1]}-1.jpg'

        # Check if the image file exists
        if not os.path.exists(image_file_path):
            return jsonify({"Error": f"Image file not found: {image_file_path}"})

        # Load language mappings
        with open('../Backend/languages_code.json', "r", encoding="utf-8") as json_file:
            language_mappings = json.load(json_file)

        # Perform OCR to extract text from the image
        extracted_text = perform_ocr(image_file_path, language_mappings[source_language][1])

        # Translate the extracted text and save it to a new JSON file
        json_file_path = f'Frontend/src/{source_language.lower()}.json'
        perform_translation(news_source, extracted_text, json_file_path, language_mappings[source_language][0])

        # Check if the translated JSON file exists
        if not os.path.exists(json_file_path):
            return jsonify({"Error": f"Translated JSON file not found: {json_file_path}"})

        # Load the translated JSON file
        with open(json_file_path, "r", encoding="utf-8") as json_file:
            scraped_data = json.load(json_file)

        return jsonify(scraped_data)

    else:
        # If the news source is not supported
        return jsonify({"Error": "News source not supported"})

if __name__ == "__main__":
    app.run()
