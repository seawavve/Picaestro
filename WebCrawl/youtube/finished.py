import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import re
import operator
import numpy as np
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('C:/Users/user/Downloads/chromedriver_win32/chromedriver')
url="https://www.youtube.com/"
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
driver.maximize_window()

time.sleep(2)
youtubeInput = driver.find_elements_by_xpath('//input[@id="search"]')[0]
print(youtubeInput)
youtubeInput.click()
youtubeInput.send_keys('벚꽃엔딩')
youtubeInput.send_keys(Keys.RETURN)

html0 = driver.page_source
soup = BeautifulSoup(html0, 'html.parser')

time.sleep(2)
youtubeInput=driver.find_element_by_xpath('//div[@class="style-scope ytd-video-renderer"]')
youtubeInput.click()
current=driver.current_url

comment_data = pd.DataFrame({'youtube_id':[],
                            'comment':[],
                            'like_num':[]})
                            

body = driver.find_element_by_tag_name('body')
time.sleep(2)

#자동넘어감방지 동영상 일시정지
youtubeInput=driver.find_element_by_xpath('//video[@*]')
youtubeInput.click()

num_page_down = 3
while num_page_down:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1.5)
    num_page_down -= 1
    
 #인기댓글순
driver.find_element_by_xpath('//paper-button[@class="dropdown-trigger style-scope yt-dropdown-menu"]').click()
time.sleep(1.5)
driver.find_element_by_xpath('//paper-listbox[@class="dropdown-content style-scope yt-dropdown-menu"]/a[1]').click()


#스크롤내리며 댓글 크롤링
num_page_down =10000
while num_page_down:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1.5)
    num_page_down -= 1
    
html_s0 = driver.page_source
html_s = BeautifulSoup(html_s0,'html.parser')
comment0 = html_s.find_all('ytd-comment-renderer',{'class':'style-scope ytd-comment-thread-renderer'})

for i in range(len(comment0)):
    comment = comment0[i].find('yt-formatted-string',{'id':'content-text','class':'style-scope ytd-comment-renderer'}).text
    
    try:
        aa = comment0[i].find('span',{'id':'vote-count-left'}).text
        like_num = "".join(re.findall('[0-9]',aa)) + "개"
    except:
        like_num = 0
        
    bb = comment0[i].find('a',{'id':'author-text'}).find('span').text
    youtube_id = "".join(re.findall('[가-힣0-9a-zA-Z]',bb))
    
    insert_data =  pd.DataFrame({'youtube_id':[youtube_id],
                                               'comment':[comment],
                                               'like_num':[like_num]})
    comment_data = comment_data.append(insert_data)
comment_data.index = range(len(comment_data))

display(comment_data)

comment_data.to_csv("comment_data1.csv", mode='w',encoding='utf-8')
