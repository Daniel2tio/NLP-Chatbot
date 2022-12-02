# Importing the necessary modules
import numpy as np
import scipy
import sklearn
import nltk
import string

#PreProcessing
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('wordnet')

#Function that takes care of lemmatising the words
def lemmatisation(tokens):
    lemmer = nltk.stem.WordNetLemmatizer()
    newtokens = []
    posmap = {
        'ADJ': 'J',
        'ADV': 'R',
        'NOUN': 'N',
        'VERB': 'V'
    }
    #parts of speech tagging using the universal tagset
    post = nltk.pos_tag(tokens, tagset='universal') #parts of speech tagging using the universal tagset
    for token in post:
        word = token[0]
        tag = token[1]
        if tag in posmap.keys():
            newtokens.append(lemmer.lemmatize(word.posmap[tag]))
        else:
            newtokens.append(lemmer.lemmatize(word))
    return newtokens

"""The following function tokenises the text
and removes stopwords alongside any any capital text"""
def text_tokenizer(text, type):
    text_tokens = word_tokenize(text)
    tokens = [word.lower() for word in text_tokens 
    if word not in stopwords.words('english') and word.isalpha()]

   # tokens = lemmatisation(tokens) type == 'lemmatisation'
   # return ('').join(tokens)



sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
    