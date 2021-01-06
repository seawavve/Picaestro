import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import re

def id_comments(song):
    url = "https://music.bugs.co.kr/"
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser") ##가져온 html 파일을 html parser를 통해서 정리

    searchForm = driver.find_element_by_xpath('//*[@id="headerSearchInput"]')
    searchForm.click()
    searchForm.send_keys(song)
    searchForm.send_keys(Keys.RETURN)
    time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    music_info = driver.find_elements_by_xpath('//*[@id="DEFAULT0"]/table/tbody/tr[1]/td[3]/a')[0]
    music_info.click()
    time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # 이전 한마디 (더보기)
    while True:
        try:
            btn_more = driver.find_element_by_xpath('//*[@id="comments"]/div/p[4]/a')
            btn_more.click()
            time.sleep(2)
        except:
            break

    time.sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    reviews_user = list()
    reviews_list = list()

    html_review_user = soup.findAll("span", {"class":"user"})
    for line in html_review_user:
        text = line.get_text()
        text = text.replace("\n", "").strip()
        reviews_user.append(text)
    #print(reviews_user)

    html_review_list = soup.findAll("p", {"name":"comment"})
    for line in html_review_list:
        text = line.get_text()
        text = text.replace("\n", "").strip()
        reviews_list.append(text)
    #print(reviews_list)

    multi_page_result = list()
    for user, comments in zip(reviews_user, reviews_list):
        row_data = [user, comments]
        multi_page_result.append(row_data)

    music_reviews = pd.DataFrame(multi_page_result, columns =['user', 'comments'])
    file_name = 'bugs_comments_' + song + '.csv' 
    music_reviews.to_csv(file_name, encoding='utf-8')
    time.sleep(2)

song = ['벚꽃엔딩', '나만, 봄', '꽃송이가']
# chrome driver  
driver = webdriver.Chrome('C:\\EUNYEONG\\Picaestro\\chromedriver_win32\\chromedriver.exe')

for i in range(len(song)):
    id_comments(song[i])
