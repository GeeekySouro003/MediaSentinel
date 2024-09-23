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
                    
                    for index,link in enumerate(article_links.find_all("a",href = True),start=1) 
                    
                    if (
                        
                        (domain_match := re.search(r'https?://(?:www\.)?([^/]+'),link["href"])
                        and domain_match.group(1) == "ndtv.com" and "india-news" in link["href"]
                    )
                ][:max_articles_to_scrape]
                
                
                tasks= [
                    fetch_article_content()
                    for index,article in enumerate(article_data,start=1)
                ]
                    
                
                await asyncio.gather(*tasks)
                
                with open() as json_file:                 ##pass in parameters the english.json from frontend
                    json.dump(article_data,json_file,ensure_ascii=False,indent=4)
            
            
            else:
                print(f'[Error] Failed to retrieve data from {source_url}\nStatus code: {response.status}')
                
                
                