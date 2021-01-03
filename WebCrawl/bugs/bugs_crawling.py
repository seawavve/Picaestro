import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import re

reviews_list = list()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
url = "https://music.bugs.co.kr/track/2615580?wl_ref=list_tr_08_search"
print(url)
html = requests.get(url, headers = headers) ##requests 를 이용해서 url의 html 파일을 가져옴
#html.encoding
print(html)
soup = BeautifulSoup(html.text, "html.parser") ##가져온 html 파일을 html parser를 통해서 정리

# soup 사용 (https://m.blog.naver.com/kiddwannabe/221177292446)
html_review_list = soup.findAll("ul", {"class": "listComments"})
print(html_review_list)
