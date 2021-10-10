import sys
from nltk.tokenize import RegexpTokenizer
from pdfminer.high_level import extract_text
from nltk.probability import FreqDist
# pdf2xml 
# @Bryspeelm
# Description: TODO:s
# Goal: Convert pdf into an indexable xml 
# Ver 0.0.1

filename = sys.argv[0] 

#Extract the text from PDF
text = extract_text(filename)
print(text)
# Create an instance of tokenizer using NLTK ResexpTokenizer
#
tokenizer = RegexpTokenizer('\w+')
print(tokenizer)
#
# Tokenize the text read from PDF
#
tokens = tokenizer.tokenize(text)
print(tokens)
#
# Find Frequency Distribution
#
freqdist = FreqDist(tokens)
print(freqdist)
#
# Find words whose length is greater than 5 and frequency greater than 20
#
long_frequent_words = [words for words in tokens if len(words) > 5 and freqdist[words] > 20]
print(long_frequent_words)
