# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

class Urls :
    def __init__(self):
        self.page_urls = []
    
    def get_urls(self):
        # 크롤링할 사이트 주소 정의 
        source_url = "https://namu.news/section/news?page="
        table_rows = []

        # 페이지를 넘겨가면서 a 태그 크롤링 수행, list 만들어주기 
        for page in range(1):
            req = requests.get(source_url+str(page+1))
            html = req.content
            soup = BeautifulSoup(html, 'lxml')
            contents_table = soup.find(name="div", attrs={"class":"xmbqsi-7"})
            table_rows.extend(contents_table.find_all(name="a"))

        # a 태그의 href 속성을 리스트로 추출 
        page_url_base = "https://namu.news"

        for row in table_rows:
            if len(row) > 0:
                page_url = page_url_base + row.get('href')
                self.page_urls.append(page_url)

        # 중복 url 제거
        self.page_urls = list(set(self.page_urls))

        return self.page_urls
        
