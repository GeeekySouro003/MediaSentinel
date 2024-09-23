import asyncio 
import json
from text_crawler import scrape_ndtv_archive
from flask import Flask,request,jsonify
from flask_cors import CORS

app = Flask(__name__)


media_outlets = {
    "Dainik Jagran": ["Hindi", "hin"],
    "Prajavani": ["Kannada", "kan"],
    "Dinamalar": ["Tamil", "tam"],
    "Mathrubhumi": ["Malayalam", "mal"],
    "Eenadu": ["Telugu", "tel"]
}



@app.route("/api", methods = ["POST"])





def process_data() -> str:
    news_source=request.json("news_source")
    selected_date=request.json("selected_date")
    
    if news_source == "NDTV":
        source_url=f"https://archives.ndtv.com/articles/{selected_date}.html"
        max_articles_to_scrape=500
        
        asyncio.run(scrape_ndtv_archive(news_source,selected_date,source_url,max_articles_to_scrape))
        with open() as json_file:
            scraped_data=json.load(json_file)
            
            ##plot_sentiment_graph(scrapped_data)
            return jsonify(scraped_data)
    elif news_source in media_outlets:
        source_language=media_outlets[news_source][0]
        image_file_path='##path of the file from the assests'
        
        
        with open() as json_file:
            language_mappings=json.load(json_file)
        
        extracted_text=perform_ocr(image_file_path,language_mappings[source_language][1])
        ##json_file_path=path from source language store it in frontend
        perform_translation()
        
        
        
        
        
        
        
        
        with open(json_file_path,"r",encoding="utf-8") as json_file:
            scraped_data=json.data(json_file)
            
            
        return jsonify(scraped_data)
    
    
    else:
        return jsonify("Error:News source not found!")

if __name__ == "__main__":
    app.run()