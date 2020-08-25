from nltk.corpus import wordnet

synonyms = []

for syn in wordnet.synsets("make"):
	for lm in syn.lemmas():
		synonyms.append(lm.name())

synonyms = list(set(synonyms))
print ((synonyms))

