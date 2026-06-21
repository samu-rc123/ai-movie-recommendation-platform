def generate_explanation(
    movie_name,
    content_score,
    svd_score,
    sentiment_score
):

    reasons = []

    if content_score > 0.15:
        reasons.append(
            f"Strong content similarity to {movie_name}"
        )

    if svd_score > 4:
        reasons.append(
            "Predicted to match your preferences"
        )

    if sentiment_score > 0.8:
        reasons.append(
            "Highly positive audience reviews"
        )
    return reasons