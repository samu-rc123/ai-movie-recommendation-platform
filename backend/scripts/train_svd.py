from pathlib import Path
import pandas as pd
import joblib
from surprise import Dataset
from surprise import Reader
from surprise import SVD
from surprise.model_selection import train_test_split
from surprise.accuracy import rmse

BASE_DIR = Path(__file__).resolve().parent.parent

reader = Reader(
    rating_scale=(0.5, 5.0)
)

ratings = pd.read_csv(
    BASE_DIR / "data/raw/movielens/ratings.csv"
)
data = Dataset.load_from_df(
    ratings[["userId", "movieId", "rating"]],
    reader
)
trainset, testset = train_test_split(
    data,
    test_size=0.2,
    random_state=42
)
model = SVD()

model.fit(trainset)

print("SVD model trained successfully")

predictions = model.test(testset)

rmse(predictions)
rmse_value = rmse(predictions, verbose=False)
print(f"RMSE: {rmse_value: .4f}")

joblib.dump(
    model,
    BASE_DIR / "data/processed/svd_model.pkl"
)

print("SVD model saved")
