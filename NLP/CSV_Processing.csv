from konlpy.tag import Okt
import pandas as pd

def youtube_processing(data):
    data['processed_comment']=None
    for i in range(len(data)):
        text=data.loc[i,'comment']
        text_list=okt.pos(text,norm=True,stem=True)
        keywords=[]
        for j in range(len(text_list)):
            if text_list[j][1]=='Noun' or text_list[j][1]=='Verb' or text_list[j][1]=='Adjective':
                keywords.append(text_list[j][0])
        if keywords:
            data.loc[i,'processed_comment']=keywords
        else:
            data.loc[i,'processed_comment']=None
    
    data.dropna(axis=0,inplace=True)
    data.reset_index(drop=True,inplace=True)
    
def melon_processing(data):
    data['processed_comment']=None
    for i in range(len(data)):
        text=data.loc[i,'댓글']
        text_list=okt.pos(text,norm=True,stem=True)
        keywords=[]
        for j in range(len(text_list)):
            if text_list[j][1]=='Noun' or text_list[j][1]=='Verb' or text_list[j][1]=='Adjective':
                keywords.append(text_list[j][0])
        if keywords:
            data.loc[i,'processed_comment']=keywords
        else:
            data.loc[i,'processed_comment']=None
    
    data.dropna(axis=0,inplace=True)
    data.reset_index(drop=True,inplace=True)
    
    
okt=Okt()
youtube_data1 = pd.read_csv('./youtube_comment_벚꽃엔딩.csv',index_col=0)
youtube_data2 = pd.read_csv('./youtube_comment_나만,봄.csv',index_col=0)
youtube_data3 = pd.read_csv('./youtube_comment_꽃송이가.csv',index_col=0)

melon_data1 = pd.read_csv('./melon_comment_벚꽃엔딩.csv',index_col=0)
melon_data2 = pd.read_csv('./melon_comment_나만봄.csv',index_col=0)
melon_data3 = pd.read_csv('./melon_comment_꽃송이가.csv',index_col=0)

youtube_processing(youtube_data1)
youtube_processing(youtube_data2)
youtube_processing(youtube_data3)
melon_processing(melon_data1)
melon_processing(melon_data2)
melon_processing(melon_data3)


youtube_data1.to_csv('youtube_refined_벚꽃엔딩.csv', mode='w',encoding='utf-8')
youtube_data2.to_csv('youtube_refined_나만,봄.csv', mode='w',encoding='utf-8')
youtube_data3.to_csv('youtube_refined_꽃송이가.csv', mode='w',encoding='utf-8')

melon_data1.to_csv('melon_refined_벚꽃엔딩.csv', mode='w',encoding='utf-8')
melon_data2.to_csv('melon_refined_나만,봄.csv', mode='w',encoding='utf-8')
melon_data1.to_csv('melon_refined_꽃송이가.csv', mode='w',encoding='utf-8')

