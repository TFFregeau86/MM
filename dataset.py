"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
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
    "nothing is going right", "stuck", "💀", "🥲", "anxious"
]

NEUTRAL_WORDS = [
    "fine", "meh", "okay", "chilling", "not sure", "🤔", "😐"
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
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
    # New posts
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
    "positive",  # I love this class so much
    "negative",  # Today was a terrible day
    "mixed",     # Feeling tired but kind of hopeful
    "neutral",   # This is fine
    "positive",  # So excited for the weekend
    "negative",  # I am not happy about this
    "negative",  # Ugh, stuck in traffic again 😩
    "positive",  # Finally finished my project! 🎉
    "negative",  # Kinda sad that the party got canceled 😔
    "neutral",   # Meh, today was okay, nothing special
    "positive",  # Feeling pumped for my workout 💪
    "negative",  # I can't believe I forgot my homework 😭
    "neutral",   # Just chilling with some music 🎶
    "negative",  # So stressed about the exam tomorrow 😬
    "positive",  # Had a lovely dinner with friends 😊
    "mixed",     # Not sure how I feel about this 🤔
    # New labels
    "mixed",     # Lowkey stressed but kind of proud of myself 🥲
    "positive",  # Highkey excited for the concert tonight 😂
    "negative",  # I absolutely love getting stuck in traffic 💀
    "positive",  # No cap, this is the best movie I've seen this year 😍
    "neutral",   # Feeling meh about everything today 😐
    "mixed",     # I hate that I love this show so much 😅
    "negative",  # Honestly, nothing is going right 💀🥲
    "mixed"      # Chilling with friends, but kinda anxious 🫣
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
