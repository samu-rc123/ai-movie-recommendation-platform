from pathlib import Path
import pandas as pd
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent.parent

model = joblib.load(
    BASE_DIR / "data/processed/svd_model.pkl"
)
movies = pd.read_csv(
    BASE_DIR / "data/raw/movielens/movies.csv"
)

ratings = pd.read_csv(
    BASE_DIR / "data/raw/movielens/ratings.csv"
)
def recommend_for_user(
    user_id,
    top_n=5
):
    watched_movies = set(
        ratings[
            ratings["userId"] == user_id
        ]["movieId"]
    )

    all_movies = movies["movieId"].tolist()

    recommendations = []

    for movie_id in all_movies:

        if movie_id not in watched_movies:

            predicted_rating = model.predict(
                user_id,
                movie_id
            ).est

            recommendations.append(
                (
                    movie_id,
                    predicted_rating
                )
            )

    recommendations.sort(
        key=lambda x: x[1],
        reverse=True
    )

    top_movies = recommendations[:top_n]

    result = []

    for movie_id, score in top_movies:

        title = movies[
            movies["movieId"] == movie_id
        ]["title"].values[0]

        result.append(
            {
        "title": title,
        "predicted_rating": round(score, 3)
    }
        )

    return result
def predict_rating(user_id, movie_id):
    prediction = model.predict(
        uid=user_id,
        iid=movie_id
    )

    return prediction.est