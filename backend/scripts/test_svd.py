from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from app.services.collaborative import predict_rating

print(
    predict_rating(
        1,
        50
    )
)