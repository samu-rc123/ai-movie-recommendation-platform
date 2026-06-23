from pathlib import Path
import joblib
from huggingface_hub import hf_hub_download
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

REPO_ID = "Samrc2255/movie-recommendation-models"

movies_path = hf_hub_download(
    repo_id=REPO_ID,
    filename="movies.pkl"
)




movies = joblib.load(
    movies_path
)

tfidf = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

tfidf_matrix = tfidf.fit_transform(
    movies["tags"]
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

    movie_vector = tfidf_matrix[movie_index]

    distances = cosine_similarity(
        movie_vector,
        tfidf_matrix
    ).flatten()

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
                    int(
                        movies.iloc[movie[0]].movie_id
                    ),

                "title":
                    movies.iloc[movie[0]].title,

                "content_score":
                    round(
                        float(movie[1]),
                        4
                    )
            }
        )

    return recommendations