from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(BASE_DIR))

from app.services.hybrid import (
    hybrid_recommend
)

results = hybrid_recommend(
    user_id=1,
    movie_name="Avatar"
)

for movie in results:
    print(movie)