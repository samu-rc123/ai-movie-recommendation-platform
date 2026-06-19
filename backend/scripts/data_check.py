from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

movies = pd.read_csv(
    BASE_DIR / "data/raw/movielens/movies.csv"
)

ratings = pd.read_csv(
    BASE_DIR / "data/raw/movielens/ratings.csv"
)

tmdb_movies = pd.read_csv(
    BASE_DIR / "data/raw/tmdb/tmdb_5000_movies.csv"
)

tmdb_credits = pd.read_csv(
    BASE_DIR / "data/raw/tmdb/tmdb_5000_credits.csv"
)

print("Movies:", movies.shape)
print("Ratings:", ratings.shape)
print("TMDB Movies:", tmdb_movies.shape)
print("TMDB Credits:", tmdb_credits.shape)