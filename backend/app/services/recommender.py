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


def recommend_with_scores(
    movie_name,
    top_n=20
):

    movie_match = movies[
        movies["title"].str.lower()
        == movie_name.lower()
    ]

    if movie_match.empty:
        return []

    movie_index = movie_match.index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1: top_n + 1]

    recommendations = []

    for movie in movie_list:

        recommendations.append(
            {
                "movie_id":
                    int(movies.iloc[movie[0]].movie_id),

                "title":
                    movies.iloc[movie[0]].title,

                "content_score":
                    float(movie[1])
            }
        )

    return recommendations