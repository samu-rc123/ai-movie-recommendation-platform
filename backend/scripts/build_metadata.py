from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

movies = pd.read_csv(
    BASE_DIR / "data/raw/tmdb/tmdb_5000_movies.csv"
)

credits = pd.read_csv(
    BASE_DIR / "data/raw/tmdb/tmdb_5000_credits.csv"
)

# Merge datasets
movies = movies.merge(
    credits,
    on="title"
)

# Keep only required columns
movies = movies[
    [
        "movie_id",
        "title",
        "overview",
        "genres",
        "keywords",
        "cast",
        "crew"
    ]
]

# Remove missing values
movies.dropna(inplace=True)

print(movies.head())
print("\nShape:", movies.shape)
print("\nNull values:")
print(movies.isnull().sum())

# Save cleaned dataset
movies.to_csv(
    BASE_DIR / "data/processed/movies_clean.csv",
    index=False
)

print("\nmovies_clean.csv saved successfully")