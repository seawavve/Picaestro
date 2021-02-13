# TF-IDF  
Term Frequency-Inverse Document Frequency  
  
![](https://github.com/seawavve/Picaestro/blob/main/NLP/TF-IDF/tfidf_bad_result.png)  
각 노래에 대해 단어들의 tf-idf값을 계산하여  
TOP 10개의 키워드를 추출했다.  
  
값은 제대로 뽑아내는데에는 성공했지만,  
사진으로 보는 값과 같이 노래와는 상관없는 키워드가 많이 잡혀있는 걸 볼 수 있다.  
빨간색으로 친 키워드는 심각하게 관련성이 없는 키워드  
파란색으로 친 키워드는 어느정도 관련성이 없는 키워드  
    
방탄, 아미, 개념과 같은 키워드들은 음악의 음악성 외적인 키워드로 우리가 원하던 값과는 다른 방향의 키워드가 잡혀  
TF-IDF방법은 맞지 않다고 판단했다.  
  
전체 프로젝트에서 키워드를 어떻게 구했는지 궁금하다면  
<b>DTM에서 stopwords를 잘 설정하는 방법으로 전향</b>했으므로   
Picaestro/NLP/DTM 파일을 확인하길 바란다.  

