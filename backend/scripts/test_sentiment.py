from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(BASE_DIR))

from app.services.sentiment import (
    analyze_sentiment
)

review = """
Terrible acting.
Weak screenplay.
Waste of time.
"""

print(
    analyze_sentiment(review)
)