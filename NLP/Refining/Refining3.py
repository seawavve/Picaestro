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
    
def lyric_processing(data):
    #print(data)
    data_list=okt.pos(data,norm=True,stem=True)
    #print(data_list)
    keywords=[]
    for j in range(len(data_list)):
            if data_list[j][1]=='Noun' or data_list[j][1]=='Verb' or data_list[j][1]=='Adjective':
                keywords.append(data_list[j][0])
    f = open(song+'_refined_lyric.txt','w',encoding='utf-8')
    f.write(str(keywords))
    f.close()


###########MAIN
okt=Okt()
sns=['youtube','melon','bugs','genie']
playlist=['벚꽃엔딩','나만,봄','꽃송이가']

for song in playlist:
    for one_sns in sns:
        
        #댓글 데이터 processing
        data=pd.read_csv('./'+one_sns+'_comment_'+song+'.csv',index_col=0)
        if one_sns=='youtube':youtube_processing(data)
        elif one_sns=='melon':melon_processing(data)
        else:genie_bugs_processing(data)
        data.to_csv(one_sns+'_refined_'+song+'.csv', mode='w',encoding='utf-8')
        
    #가사 데이터 processing
    f = open(song+'_lyric.txt','rt',encoding='utf-8')  # Open file with 'UTF-8' 인코딩
    data = f.read()
    f.close()
    lyric_processing(data)
    
#노래의 수 * (sns의 수 + 가사파일 1개) 의 파일이 만들어지게 됩니다 
