import pandas as pd
from Preprocessing import text_tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import pairwise_distances

import numpy as np

#dataset containing general questions

dataset = '/Data/QNA Dataset.csv'

def qna_response(query, threshold):

    df = pd.read_csv(dataset)
    df['processed_Question'] = df['Question'].apply(text_tokenizer, type = 'lemmatisation')

    # TF-IDF
    tfidf_vec = TfidfVectorizer(analyzer='word')
    X_tfidf = tfidf_vec.fit_transform(df['Question']).toarray()
    df_tfidf = pd.DataFrame(X_tfidf, columns = tfidf_vec.get_feature_names_out())

    # Process the question and finds the answer in the dataset
    processed_query = text_tokenizer(query, 'lemmatisation')
    input_tfidf = tfidf_vec.transform([processed_query]).toarray()
    cos = 1 - pairwise_distances(df_tfidf, input_tfidf, metric = 'cosine')

    if cos.max() >= threshold:
        id_argmax = np.where(cos == np.max(cos, axis=0))
        id = np.random.choice(id_argmax[0]) 
        return df['Answer'].loc[id]
    else:
        return 'NOT FOUND'