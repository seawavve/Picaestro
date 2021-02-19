# DTM  
Document Term Matrix
  
  
`DTM_nonStopword.py`,`DTM_Stopword.py`에 각 노래별 TOP10개의 키워드가 출력되도록 했습니다.  


  
![](https://github.com/seawavve/Picaestro/blob/main/NLP/DTM/dtm_good_result.png)    
상위 2~3개의 keyword가 원하는대로 잘 출력됩니다.  

2021.02.16 update  
  
  가사또한 크롤링하여 텍스트 전처리하여 keyword csv파일 만드는데 열추가 했습니다.  
  가사는 특별히 3을 곱하는 가중치를 넣었습니다.  
  테스트결과 이전보다 더 키워드가 잘 출력됩니다.  
  ![](https://github.com/seawavve/Picaestro/blob/main/NLP/DTM/%EB%B2%9A%EA%BD%83%EC%97%94%EB%94%A9.png)
  
  
  
2021.02.19 update  
directory를 lric과 non_lyric으로 나눴습니다.   
non_lyric은 가사를 데이터에 추가하지 않은 코드.  
lyric은 추가한 코드입니다.  
lyric directory를 보시길 권장합니다.  
