#Pet카테고리에 있는 에세이
doc="""
   believe love is steadfast.
  My parents have a great big cat at home named Comet. We think he’s at least part Maine coon—he has great big ears, a very large head, huge feet, and a laid-back, mellow personality—but we have no way of knowing for sure. He came from the local animal shelter. My brother and I didn’t really want him, since he was a kitten and we wanted to adopt an adult cat because we thought the kittens would be more likely to find another home, but my little sister insisted.
  We brought two cats home that day. Harry had the sniffles at the time, and Comet soon caught them. Unfortunately, where Harry quickly perked up after some medicine, Comet nearly died. He shrank to skin and bones; his fur was falling out, each of his ribs was clearly visible, and his eyes swelled almost shut. He was terrible to look at, and I was afraid to touch him. The poor thing desperately needed love and care, but I shied away from him.
  Some years later, now a college student, I went home one afternoon after having had an emotional breakdown. My whole life was upside down; I could not go on without cutting some things out of my life, but the only things I could think to cut were the only things worth doing. I felt hollow, dead, an empty shell of a person. I had failed. I had no idea what pieces were even worth picking up again.
  I found Comet curled up in a pile of laundry that afternoon. He’d been asleep, but he lifted his head and looked at me when I came in. Dully, I reached a hand toward him. He nuzzled it, immediately burst into a deep, loud purr, and gave me a perfectly content cat grin. I moved my hand down to scratch his back and sides, and he stretched luxuriously, lolling and showing off his belly to be rubbed, giving me looks of absolute adoration.
  At that point, it hit me: this cat loved me. The cat I didn’t want, the cat I couldn’t bear to take care of when his life depended on it, loved me. And he always would love me. No matter how I failed, no matter what was going on in my life, no matter what I did, Comet would still nap in clean laundry, would still look up from that nap when I entered the room, would still love to be touched by me.
  I believe love is steadfast. I believe that real love, whether it comes from God, a spouse, or a shelter cat, is offered unswervingly and unconditionally. Love doesn’t consider past transgressions; love doesn’t wait to make sure it will be returned; love isn’t looking for something better and settling for less. We are all of us empty people, searching for meaning after our failures. Love is what enables us to pick up the pieces of our broken lives and go on, renewed, undeservedly but steadfastly.
"""

from sklearn.feature_extraction.text import CountVectorizer

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

top_n = 5
distances = cosine_similarity(doc_embedding, candidate_embeddings)
keywords = [candidates[index] for index in distances.argsort()[0][-top_n:]]
keywords.reverse() #연관성 높은순

print(keywords)
