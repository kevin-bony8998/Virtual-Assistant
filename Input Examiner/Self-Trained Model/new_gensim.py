#import gensim
from gensim.models import Word2Vec
import pandas as pd

com = pd.read_csv("C:/Users/KEVINBONYTHEKKANATH-/Desktop/Projects/Chatbot/clean_wiki.csv")
print("Shape of dataset:",com.shape)

sentences = com['Target']
print(type(sentences))
print(sentences[0].split("."))

del com

training_data = []
count = 0

for sentence in sentences:
	lines = sentence.split(".")
	sec_index = 0
	for line in lines:
		#print(line.split(" "))
		print((line.lower()).split(" "))
		training_data.append((line.lower()).split(" "))
		#print("Index value of Wiki csv: ",count," and index value in lines", sec_index)
		sec_index+=1
	count+=1

del sentences

model = Word2Vec(training_data, min_count=1)

#model.train([line.split(" ")],epochs=model.epochs,total_examples=model.corpus_count)
model.save("C:/Users/KEVINBONYTHEKKANATH-/Desktop/Projects/Chatbot/word_similarity")