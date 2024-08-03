import nltk
from nltk.stem import WordNetLemmatizer
# nltk.download('wordnet')

x = 'was'
y = 'is'

lemmatizer = WordNetLemmatizer()

lemma1 = lemmatizer.lemmatize(x,'v')

print(lemma1)


lemma2 = lemmatizer.lemmatize(y,'v')

print(lemma2)