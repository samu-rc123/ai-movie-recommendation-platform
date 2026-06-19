from pathlib import Path
import pandas as pd
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent.parent

movies = joblib.load(
    BASE_DIR / "data/processed/movies.pkl"
)

similarity = joblib.load(
    BASE_DIR / "data/processed/similarity.pkl"
)


def recommend(movie_name: str, top_n: int = 5):
    try:
        movie_match = movies[
        movies["title"].str.lower()
        == movie_name.lower()
    ]

        if movie_match.empty:
            return []

        movie_index = movie_match.index[0]
    except IndexError:
        return []

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1: top_n + 1]

    recommendations = []

    for movie in movie_list:
        recommendations.append(
            movies.iloc[movie[0]].title
        )

    return recommendations