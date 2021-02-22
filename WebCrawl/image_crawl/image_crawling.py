from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from urllib.request import urlretrieve
from selenium import webdriver
from tqdm import tqdm
import pandas as pd
import re, os, time, shutil
from PIL import Image


def get_image(keywords):
    url = "https://shutterstock.com/"
    driver.get(url)
    #header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    time.sleep(5)
    
    searchForm = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/form/div/div/div/div[1]/div/div[2]/span/div/div/div[1]/input')
    searchForm.click()
    searchForm.send_keys(keywords)
    searchForm.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.maximize_window()
    #html = driver.page_source

    # 이미지들만 추출
    if driver.find_elements_by_class_name('z_h_9d80b'):
        # 스크롤 어디까지 할건지 설정
        some_tag = driver.find_element_by_class_name('z_b_6e283')
        time.sleep(5)

        action = ActionChains(driver)
        action.move_to_element(some_tag).perform()  # 스크롤
        time.sleep(5)

        imgs = driver.find_elements_by_class_name('z_h_9d80b')
        result = []

        for img in tqdm(imgs):
            result.append(img.get_attribute('src'))
            #print(img.get_attribute('src'))

        # 소스코드가 있는 경로에 각각의 'keywords' 폴더가 없으면 만들어준다.
        #(이미지 저장을 위해서) 
        if not os.path.exists(keywords):  
            os.mkdir(keywords)

        # 이미지 경로를 받아 로컬에 저장한다.
        for index, link in tqdm(enumerate(result)):
            try:
                urlretrieve(link, './{}/{}{}{}'.format(keywords, keywords, index, '.jpg'))
                # 이미지 열어서 자르기(crop)
                img = Image.open('./{}/{}{}{}'.format(keywords, keywords, index, '.jpg'))
                croppedImage = img.crop((0, 0, img.width, img.height-20))
                # 자른 이미지 저장
                croppedImage.save('./{}/{}{}{}'.format(keywords, ('cropped_' + keywords), index, '.jpg'))
                # 원본 삭제
                os.remove('./{}/{}{}{}'.format(keywords, keywords, index, '.jpg'))
            
            except:
                print("can't get img")
                break
    
    time.sleep(5)
            
# ----------------- main ---------------- #
playlist = ['벚꽃엔딩', '나만,봄', '꽃송이가']    

for song in playlist: 
    fp = pd.read_csv('./' + song + '_dtm.csv', encoding='utf-8')
    fp = fp.sort_values(by="total", ascending = False)
    keywords = fp["Unnamed: 0"].head(3)
    keywords = keywords.values.tolist()
    print(keywords)

    # 'song' 폴더가 없으면 만들어준다.
    if not os.path.exists(song):  
        os.mkdir(song)

    # chrome driver  
    driver = webdriver.Chrome('C:\\EUNYEONG\\Picaestro\\Eun0\'s Work\\chromedriver_win32\\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36")

    for i in range(len(keywords)):
        get_image(keywords[i])
        if os.path.exists(keywords[i]): # 경로에 폴더가 있고
            if os.path.exists(song + '/' + keywords[i]): # 'song/keywords' 에 중복된 폴더가 있으면
                shutil.rmtree('./{}/{}'.format(song, keywords[i]))  # 삭제하고
            shutil.move(keywords[i], song)  # 새로 저장
driver.close()
