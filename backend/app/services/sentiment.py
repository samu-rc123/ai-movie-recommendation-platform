from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_PATH = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

sentiment_model = None
def get_sentiment_model():

    global sentiment_model

    if sentiment_model is None:

        sentiment_model = pipeline(
            "sentiment-analysis",
            model=MODEL_PATH,
            tokenizer=MODEL_PATH
        )

    return sentiment_model

def analyze_sentiment(text):

    result = get_sentiment_model()(text)[0]

    label = (
        "POSITIVE"
        if result["label"] == "LABEL_1"
        else "NEGATIVE"
    )

    return {
        "label": label,
        "score": round(float(result["score"]), 4)
    }

def aggregate_sentiment(reviews):

    scores = []

    for review in reviews:

        result = analyze_sentiment(review)

        score = result["score"]

        if result["label"] == "NEGATIVE":
            score = 1 - score

        scores.append(score)

    return round(
        sum(scores)/len(scores),
        4
    )