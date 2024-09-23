## write the code for scrapping the data
import asyncio
import json
import re
import aiohttp

from bs4 import BeautifulSoup

async def scrape_ndtv_archive(news_source:str,selected_date:str,source_url:str,max_articles_to_scrape:int) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(source_url) as response:
            if response.status == 200 :
                ndtv_soup=BeautifulSoup(await response.text(),"html.parser")
                article_links = ndtv_soup.find("div",id = "main-content")
                
                article_data=[
                    
                    {
                        "id":index,
                        "source":news_source,
                        "publication_date":selected_date,
                        "link": link["href"],
                        "title": link.text.strip(),
                        "text": None,
                        "tone" : None,
                        "government_body": None
                        
                        
                    }
                ]
                
                
                