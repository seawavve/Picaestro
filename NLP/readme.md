# PATCH NOTE
  
  #BERT #DTM #TF-IDF #WordCloud #GoogleTranslationAPI
  
2021.01.02   
+ `CSV_Processing.py` KoNLPy 형태소 분석기로 키워드 추출   
   ㄴ전처리한 데이터는 `매체이름_refined_노래이름.csv`  
+ `keyword_frequency.py` 키워드와 빈도수로 리패키징   
  
    
    KoNLPy를 사용해 형태소별로 슬라이싱했습니다.  
    키워드를 추출하기위해 사용한 형태소로는 명사와 형용사 동사를 사용했습니다.
    okt모듈 이외에도 다른 모듈을 사용해보려합니다.  
      
    
    
2021.02.06  
Keyword추출의 다양한 방법을 시도하고 있습니다.  
-DTM(Document-Term Matrix) 구현  
-TF-IDF(termFrequent - InverseDocumentFrequent) tutorial 구현  
  
 꽃송이가 외 2곡을 이용하여 봄이라는 키워드를 얻기위해 small data로 구현하고 있는 지금은 DTM이 더 유용하겠지만,  
 플레이리스트가 훨씬 다양해진다면 각 도큐먼트의 특징을 잘 파악하는 TF-IDF방법이 더 효과적일거라 예상합니다.  

DTM방식으로 한번 결과값을 뽑은다음 불용어를 파악하여 이를  TF-IDF에 적용시킨다면 좋은 solution이 되겠습니다.  
  
  
  우선 다양한 키워드 추출방식을 시도하고 체화한다는 점에 의의를 두고 있습니다.  
    
      
2021.02.13   
**TF-IDF directory**     
TF-IDF 구현했습니다.  
방탄, 아미, 개념과 같은 키워드들은 음악의 음악성 외적인 키워드로 우리가 원하던 값과는 다른 방향의 키워드가 잡혀  
TF-IDF방법은 맞지 않다고 판단했습니다.  
따라서, DTM에서 stopwords를 잘 설정하는 방법으로 전향합니다.  
  

  
2021.02.14  
**DTM directory**  
DTM 구현했습니다.   
봄, 벚꽃 등 원하던 결과값에 잘 대응함을 확인했습니다.  
  
2021.02.16  
가사에서 텍스트를 추출해 키워드중요도 표를 보완하기로 했습니다.  
melon에서 가사를 크롤링하는 부분까지 구현했습니다.  

 
2021.02.23  
**BERT directory**  
keyword추출결과 중 '그렇다','오다'와 같은 의미없는 키워드가 추출되는 게 썩 맘에 들지 않아 보완하게 됐습니다.  
BERT모델을 사용하면 각 단어를 임베딩하여 단어간의 연관성을 계산하여 반환합니다.  
위 모델을 사용하면 하나의 분위기에 통일된 키워드를 얻을 수 있을거란 희망이 생깁니다.  
keyword extraction tutorial Using distilBERT를 업로드합니다.  

  
  
2021.02.25
BERT에 한글 데이터를 적용시킬 수 없어 translation으로 영어로 바꾼 후 진행하기로 결정했습니다.
Google translation API를 사용합니다.
