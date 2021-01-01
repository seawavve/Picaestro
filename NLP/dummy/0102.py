#konlpy패키지의 Okt클래스 tutorial

#! pip install konlpy

from konlpy.tag import Okt
okt=Okt()

text=u'한국가사 나와서 흠칫함ㅋㅋㅋㅋㅋㅋ예상도 못했다'
print(okt.morphs(text))
print(okt.nouns(text))
print(okt.pos(text)

text=u'한국가사 나와서 흠칫함ㅋㅋㅋㅋㅋㅋ예상도 못했다 근데 본좌가 말이야 야스오 지리누 예쁜 가사 좋아요 아잉'
text_list=okt.pos(text)
keywords=[]
for i in range(len(text_list)):
    if text_list[i][1]=='Noun' or text_list[i][1]=='Verb' or text_list[i][1]=='Adjective':keywords.append(text_list[i][0])
    print(keywords)
