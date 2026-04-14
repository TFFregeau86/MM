"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS
  - NEGATIVE_WORDS
  - NEUTRAL_WORDS
  - SAMPLE_POSTS
  - TRUE_LABELS
  - EDGE_CASES (Week 8 reliability testing)
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy", "great", "good", "love", "excited", "awesome", "fun",
    "chill", "relaxed", "amazing", "pumped", "finished", "best",
    "lowkey proud", "highkey excited", "😍", "😊", "🎉", "💪", "😂", "😅"
]

NEGATIVE_WORDS = [
    "sad", "bad", "terrible", "awful", "angry", "upset", "tired",
    "stressed", "hate", "boring", "ugh", "😭", "😩", "😔", "😬",
    "stuck", "💀", "🥲", "anxious",
    "nothing is going right"  # FIX: keep ONLY in negative (remove duplicate ambiguity issue)
]

NEUTRAL_WORDS = [
    "fine", "meh", "okay", "chilling", "not sure", "🤔", "😐"
]

# ---------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------

SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "Ugh, stuck in traffic again 😩",
    "Finally finished my project! 🎉",
    "Kinda sad that the party got canceled 😔",
    "Meh, today was okay, nothing special",
    "Feeling pumped for my workout 💪",
    "I can't believe I forgot my homework 😭",
    "Just chilling with some music 🎶",
    "So stressed about the exam tomorrow 😬",
    "Had a lovely dinner with friends 😊",
    "Not sure how I feel about this 🤔",

    # Week 8 edge cases
    "Lowkey stressed but kind of proud of myself 🥲",
    "Highkey excited for the concert tonight 😂",
    "I absolutely love getting stuck in traffic 💀",
    "No cap, this is the best movie I've seen this year 😍",
    "Feeling meh about everything today 😐",
    "I hate that I love this show so much 😅",
    "Honestly, nothing is going right 💀🥲",
    "Chilling with friends, but kinda anxious 🫣"
]

TRUE_LABELS = [
    "positive",
    "negative",
    "mixed",
    "neutral",
    "positive",
    "negative",
    "negative",
    "positive",
    "negative",
    "neutral",
    "positive",
    "negative",
    "neutral",
    "negative",
    "positive",
    "mixed",

    "mixed",
    "positive",
    "negative",
    "positive",
    "neutral",
    "mixed",
    "negative",
    "mixed"
]

# ---------------------------------------------------------------------
# WEEK 8 EDGE CASE TEST SET (NEW)
# ---------------------------------------------------------------------

EDGE_CASE_POSTS = [
    "I love this but also hate it 💀",
    "not bad not good just existing",
    "this is fine 🙂 but actually I'm dying inside",
    "lowkey happy but also stressed 🥲",
    "I guess it's okay?? maybe??",
]

EDGE_CASE_LABELS = [
    "mixed",
    "neutral",
    "mixed",
    "mixed",
    "neutral",
]

# ---------------------------------------------------------------------
# Dataset Validation (WEEK 8 RELIABILITY SAFETY)
# ---------------------------------------------------------------------

def validate_dataset():
    """
    Ensures dataset integrity for AI evaluation.
    """

    if len(SAMPLE_POSTS) != len(TRUE_LABELS):
        raise ValueError(
            f"Dataset mismatch: {len(SAMPLE_POSTS)} posts vs {len(TRUE_LABELS)} labels"
        )

    allowed_labels = {"positive", "negative", "neutral", "mixed"}

    for label in TRUE_LABELS:
        if label not in allowed_labels:
            raise ValueError(f"Invalid label found: {label}")

    return True


# Auto-run validation safely
validate_dataset()

# ---------------------------------------------------------------------
# Dataset statistics (WEEK 8 DEBUG TOOL)
# ---------------------------------------------------------------------

def dataset_summary():
    """
    Returns dataset distribution for debugging model bias.
    """

    return {
        "total_samples": len(SAMPLE_POSTS),
        "positive": TRUE_LABELS.count("positive"),
        "negative": TRUE_LABELS.count("negative"),
        "neutral": TRUE_LABELS.count("neutral"),
        "mixed": TRUE_LABELS.count("mixed"),
    }