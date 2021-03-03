import nltk
from nltk.tokenize import PunktSentenceTokenizer
text='I am a human being, capable of doing terrible things'
sentences=nltk.sent_tokenize(text)
for sent in sentences:
        print(nltk.pos_tag(nltk.word_tokenize(sent)))
