from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer
)
import torch

# =========================
# Load Fine-Tuned Model
# =========================

model_path = "models/sentiment"

model = AutoModelForSequenceClassification.from_pretrained(
    model_path
)

# =========================
# Save Tokenizer (One Time)
# =========================

tokenizer = AutoTokenizer.from_pretrained(
    "distilbert-base-uncased"
)

tokenizer.save_pretrained(model_path)

print("✅ Tokenizer saved successfully!")

# =========================
# Test Sentences
# =========================

test_reviews = [
    "This movie was amazing and I loved every minute.",
    "One of the best films I have ever watched.",
    "The acting was terrible and the story was boring.",
    "I regret wasting my time on this movie.",
    "The movie was okay, not great but not bad either."
]

print("\n===== SENTIMENT PREDICTIONS =====\n")

for review in test_reviews:

    inputs = tokenizer(
        review,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=512
    )

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits

    probabilities = torch.softmax(
        logits,
        dim=1
    )

    prediction = torch.argmax(
        probabilities,
        dim=1
    ).item()

    label = "Positive" if prediction == 1 else "Negative"

    confidence = probabilities[0][prediction].item()

    print(f"Review: {review}")
    print(f"Prediction: {label}")
    print(f"Confidence: {confidence:.4f}")
    print("-" * 60)

print("\n✅ Sentiment model is working correctly!")