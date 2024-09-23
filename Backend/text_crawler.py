## write the code for scrapping the data
import asyncio
import json
import re
async def scrape_ndtv_archive(news_source:str,selected_date:str,source_url:str,max_articles_to_scrape:int) -> None: