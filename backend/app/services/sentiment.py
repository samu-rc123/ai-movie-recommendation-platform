from transformers import pipeline

sentiment_model = pipeline(
    "sentiment-analysis",
    model="./models/sentiment",
    tokenizer="./models/sentiment"
)
def analyze_sentiment(text):

    result = sentiment_model(text)[0]

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