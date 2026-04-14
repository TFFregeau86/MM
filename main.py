"""
Entry point for the Mood Machine rule based mood analyzer.
"""

from typing import List

from mood_analyzer import MoodAnalyzer
from dataset import SAMPLE_POSTS, TRUE_LABELS


def evaluate_rule_based(posts: List[str], labels: List[str]) -> float:
    """
    Evaluate the rule based MoodAnalyzer on a labeled dataset.

    Prints each text with its predicted label and the true label,
    then returns the overall accuracy as a float between 0 and 1.
    """
    analyzer = MoodAnalyzer()
    correct = 0
    total = len(posts)

    print("=== Rule Based Evaluation on SAMPLE_POSTS ===")
    for text, true_label in zip(posts, labels):
        predicted_label = analyzer.predict_label(text)
        is_correct = predicted_label == true_label
        if is_correct:
            correct += 1

        # Optional explainability (Week 8 debugging tool)
        # reason = analyzer.explain(text)
        # print(f'"{text}" -> predicted={predicted_label}, true={true_label} ({reason})')

        print(f'"{text}" -> predicted={predicted_label}, true={true_label}')

    if total == 0:
        print("\nNo labeled examples to evaluate.")
        return 0.0

    accuracy = correct / total
    print(f"\nRule based accuracy on SAMPLE_POSTS: {accuracy:.2f}")
    return accuracy


def run_batch_demo() -> None:
    """
    Run the MoodAnalyzer on the sample posts and print predictions only.
    """
    analyzer = MoodAnalyzer()
    print("\n=== Batch Demo on SAMPLE_POSTS (rule based) ===")
    for text in SAMPLE_POSTS:
        label = analyzer.predict_label(text)
        print(f'"{text}" -> {label}')


def run_interactive_loop() -> None:
    """
    Let the user type their own sentences and see the predicted mood.
    """
    analyzer = MoodAnalyzer()
    print("\n=== Interactive Mood Machine (rule based) ===")
    print("Type a sentence to analyze its mood.")
    print("Type 'quit' or press Enter on an empty line to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input == "" or user_input.lower() == "quit":
            print("Goodbye from the Mood Machine.")
            break

        label = analyzer.predict_label(user_input)
        print(f"Model: {label}")


# ---------------------------------------------------------------------
# FIXED: Failure analysis (NO recursion bug)
# ---------------------------------------------------------------------
def show_failures(posts, labels):
    analyzer = MoodAnalyzer()

    print("\n=== RULE-BASED FAILURE CASES ===")

    failures = []

    for text, true_label in zip(posts, labels):
        pred = analyzer.predict_label(text)

        if pred != true_label:
            failures.append((text, true_label, pred))

            print("\n❌ TEXT:", text)
            print("   expected:", true_label)
            print("   got:", pred)

    print("\n--- Failure Summary ---")
    print("Total failures:", len(failures))
    print("Failure rate:", len(failures) / len(posts) if posts else 0)

    return failures


# ---------------------------------------------------------------------
# Week 8: Failure pattern analysis (RELIABILITY INSIGHT)
# ---------------------------------------------------------------------
def analyze_failure_patterns(failures):
    """
    Week 8: AI reliability debugging insight.
    Shows where rule-based model breaks.
    """

    pattern_counts = {
        "positive→negative": 0,
        "negative→positive": 0,
        "neutral→mixed": 0,
        "mixed→other": 0,
    }

    for text, true, pred in failures:
        key = f"{true}→{pred}"
        if key in pattern_counts:
            pattern_counts[key] += 1

    print("\n=== FAILURE PATTERN ANALYSIS ===")
    for k, v in pattern_counts.items():
        print(f"{k}: {v}")


# ---------------------------------------------------------------------
# MAIN EXECUTION
# ---------------------------------------------------------------------
if __name__ == "__main__":

    evaluate_rule_based(SAMPLE_POSTS, TRUE_LABELS)

    run_batch_demo()

    # Structured debugging output (Week 8 requirement)
    failures = show_failures(SAMPLE_POSTS, TRUE_LABELS)
    analyze_failure_patterns(failures)

    run_interactive_loop()

    print("\nTip: After you explore the rule based model here,")
    print("run `python ml_experiments.py` to try a simple ML based model")
    print("trained on the same SAMPLE_POSTS and TRUE_LABELS.")