import pandas as pd

# Import csv data
movies_c = pd.read_csv('app/data/movies.csv')
movies_c.head()


ratings_c = pd.read_csv('app/data/ratings.csv')
ratings_c.head()


tags_c = pd.read_csv('app/data/tags.csv')
tags_c.head()

# TODO Preprocessing data (Make a DF with : movieId, title, tags, avg_rating, genres)
