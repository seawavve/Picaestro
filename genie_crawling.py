import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import re

music_title = list()
genre_list = list()
lyric_list = list()
reviews_list = list()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
url = "https://www.genie.co.kr/detail/songInfo?xgnm=81302362"
print(url)
html = requests.get(url, headers = headers) ##requests 를 이용해서 url의 html 파일을 가져옴
#html.encoding
print(html)
soup = BeautifulSoup(html.text, "html.parser") ##가져온 html 파일을 html parser를 통해서 정리

# soup 사용 (https://m.blog.naver.com/kiddwannabe/221177292446)
html_music_title = soup.find("h2", {"class":"name"}).text
print(html_music_title.strip())
music_title.append(html_music_title.strip())
print(music_title)

html_genre = soup.select('#body-content > div.song-main-infos > div.info-zone > ul > li')[0].findAll("span", {"class":"value"})
html_genre = html_genre[2]
korean = re.compile('[^ \u3131-\u3163\uac00-\ud7a3]+') # 정규식을 사용하여 한글만 가져오기 (https://jokergt.tistory.com/52)
genre_list.append(korean.sub('', str(html_genre)))
print(genre_list)

html_lyric = soup.select('#pLyrics')[0].find("p").text
html_lyric = html_lyric.replace("\n", " ").strip()
html_lyric = html_lyric.replace("\r", "").strip()
lyric_list.append(html_lyric)
print(lyric_list)

"""html_review_list = soup.select('.page-comment')
print(html_review_list)
for line in html_review_list:
    text = line.get_text()
    text = text.replace("\n", "").strip()
    reviews_list.append(text)
"""
multi_page_result = list()
for title, genre, lyric in zip(music_title, genre_list, lyric_list):
    row_data = [title, genre, lyric]
    multi_page_result.append(row_data)

information_music = pd.DataFrame(multi_page_result, columns =['title', 'genre', 'lyric'])

information_music
information_music.to_csv('about_music.csv')