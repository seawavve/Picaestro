import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import re

def id_comments(song):
    url = "https://www.genie.co.kr/"
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser") ##가져온 html 파일을 html parser를 통해서 정리

    searchForm = driver.find_element_by_xpath('//*[@id="sc-fd"]')
    searchForm.click()
    searchForm.send_keys(song)
    searchForm.send_keys(Keys.RETURN)
    time.sleep(2)
    
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    music_info = driver.find_elements_by_xpath('//*[@id="body-content"]/div[3]/div[2]/div/table/tbody/tr[1]/td[4]/a')[0]
    music_info.click()
    time.sleep(2)
    
    reviews_user = list()
    reviews_list = list()
    i = 1

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    html_review_user = soup.select('div.cmt-wrap > div.reply-text > div > strong > a')
    html_review_user_reply = soup.select('div.cmt-wrap > div.reply > div.reply-text > div > strong > a') # 리댓
    
    for line in html_review_user:
        text = line.get_text()
        text = text.replace("\n", "").strip()
        reviews_user.append(text)
    for line in html_review_user_reply:
        text = line.get_text()
        text = text.replace("\n", "").strip()
        reviews_user.append(text)
    #print(reviews_user)

    html_review_list = soup.select('div.cmt-wrap > div.reply-text > p')
    html_review_reply = soup.select('div.reply > div > div > p')    # 리댓
    #print(html_review_reply)
    for line in html_review_list:
        text = line.get_text()
        text = text.replace("\n", "").strip()
        reviews_list.append(text)
    for line in html_review_reply:
        text = line.get_text()
        text = text.replace("\n", "").strip()
        reviews_list.append(text)    
    #print(reviews_list)
    time.sleep(1.5)
    # 다음 페이지 댓글
    while True:
        try:
            if(song == '꽃송이가'):
                btn_more = driver.find_element_by_xpath('//*[@id="reply_wrap"]/div[2]/a[8]')
                btn_more.click()
                time.sleep(2)
            else:
                btn_more = driver.find_element_by_xpath('//*[@id="reply_wrap"]/div[2]/a[13]')
                btn_more.click()
                time.sleep(2)
                
            i += 1
            print(i)
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            html_review_user = soup.select('div.cmt-wrap > div.reply-text > div > strong > a')
            html_review_user_reply = soup.select('div.cmt-wrap > div.reply > div.reply-text > div > strong > a') # 리댓
            
            for line in html_review_user:
                text = line.get_text()
                text = text.replace("\n", "").strip()
                reviews_user.append(text)
            for line in html_review_user_reply:
                text = line.get_text()
                text = text.replace("\n", "").strip()
                reviews_user.append(text)
            #print(reviews_user)

            html_review_list = soup.select('div.cmt-wrap > div.reply-text > p')
            html_review_reply = soup.select('div.reply > div > div > p')    # 리댓
            
            for line in html_review_list:
                text = line.get_text()
                text = text.replace("\n", "").strip()
                reviews_list.append(text)
            for line in html_review_reply:
                text = line.get_text()
                text = text.replace("\n", "").strip()
                reviews_list.append(text)
            #print(reviews_list)
            time.sleep(1.5)

        except:
            break
   
    multi_page_result = list()
    for user, comments in zip(reviews_user, reviews_list):
        row_data = [user, comments]
        multi_page_result.append(row_data)

    music_reviews = pd.DataFrame(multi_page_result, columns =['user', 'comments'])
    file_name = 'genie_comments_' + song + '.csv' 
    music_reviews.to_csv(file_name, encoding='utf-8')
    time.sleep(2)

song = ['벚꽃엔딩', '나만, 봄', '꽃송이가']
# chrome driver  
driver = webdriver.Chrome('C:\\EUNYEONG\\Picaestro\\chromedriver_win32\\chromedriver.exe')

for i in range(len(song)):
    id_comments(song[i])

driver.close()