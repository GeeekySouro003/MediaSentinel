import asyncio 
import json

from flask import Flask,request,jsonify
from flask_cors import CORS

app = Flask(__name__)


@app.route("/api", methods = ["POST"])

def process_data() -> str:
    news_source=request.json("news_source")
    selected_date=request.json("selected_date")
    
    if news_source == "NDTV":
        source_url=f"https://archives.ndtv.com/articles/{selected_date}.html"
        max_articles_to_scrape=500
        
        asyncio.run(scrape_ndtv_archive(news_source,selected_date,source_url,max_articles_to_scrape)

if __name__ == "__main__":
    app.run()