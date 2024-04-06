import pandas as pd
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies_recommend.csv")
movies.head()
# this part read movies csv file, this database will be used to build the recommendation system.
# ---cleaning movie title with regex


def clean_title(title):
    title = re.sub("[^a-zA-Z0-9 ]", "", title)
    return title
    # used to clean the titles and make them fit a certain pattern


movies["clean_title"] = movies["title"].apply(clean_title)
# this part goes to each column and apply the clean_code function to each title
vectorizer = TfidfVectorizer(ngram_range=(1,2))
tfidf = vectorizer.fit_transform(movies["clean_title"])
# --now for part of the search engine by building term frequency matrix
# when the user type a title the function will scan the database titles for each title the function will see each word
# how many times in the title the user entered.
# --depending on how many the word occurs in the input the function will give the titles a number of
# titles with the highest score will be the output.
# --also there is the inverse document frequency, it is the second principle the recommendations will be filtered by
# all this math can be applied using the Tfidfvectorizer function.


def recommend_movies(title):
    title = clean_title(title)
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidf).flatten()
    indices = np.argpartition(similarity, -5)[-5:]
    results = movies.iloc[indices].iloc[::-1]

    return results
# this function recommend movies based on similarity of the given input from the user


