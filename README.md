# Picaestro
Make your playlist into one piece!  
TEAM 조곤소곤  
#WebCrawling #NLP #이미지처리
  
  <img src="https://github.com/seawavve/Picaestro/blob/main/Methodology.jpg">  
  
  내 플레이리스트에 있는 음악들의 공통점을 찾아 그림으로 그려주는 현대예술적 의의를 갖는 프로젝트입니다. 유명한 음악 사이트 3곳에서 각 음악의 반응을 크롤링해 nlp로 키워드를 수집하여 이를 콜라주형태의 그림으로 표현합니다. ‘감성분석 음악 추천 알고리즘’ 논문을 읽고 음악추천이 사람들의 comment에서 공통적으로 표현하는 언어를 기반으로 추천한다는 점을 차용해 이를 토대로 구축하고 있습니다.    
    
    
### Progress
사용자의 플레이리스트에 접근하여 각 노래의 느낌을 설명할 수 있는 키워드를 수집합니다.(장르, 앨범명, 가사, 노래설명) 키워드를 모아 GPT-2와 같은 NLG Natural Language Generation 기술을 활용하여 느낌을 설명할 수 있는 문장을 만듭니다. 문장을 Imagen, DALLE-2와 같은 Text to Image 멀티모달 기술을 사용해 이미지로 구현합니다.

조한희 @seawavve  
 + 유튜브 댓글 크롤링  
 + NLP 한글 데이터 전처리 
 + keyword추출(DTM,TF-IDF,BERT) 
 + melon 가사 크롤링
   
김문곤 @kim-mun-gon  
 + 멜론 댓글 크롤링  
 + keyword WordCloud 생성  
   
손은영 @enyng309  
 + 벅스,지니 댓글 크롤링

