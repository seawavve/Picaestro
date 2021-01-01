#konlpy패키지의 Okt클래스 tutorial

! pip install konlpy

from konlpy.tag import Okt
okt=Okt()

text=u'한국가사 나와서 흠칫함ㅋㅋㅋㅋㅋㅋ예상도 못했다'
print(okt.morphs(text))
print(okt.nouns(text))
print(okt.pos(text))
