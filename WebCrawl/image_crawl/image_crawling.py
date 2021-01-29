from selenium.webdriver import ActionChains
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlretrieve
from tqdm import tqdm
import time
import pandas as pd
import re, os


def get_image(keywords):
    url = "https://shutterstock.com/"
    driver.get(url)
    #header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    time.sleep(2)
    
    searchForm = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/form/div/div/div/div[1]/div/div[2]/span/div/div/div[1]/input')
    searchForm.click()
    searchForm.send_keys(keywords)
    searchForm.send_keys(Keys.RETURN)
    time.sleep(2)
    driver.maximize_window()
    #html = driver.page_source

    # 소스코드가 있는 경로에 각각의 'keywords' 폴더가 없으면 만들어준다.
    #(이미지 저장을 위해서) 
    if not os.path.exists(keywords):  
        os.mkdir(keywords)

    some_tag = driver.find_element_by_class_name('z_b_6e283')
    print(some_tag)

    for i in range (1, 3):
        action = ActionChains(driver)
        action.move_to_element(some_tag).perform()
        #driver.execute_script("window.scrollTo(0, 2000)")
        time.sleep(2)
            
        imgs = driver.find_elements_by_class_name('z_h_9d80b')
        result = []

        for img in tqdm(imgs):
            result.append(img.get_attribute('src'))
            #print(img.get_attribute('src'))

        # 이미지 경로를 받아 로컬에 저장한다.
        for index, link in tqdm(enumerate(result)):
            try:
                urlretrieve(link, './{}/{}{}{}{}'.format(keywords, keywords, (str(i) + '_'), index, '.jpg'))
            #print(index)
            except:
                break
        
        btn_more = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/div[2]/main/div/div[3]/div[2]/div/div/a[2]')
        btn_more.click()
        time.sleep(5)
            
        
fp = pd.read_csv('C:\\EUNYEONG\\Picaestro\\벚꽃엔딩_keywords.csv', encoding='utf-8')
keywords = fp["keyword"].head(10)
keywords = keywords.values.tolist()
print(keywords)
# chrome driver  
driver = webdriver.Chrome('C:\\EUNYEONG\\Picaestro\\chromedriver_win32\\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36")
for i in range(len(keywords)):
    get_image(keywords[i])
driver.close()
