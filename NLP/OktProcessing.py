#konlpy패키지의 Okt클래스 tutorial

#! pip install konlpy

from konlpy.tag import Okt
import pandas as pd
okt=Okt()

data = pd.read_csv('./comment_벚꽃엔딩.csv',index_col=0)
data['processed_comment']=None
#display(data)

def processing(data):
    for i in range(len(data)):
        text=data.loc[i,'comment']
        text_list=okt.pos(text)
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

        
processing(data)
display(data)
