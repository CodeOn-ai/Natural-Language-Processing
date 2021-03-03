from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


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

# stopwords 
stopWord = stopwords.words('english')
#print(stopWord)

stop_words = set(stopwords.words('english'))

# remove stop words
words = [w for w in tokens if not w in stop_words]

# print the first 100 tokens
print(words[:100])