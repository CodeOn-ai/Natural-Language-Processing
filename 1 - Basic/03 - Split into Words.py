from nltk.tokenize import word_tokenize

# load text
filename = 'text.txt'
file = open(filename, 'rt')
text = file.read()

file.close()

# split into words
tokens = word_tokenize(text)

# print the first 100 tokens
print(tokens[:100])