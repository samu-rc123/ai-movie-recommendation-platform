from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(BASE_DIR))

from app.services.sentiment import (
    aggregate_sentiment
)

reviews = [
    "Amazing acting and visuals.",
    "Excellent story and soundtrack.",
    "Weak ending but overall enjoyable."
]

print(
    aggregate_sentiment(reviews)
)