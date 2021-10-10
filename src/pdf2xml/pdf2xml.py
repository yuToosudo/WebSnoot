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