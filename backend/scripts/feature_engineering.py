from pathlib import Path
import pandas as pd
import ast

def convert(text):
    result = []
    for i in ast.literal_eval(text):
        result.append(i['name'])
    return result
def fetch_cast(text):
    result = []
    counter = 0

    for i in ast.literal_eval(text):
        if counter != 3:
            result.append(i['name'])
            counter += 1
        else:
            break

    return result
def fetch_director(text):
    result = []

    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            result.append(i['name'])
            break

    return result
BASE_DIR = Path(__file__).resolve().parent.parent

movies = pd.read_csv(
    BASE_DIR / "data/processed/movies_clean.csv"
)
movies['crew'] = movies['crew'].apply(fetch_director)
movies['cast'] = movies['cast'].apply(fetch_cast)
movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['overview'] = movies['overview'].apply(lambda x: x.split())
movies['genres'] = movies['genres'].apply(
    lambda x: [i.replace(" ", "") for i in x]
)

movies['keywords'] = movies['keywords'].apply(
    lambda x: [i.replace(" ", "") for i in x]
)

movies['cast'] = movies['cast'].apply(
    lambda x: [i.replace(" ", "") for i in x]
)

movies['crew'] = movies['crew'].apply(
    lambda x: [i.replace(" ", "") for i in x]
)
movies['tags'] = (
    movies['overview']
    + movies['genres']
    + movies['keywords']
    + movies['cast']
    + movies['crew']
)
new_df = movies[
    [
        "movie_id",
        "title",
        "tags"
    ].copy()
]
new_df['tags'] = new_df['tags'].apply(
    lambda x: " ".join(x)
)
new_df['tags'] = new_df['tags'].apply(
    lambda x: x.lower()
)

new_df.to_csv(
    BASE_DIR / "data/processed/final_movies.csv",
    index=False
)

print("final_movies.csv saved successfully")
print(movies.head())
print(movies['cast'].iloc[0])
print(movies['crew'].iloc[0])
print(movies['overview'].iloc[0][:10])
print(new_df.head())