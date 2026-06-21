from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from app.services.collaborative import (
    recommend_for_user
)

print(
    recommend_for_user(1)
)