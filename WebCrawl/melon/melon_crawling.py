import json
import requests
from selenium import webdriver
import time
import pandas as pd

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

broswer = webdriver.Chrome('C:\Chrome_Driver\chromedriver.exe')
broswer.implicitly_wait(5)
broswer.get('https://www.melon.com/song/detail.htm?songId=' + str(number))

i = input('몇 페이지 크롤링 할까요 : ')  # 원하는 페이지 수 만큼 댓글 읽어오기

for page in range(1, int(i) + 1, 1):
    page_url = "https://www.melon.com/song/detail.htm?songId=" + str(number) + "#cmtpgn=&pageNo=" + str(page) + "&sortType=0&srchType=2&srchWord="
    result = requests.get(page_url, headers=headers)
    broswer.get(page_url)
    time.sleep(1)

    # 댓글과 id 범위
    comments = broswer.find_elements_by_css_selector('div.wrap_cntt.d_cmtpgn_cmt_cont_wrapper > div.cntt')
    ids = broswer.find_elements_by_css_selector('div.wrap_nicnmname.d_cmtpgn_cmt_member_wrapper > div > a > span')

    #  melon_id 출력
    for id in ids:
        melon_id.append(id.text)

    #  melon 댓글 출력
    for comment in comments:
        melon_comment.append(comment.text)

#  pandas를 이용한 csv 파일 저장
data = pd.DataFrame({'melon_id': melon_id,
                     'melon_comment': melon_comment})
data.columns = ['melon_id', '댓글']
data.head()
data.to_csv('comment_벚꽃엔딩.csv', mode='w', encoding='utf-8')
