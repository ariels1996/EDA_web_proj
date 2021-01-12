import requests
from bs4 import BeautifulSoup
import re

# 크롤링할 사이트 주소 정의 
source_url = "https://namu.news/section/news?page="
table_rows = []

# 페이지를 넘겨가면서 a 태그 크롤링 수행, list 만들어주기 
for page in range(5):
    req = requests.get(source_url+str(page+1))
    html = req.content
    soup = BeautifulSoup(html, 'lxml')
    contents_table = soup.find(name="div", attrs={"class":"hkXeBB"})
    table_rows.extend(contents_table.find_all(name="a"))

# a 태그의 href 속성을 리스트로 추출 
page_url_base = "https://namu.news"
page_urls = []
for row in table_rows:
    if len(row) > 0:
        page_url = page_url_base + row.get('href')
        page_urls.append(page_url)

# 중복 url 제거
page_urls = list(set(page_urls))

# 페이지 확인 
for page in page_urls:
    print(page)
