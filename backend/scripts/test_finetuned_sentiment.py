from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from app.services.sentiment import analyze_sentiment

print(
    analyze_sentiment(
        "This movie was absolutely amazing. Brilliant acting and story."
    )
)

print(
    analyze_sentiment(
        "Terrible movie. Waste of time and money."
    )
)