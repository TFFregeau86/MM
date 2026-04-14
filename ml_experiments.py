# ml_experiments.py
"""
Simple ML experiments for the Mood Machine lab.

This file uses a "real" machine learning library (scikit-learn)
to train a tiny text classifier on the same SAMPLE_POSTS and
TRUE_LABELS that you use with the rule based model.
"""

from typing import List, Tuple

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from dataset import SAMPLE_POSTS, TRUE_LABELS


def train_ml_model(
    texts: List[str],
    labels: List[str],
) -> Tuple[CountVectorizer, LogisticRegression]:
    """
    Train a simple text classifier using bag of words features
    and logistic regression.

    Steps:
      1. Convert the texts into numeric vectors using CountVectorizer.
      2. Fit a LogisticRegression model on those vectors and labels.

    Returns:
      (vectorizer, model)
    """
    if len(texts) != len(labels):
        raise ValueError(
            "texts and labels must be the same length. "
            "Check SAMPLE_POSTS and TRUE_LABELS in dataset.py."
        )

    if not texts:
        raise ValueError("No training data provided. Add examples in dataset.py.")

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)

    model = LogisticRegression(max_iter=1000)
    model.fit(X, labels)

    return vectorizer, model


def evaluate_on_dataset(
    texts: List[str],
    labels: List[str],
    vectorizer: CountVectorizer,
    model: LogisticRegression,
) -> float:
    """
    Evaluate the trained model on a labeled dataset.

    Prints each text with its predicted label and the true label,
    then returns the overall accuracy as a float between 0 and 1.
    """
    if len(texts) != len(labels):
        raise ValueError(
            "texts and labels must be the same length. "
            "Check your dataset."
        )

    X = vectorizer.transform(texts)
    preds = model.predict(X)

    print("=== ML Model Evaluation on Dataset ===")
    correct = 0

    for text, true_label, pred_label in zip(texts, labels, preds):
        if pred_label == true_label:
            correct += 1

        print(f'"{text}" -> predicted={pred_label}, true={true_label}')

    accuracy = accuracy_score(labels, preds)
    print(f"\nAccuracy on this dataset: {accuracy:.2f}")
    return accuracy


def predict_single_text(
    text: str,
    vectorizer: CountVectorizer,
    model: LogisticRegression,
) -> str:
    """
    Predict the mood label for a single text string using
    the trained ML model.
    """
    X = vectorizer.transform([text])
    return model.predict(X)[0]


# =========================================================
# 🆕 WEEK 8 ADDITION: confidence-based prediction
# =========================================================
def predict_with_confidence(
    text: str,
    vectorizer: CountVectorizer,
    model: LogisticRegression,
):
    """
    Returns:
      (prediction, confidence)
    """
    X = vectorizer.transform([text])
    probs = model.predict_proba(X)[0]

    idx = probs.argmax()
    return model.classes_[idx], float(probs[idx])


def run_interactive_loop(
    vectorizer: CountVectorizer,
    model: LogisticRegression,
) -> None:
    """
    Let the user type their own sentences and see the ML model's
    predicted mood label.
    """
    print("\n=== Interactive Mood Machine (ML model) ===")
    print("Type a sentence to analyze its mood.")
    print("Type 'quit' or press Enter on an empty line to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input == "" or user_input.lower() == "quit":
            print("Goodbye from the ML Mood Machine.")
            break

        label = predict_single_text(user_input, vectorizer, model)
        print(f"ML model: {label}")


# =========================================================
# 🆕 WEEK 8 ADDITION: ML failure analysis
# =========================================================
def show_ml_failures(texts, labels, vectorizer, model):
    print("\n=== ML FAILURE CASES ===")

    X = vectorizer.transform(texts)
    preds = model.predict(X)

    for text, true_label, pred in zip(texts, labels, preds):
        if pred != true_label:
            print("\n❌ TEXT:", text)
            print("   expected:", true_label)
            print("   got:", pred)


# =========================================================
# 🆕 WEEK 8 ADDITION: model comparison tool
# =========================================================
def compare_models(rule_model, vectorizer, ml_model):
    from mood_analyzer import MoodAnalyzer

    rule = MoodAnalyzer()

    print("\n=== RULE vs ML COMPARISON ===")

    for text, true_label in zip(SAMPLE_POSTS, TRUE_LABELS):

        rule_pred = rule.predict_label(text)
        ml_pred = predict_single_text(text, vectorizer, ml_model)

        print("\nTEXT:", text)
        print("TRUE:", true_label)
        print("RULE:", rule_pred)
        print("ML:  ", ml_pred)


if __name__ == "__main__":
    print("Training ML model on SAMPLE_POSTS and TRUE_LABELS...")
    print("Make sure dataset is complete before running.\n")

    vectorizer, model = train_ml_model(SAMPLE_POSTS, TRUE_LABELS)

    evaluate_on_dataset(SAMPLE_POSTS, TRUE_LABELS, vectorizer, model)

    run_interactive_loop(vectorizer, model)

    print("\nTip: Compare ML vs Rule-based model using main.py")


# =========================================================
# 🧠 WEEK 8 SUMMARY
# =========================================================
"""
ML SYSTEM CAPABILITIES:

✔ Bag-of-words classification (CountVectorizer)
✔ Logistic Regression classifier
✔ Accuracy evaluation
✔ Confidence scoring (probability-based)
✔ Failure inspection tool
✔ Rule vs ML comparison tool

RELIABILITY INSIGHTS:
- ML model handles patterns rule system misses
- Rule model handles emojis + logic better
- Both fail on sarcasm + ambiguity
"""