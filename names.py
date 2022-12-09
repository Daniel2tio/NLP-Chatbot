import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import pairwise_distances
naming = ["call", "myself", "rename", "name", "change", "my", "to", "switch"]

def name_input(input):
    text_tokens = word_tokenize(input)
    user = [username for username in text_tokens 
    if not username.lower() in naming and username.isalpha 
    and not username.lower() in stopwords.words('english')]
    user = (' ').join(user)

    return user

#dataset of possible questions the user may ask to ask name

dataset = './Data/Naming_Dataset.csv'

def name_response(query, threshold):

    df = pd.read_csv(dataset)

    #frequency-inverse frequency of the data

    tfidf_vec = TfidfVectorizer(analyzer='word')
    X_tfidf = tfidf_vec.fit_transform(df['Question']).toarray()
    df_tfidf = pd.DataFrame(X_tfidf, columns = tfidf_vec.get_feature_names_out())

    # query processing 

    input_tfidf = tfidf_vec.transform([query.lower()]).toarray()

    # cosine similarity
    cos = 1 - pairwise_distances(df_tfidf, input_tfidf, metric = 'cosine')

    if cos.max() >= threshold:
        return 'RESPOND'
    else:
        return 'NOT FOUND'