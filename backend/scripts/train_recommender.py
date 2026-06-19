from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib

tfidf = TfidfVectorizer(
    max_features=5000,
    stop_words='english'
)


BASE_DIR = Path(__file__).resolve().parent.parent

movies = pd.read_csv(
    BASE_DIR / "data/processed/final_movies.csv"
)
vectors = tfidf.fit_transform(
    movies['tags']
)
similarity = cosine_similarity(vectors)
def recommend(movie):
    movie_index = movies[
        movies['title'] == movie
    ].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    for i in movie_list:
        print(
            movies.iloc[i[0]].title
        )
joblib.dump(
    movies,
    BASE_DIR / "data/processed/movies.pkl"
)

joblib.dump(
    similarity,
    BASE_DIR / "data/processed/similarity.pkl"
)

print("Models saved successfully")
print(movies.head())
print(movies.shape)
print(vectors.shape)
print(similarity.shape)
recommend("Avatar")