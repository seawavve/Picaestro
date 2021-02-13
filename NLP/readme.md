# PATCH NOTE
  
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
방탄, 아미, 개념과 같은 키워드들은 음악의 음악성 외적인 키워드로 우리가 원하던 값과는 다른 방향의 키워드가 잡혀  
TF-IDF방법은 맞지 않다고 판단했습니다.  
따라서, DTM에서 stopwords를 잘 설정하는 방법으로 전향합니다.  
  
