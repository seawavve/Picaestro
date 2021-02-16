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

def genie_bugs_processing(data):
    data['processed_comment']=None
    for i in range(len(data)):
        text=data.loc[i,'comments']
        text=str(text)
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
sns=['youtube','melon','bugs','genie']
playlist=['벚꽃엔딩','나만,봄','꽃송이가']

for song in playlist:
    for one_sns in sns:
        data=pd.read_csv('./'+one_sns+'_comment_'+song+'.csv',index_col=0)
        if one_sns=='youtube':youtube_processing(data)
        elif one_sns=='melon':melon_processing(data)
        else:genie_bugs_processing(data)
        data.to_csv(one_sns+'_refined_'+song+'.csv', mode='w',encoding='utf-8')
