from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

text = ['dog eat cat dog', 'cat cat cat meat meat eat dog dog dog', 'dog cat', 'dog']
vect = TfidfVectorizer(ngram_range={2, 3})
vector = vect.fit_transform(text)
print (vector)
print(vect.vocabulary_)


