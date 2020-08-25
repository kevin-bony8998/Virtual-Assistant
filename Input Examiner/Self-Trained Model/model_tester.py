from gensim.models import Word2Vec

model = Word2Vec.load("C:/Users/KEVINBONYTHEKKANATH-/Desktop/Projects/Chatbot/word_similarity")
print(model["war"])
print(model.wv.index2entity[:100])
print(model.wv.similarity('london', 'adele'))