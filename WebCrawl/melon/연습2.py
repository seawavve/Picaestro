import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def melon_search(search_word):

    url = 'http://www.melon.com/search/keyword/index.json'
    params = {
        'jscallback': 'jQuery191035080718916700837_1500265008682',
        'query': search_word
    }

    headers = {
        'Referer': 'https://www.melon.com/index.htm',
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
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
    line = input('가수의 이름을 입력하세요: ')
    melon_search(line)

number = int(input('원하시는 곡의 SONGID를 입력하세요: '))
broswer = webdriver.Chrome('C:\Chrome_Driver\chromedriver.exe')
broswer.get('https://www.melon.com/song/detail.htm?songId=' + str(number))
html = broswer.page_source

soup = BeautifulSoup(html, 'html.parser')

song_comments = soup.select('div.d_cmtpgn_cmt_cont_wrapper > div.cntt')
print(len(song_comments))
rank = 10
for i in range(rank):
    print(song_comments[i].text)

#d_cmtpgn_cmt_list_wrapper > ul > li.first_child
#d_cmtpgn_cmt_list_wrapper > ul > li.first_child > div > div.wrap_cntt.d_cmtpgn_cmt_cont_wrapper > div.cntt > div
