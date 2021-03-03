from nltk.tokenize import word_tokenize
import string


# load text
filename = 'text.txt'
file = open(filename, 'rt')
text = file.read()

file.close()

#lowerCase the words
lowerCase = text.lower()

# remove punctuation
cleanedText = lowerCase.translate(str.maketrans('','',string.punctuation))

# split into words
tokens = word_tokenize(cleanedText)

# print the first 100 tokens
print(tokens[:100])