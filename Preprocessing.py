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

#BOT Training packages 
import re, collections

nltk.download('wordnet')

#Function that takes care of lemmatising the words
def lemmatisation(tokens):
    lemmer = nltk.stem.WordNetLemmatizer()
    newtokens = []
    posmap = {
        'ADJ': 'a',
        'ADV': 'r',
        'NOUN': 'n',
        'VERB': 'v'
    }
    #parts of speech tagging using the universal tagset
    post = nltk.pos_tag(tokens, tagset='universal') #parts of speech tagging using the universal tagset
    for token in post:
        word = token[0]
        tag = token[1]
        if tag in posmap.keys():
            newtokens.append(lemmer.lemmatize(word, posmap[tag]))
        else:
            newtokens.append(lemmer.lemmatize(word))
    return newtokens

"""The following function tokenises the text
and removes stopwords alongside any any capital text"""
def text_tokenizer(text, type):
    text_tokens = word_tokenize(text)
    tokens = [word.lower() for word in text_tokens 
    if word not in stopwords.words('english') and word.isalpha()]
    tokens = lemmatisation(tokens) if type == 'lemmatisation' else 0
    return (' ').join(tokens)



remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def words(text): return re.findall('[a-z]+', text.lower()) 

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model




VANILLA_WORDS = train(words(open("./Data/text_check.txt", "r").read()))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in VANILLA_WORDS)

def known(words): return set(w for w in words if w in VANILLA_WORDS)
    
def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=VANILLA_WORDS.get)