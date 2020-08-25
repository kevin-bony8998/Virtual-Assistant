import gensim.downloader as api
from gensim.models.word2vec import Word2Vec

import json
info = api.info()
#corpus = api.load('text8')
for model_name, model_data in sorted(info['models'].items()):
	print(
	'%s (%d records): %s' % (
	model_name,
	model_data.get('num_records', -1),
	model_data['description'][:40] + '...',
	)
	)

fake_news_info = api.info('glove-wiki-gigaword-50')
print(json.dumps(fake_news_info, indent=4))

model = api.load("glove-wiki-gigaword-50")
print(model.most_similar("cat"))
model.init_sims(replace=True)
model.save("C:/Users/KEVINBONYTHEKKANATH-/Desktop/Projects/Chatbot/pretrained_word_similarity")

print(model.similarity('kevin', 'bonita'))
print(model.similarity('cat', 'meow'))