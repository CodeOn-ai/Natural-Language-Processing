from nltk import sent_tokenize

# load text
filename = 'text.txt'
file = open(filename, 'rt')
text = file.read()

file.close()

# split into sentences
sentences = sent_tokenize(text)
print(sentences[0])