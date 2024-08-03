import nltk
from nltk.stem import WordNetLemmatizer, wordnet

# once downloaded no need to run again

# nltk.download('wordnet')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

leammatizer =  WordNetLemmatizer()

sentence = 'Vegetables are types of plants'

# We have to tokenize the sentences

sentence_tokens = nltk.word_tokenize(sentence.lower())

# creating position tags
pos_tags = nltk.pos_tag(sentence_tokens)



for tokens,pos_tag in zip(sentence_tokens,pos_tags):
  if pos_tag[1][0].lower() in ['n','v','a','r']:
    lemma = leammatizer.lemmatize(tokens,pos_tag[1][0].lower())
    print(lemma)
  else:
    print(tokens)
