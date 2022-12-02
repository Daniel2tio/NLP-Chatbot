import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import pairwise_distances
import numpy as np


#dataset of common small talk questions

dataset = './Data/Small Talk.csv'

#function to repond with small talk answers based on user questions

def smalltalk_answers(query, threshold):

    df = pd.read_csv(dataset)

    #TF-IDF
    tfidf_vec = TfidfVectorizer(analyzer='word')
    X_tfidf = tfidf_vec.fit_transform(df['Question']).toarray()
    df_tfidf = pd.DataFrame(X_tfidf, columns = tfidf_vec.get_feature_names.out())

    # process query 
    input_tfidf = tfidf_vec.transform([query.lower()]).toarray()

    # cosine similarity
    cos = 1 - pairwise_distances(df_tfidf, input_tfidf, metric = 'cosine')

    if cos.max() >= threshold:
        id_argmax = np.where(cos == np.max(cos, axis=0))
        id = np.random.choice(id_argmax[0]) 
        return df['Answer'].loc[id]
    else:
        return 'NOT FOUND'
    
if __name__ == "__main__":
    print(smalltalk_answers("What is up", 0.1))