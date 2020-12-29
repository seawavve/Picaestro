import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import re
import operator
import numpy as np

driver = webdriver.Chrome('C:/Users/user/Downloads/chromedriver_win32/chromedriver')
url="https://www.youtube.com/"
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
print(soup)
# delay=3
# browser = webdriver.Chrome()
# browser.implicitly_wait(delay)
# start_url  = 'https://www.youtube.com'
# browser.get(start_url)  
# browser.maximize_window()


youtubeInput = driver.find_elements_by_xpath('//input[@id="search"]')[0]
print(youtubeInput)
youtubeInput.click()
youtubeInput.send_keys('벚꽃엔딩')
youtubeInput.send_keys(Keys.RETURN)

html0 = driver.page_source
soup = BeautifulSoup(html0, 'html.parser')


youtubeInput=driver.find_element_by_xpath('//div[@class="style-scope ytd-video-renderer"]')
youtubeInput.click()


import pandas as pd
data=pd.DataFrame({
        'name':[],
            'comment':[]
            })

