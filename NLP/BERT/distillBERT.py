#Colab으로 작성함
#refined_*.csv에서 comment column만 추출 후 번역기 돌려서 doc으로 만들고 한번에 번역시켜버리자
import io
import pandas as pd
from google.colab import drive

drive.mount('/content/drive')
filename = '/content/drive/My Drive/bugs_refined_꽃송이가.csv'
data = pd.read_csv(filename)
data.head()

from google_trans_new import google_translator
from sklearn.feature_extraction.text import CountVectorizer

def google_trans(doc):
  translator = google_translator()  
  translate_text = translator.translate(doc,lang_src='ko', lang_tgt='en')  
  return translate_text

def distill_bert(doc):
  n_gram_range = (1, 1)
  stop_words = "english"

  # 후보 단어 추출
  count = CountVectorizer(ngram_range=n_gram_range, stop_words=stop_words).fit([doc])
  candidates = count.get_feature_names()

  print(candidates)

  #임베딩
  from sentence_transformers import SentenceTransformer

  model = SentenceTransformer('distilbert-base-nli-mean-tokens')
  doc_embedding = model.encode([doc])
  candidate_embeddings = model.encode(candidates)

  #유사한 키워드 추출
  from sklearn.metrics.pairwise import cosine_similarity

  top_n = 10
  distances = cosine_similarity(doc_embedding, candidate_embeddings)
  keywords = [candidates[index] for index in distances.argsort()[0][-top_n:]]
  keywords.reverse() #연관성 높은순

  print(keywords)


playlist=['벚꽃엔딩','나만,봄','꽃송이가']
sns=['youtube','melon','genie','bugs']

for song in playlist:
  total_comment=''
  translated_comment=''

  filename = '/content/drive/My Drive/'+song+'_lyric.txt'
  f = open(filename, 'r')
  #print(f.read())
  total_comment+=str(f.read()*5)
  f.close()
  

  for one_sns in sns:
    filename = '/content/drive/My Drive/'+one_sns+'_refined_'+song+'.csv'
    if filename:print(song,one_sns)
    data = pd.read_csv(filename)
    
    data.columns=data.columns.str.replace('comments','comment')
    data.columns=data.columns.str.replace('댓글','comment')
    #display(data.head())

    
    for i in range(len(data)):
      total_comment+='. '+data.iloc[i][2]
      if len(total_comment)>4500:
        translated_comment+=google_trans(total_comment)
        total_comment=''
  distill_bert(translated_comment)
