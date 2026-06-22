import pandas as pd

movies = pd.read_csv(
    "data/raw/tmdb/tmdb_5000_movies.csv"
)

print(movies.columns.tolist())