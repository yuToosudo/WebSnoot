import sys
from nltk.tokenize import RegexpTokenizer
from pdfminer.high_level import extract_text
from nltk.probability import FreqDist
import lxml.etree
import lxml.builder
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

#Make XML
E = lxml.builder.ElementMaker()
ROOT = E.root
DOC = E.doc
FIELD1 = E.field1
FIELD2 = E.field2

the_doc = ROOT(
        DOC(
            FIELD1(tokens, name='tokens'),
            FIELD2(text, name='text')
            )   
        )   
print lxml.etree.tostring(the_doc, pretty_print=True)

#Write XML
f = open("mydoc.xml", "w")
f.write(lxml.etree.tostring(the_doc, pretty_print=True)
f.close()
