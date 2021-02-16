import json
import requests
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys

melon_comment = []
melon_id = []
headers = {
    'Referer': 'https://www.melon.com/index.htm',
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
}

def melon_search(search_word):

    url = 'http://www.melon.com/search/keyword/index.json'
    params = {
        'jscallback': 'jQuery191035080718916700837_1500265008682',
        'query': search_word
    }

    response = requests.get(url, headers = headers, params = params).text
    json_string = response.replace(params['jscallback']+'(', '').replace(');','')
    result_dict = json.loads(json_string)

    if len(result_dict['SONGCONTENTS']) == 0:
        print('멜론 검색 결과가 없습니다.')
    else:
        print('\n멜론 "{}" 검색 결과(앨범명, 곡명, 곡정보 URL)\n'.format(result_dict['KEYWORD']))
        for song in result_dict['SONGCONTENTS']:
            print('''{ALBUMNAME} : {SONGNAME} : {ARTISTNAME} 
            https://www.melon.com/song/detail.htm?songId={SONGID}\n'''.format(**song))

if __name__ == '__main__':
    line = input('가수의 이름을 입력하세요: ')  # 가수의 모든 노래 검색
    melon_search(line)

number = int(input('원하시는 곡의 SONGID를 입력하세요: '))  # 원하는 노래의 앨범으로 들어가기

broswer = webdriver.Chrome('C:/Users/user/Downloads/chromedriver_win32/chromedriver')
broswer.implicitly_wait(5)
broswer.get('https://www.melon.com/song/detail.htm?songId=' + str(number))


page_url = "https://www.melon.com/song/detail.htm?songId=" + str(number)
result = requests.get(page_url, headers=headers)
broswer.get(page_url)
time.sleep(2)
body = broswer.find_element_by_tag_name('body')
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1.5)
Input = broswer.find_elements_by_xpath('//button[@class="button_more arrow_d"]')[0]
Input.click()

lyric=broswer.find_element_by_class_name("lyric").text
print(lyric)

f = open("lyric.txt", 'w',encoding='utf-8')
f.write(lyric)
f.close()
