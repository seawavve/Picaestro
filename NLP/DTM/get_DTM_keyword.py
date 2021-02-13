import pandas as pd
from collections import defaultdict
from collections import Counter
import ast

playlist=['벚꽃엔딩','나만,봄','꽃송이가']
sns=['youtube','melon']

#한 노래, 한 sns의 데이터를 가져와 Counter형태로 Packing
def keywords_packing(song,s):
    keyword_df= pd.DataFrame({"keyword":[], "count":[]})
    csv_name=s+'_refined_'+song+'.csv'
    data = pd.read_csv(csv_name,index_col=0)
    data=data['processed_comment'].tolist()
    #print(data)
    for k in range(len(data)):
        data[k]=ast.literal_eval(data[k])
    #print(data)
    for j in range(len(data)):
        line=data[j]
        line_dic={x:line.count(x) for x in line}
        line_dic=Counter(line_dic)
        if j==0:
            total=line_dic
            continue
        total+=line_dic
    return total

#Packing된 Counter 파일들을 하나의 df로 합치기
def make_keyword_list(song,sns):
    for i in range(len(sns)):
        if i==0: counter_data=keywords_packing(song,sns[i])
        else: counter_data+=keywords_packing(song,sns[i])
    dict_data=dict(counter_data)
    #print(dict_data)
    return pd.DataFrame(list(dict_data.items()),columns=['keyword', 'count'])
        

#*******MAIN*******
for i in range(len(playlist)):
    df=make_keyword_list(playlist[i],sns)
    df=df.sort_values(by=['count'], axis=0, ascending=False)
    df.reset_index(drop=True,inplace=True)
    #display(df)
    #print(df["count"].sum())
    df.to_csv(playlist[i]+'_keywords.csv', mode='w',encoding='utf-8')
