import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from get_urls import Urls

class Texts :
    
    def __init__(self):
        self.title_corpus = ""
        self.content_corpus = ""
    
    def get_texts(self):
        urls = Urls()
        page_urls = urls.get_urls()

        columns = ['title', 'content_text']
        df = pd.DataFrame(columns=columns)

        for page_url in page_urls:
            req = requests.get(page_url)
            html = req.content
            soup = BeautifulSoup(html, 'lxml')
            title = soup.find(name = "div", attrs={"class":"sc-1gwvzpi-1"})
            article = soup.find(name = "article", attrs={"class":"sc-1gwvzpi-18"})
            
            if title is not None:
                row_title = title.get_text(separator=" ").strip()
            else:
                row_title = ""

            if article is not None:
                row_article = article.get_text(separator=" ").strip()
            else:
                row_article = ""
            
            row = [row_title, row_article]
            series = pd.Series(row, index=df.columns)
            df = df.append(series, ignore_index=True)

        def text_cleaning(text):
            hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
            result = hangul.sub('',text)
            return result

        df['title'] = df['title'].apply(lambda x: text_cleaning(x))
        df['content_text'] = df['content_text'].apply(lambda x: text_cleaning(x))

        self.title_corpus = " ".join(df['title'].tolist())
        self.content_corpus = " ".join(df['content_text'].tolist())
