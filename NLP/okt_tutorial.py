#konlpy패키지의 Okt클래스 tutorial

! pip install konlpy

from konlpy.tag import Okt
okt=Okt()

text=u'나는 오늘 배가 고프지 않아'
print(okt.morphs(text))
print(okt.nouns(text))
print(okt.pos(text))
