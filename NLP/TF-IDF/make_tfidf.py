import pandas as pd
from math import log # IDF 계산
import ast

#테스트 sns가 적어서(youtube,melon 단 두개) tf-idf값이 음수로 나올 수 있습니다.

def make_data(song,one_sns):
    csv_name=one_sns+'_refined_'+song+'.csv'
    data = pd.read_csv(csv_name,index_col=0)
    #display(data)
    return data



#한 노래,한 sns,한 키워드당 tf-idf값 하나 
#TF-IDF
#t:전처리 후 문자열 리스트중 하나
#d:전처리 전 문자열 리스트
def tf(t, d):
    return d.count(t)

#docs:전체 단어 sns별 리스트
def idf(t,docs):
    N=len(docs)
    df = 0
    for doc in docs:
        df += t in doc
        #print(df)
    return log(N/(df + 1))

def tfidf(t, d, docs):
    return tf(t,d)* idf(t,docs)

def get_tfidf(playlist,sns):
    for song in playlist:
        sns_word_dic={}
        for one_sns in sns:
            unprocessed_words=[] #중복처리전
            comment_series=pd.Series(make_data(song,one_sns)['processed_comment'])
            for i in range(len(comment_series)):
                comment_list=ast.literal_eval(comment_series[i])
                unprocessed_words.extend(comment_list)
            sns_word_dic[one_sns]=unprocessed_words
        #지금 sns_word_dic에는 전처리전 데이터가 sns별로 dictionary화 되어있음
        total_words=[]
        for one_sns in sns:
            total_words.extend(sns_word_dic[one_sns])
        print(song,'댓글 중복처리전 단어 개수:',len(total_words))
        total_words=list(set(total_words))
        print(song,'댓글 중복처리후 단어 개수',len(total_words))
        df=make_df(song,sns,sns_word_dic,total_words)
        df.to_csv(song+'_tfidf.csv', mode='w',encoding='utf-8')

def make_df(song,sns,sns_word_dic,total_words):
    #노래 한 곡, sns 리스트, sns당 복수처리전 단어 dictionary, 모든 sns 복수처리후 단어 리스트 사용
    #tf-idf처리된 DataFrame만들기
    
    df=pd.DataFrame(columns=sns) #각 sns당 dictionary로 만들고 df에 추가. #행은 단어, 열은 sns
    sns_word_list=[]
    for val in sns_word_dic.values():
        sns_word_list.append(val)
    
    #df에 tf-idf값 채우기
    for keyword in total_words:
        line=[]
        for one_sns in sns:
            #line.append(tf(keyword,sns_word_dic[one_sns])) 
            #line.append(idf(keyword,sns_word_list)) 
            line.append(tfidf(keyword,sns_word_dic[one_sns],sns_word_list))        
        df.loc[keyword]=line
    display(df)
    return df
            
playlist=['벚꽃엔딩','나만,봄','꽃송이가']
sns=['youtube','melon']
get_tfidf(playlist,sns)
