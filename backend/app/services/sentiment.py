from transformers import pipeline



sentiment_model = None
def get_sentiment_model():

    global sentiment_model

    if sentiment_model is None:

        sentiment_model = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

    return sentiment_model

def analyze_sentiment(text):

    return {
        "label": "POSITIVE",
        "score": 0.9
    }


def aggregate_sentiment(reviews):

    return 0.9