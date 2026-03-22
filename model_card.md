# Model Card: Mood Machine
This model card is for the Mood Machine project, which includes two versions of a mood classifier:

A rule-based model implemented in mood_analyzer.py
A machine learning model implemented in ml_experiments.py using scikit-learn

Both versions are included in this card to compare performance and limitations.

1. Model Overview
Model type:
I explored both the rule-based model and the ML model, comparing their behavior on the same labeled dataset.

Intended purpose:
The Mood Machine is designed to classify short text posts (like social media updates or messages) into four mood categories: positive, negative, neutral, or mixed. It is intended for educational purposes, personal sentiment exploration, and demonstrating rule-based vs. ML approaches.

How it works (brief):
Rule-based: Each post is tokenized and scored using positive and negative word lists, including emoji handling and slang expressions. Negations like “not happy” are handled, and final labels are assigned based on thresholds of positive/negative scores.
ML-based: Uses a CountVectorizer to convert text into bag-of-words features and trains a small classifier on SAMPLE_POSTS and TRUE_LABELS. The ML model learns patterns automatically, including co-occurrences and subtle indicators of mixed sentiment.

2. Data
Dataset description:
The dataset contains 24 posts in SAMPLE_POSTS with corresponding labels in TRUE_LABELS. Additional posts were added to cover mixed emotions, sarcasm, slang (lowkey, highkey, no cap), and emojis (💀, 😂, 🥲).

Labeling process:
Labels were chosen manually based on the overall sentiment of each post. Posts with both positive and negative cues were labeled mixed. Examples that were hard to label included:
“Feeling tired but kind of hopeful” → mixed
“Lowkey stressed but kind of proud of myself 🥲” → mixed
“I hate that I love this show so much 😅” → mixed

Important characteristics of your dataset:
Contains informal language, slang, and emojis
Includes sarcasm and mixed emotions
Short, ambiguous messages that mimic social media posts

Possible issues with the dataset:
Small size may lead to overfitting in the ML model
Some slang or emoji usage may not be fully covered
Imbalance: more posts with clear positive/negative sentiment than ambiguous/mixed posts

3. How the Rule-Based Model Works

Your scoring rules:
Each positive word increments a score, each negative word decrements it.
Negation handling flips sentiment for words like “not happy” → negative.
Emojis contribute to the sentiment score.
Thresholds determine final label: mostly positive → positive, mostly negative → negative, neither strong → neutral, mix of positive and negative → mixed.

Strengths of this approach:
Transparent and interpretable: easy to see why a post is labeled a certain way
Works well on clear, single-emotion posts
Handles negations and common slang reasonably

Weaknesses of this approach:
Fails on nuanced mixed emotions: e.g., “Lowkey stressed but kind of proud of myself 🥲” → predicted negative
Misses subtle sarcasm or context-specific phrases
Limited by word lists; new slang or emojis are ignored

4. How the ML Model Works

Features used:
Bag-of-words representation using CountVectorizer.

Training data:
Trained on SAMPLE_POSTS and TRUE_LABELS.

Training behavior:
Accuracy improves as more labeled examples are added
Small dataset leads to perfect training accuracy (1.0) but may overfit

Strengths and weaknesses:
Strengths: automatically captures patterns, handles mixed sentiment and sarcasm better than the rule-based approach
Weaknesses: sensitive to the exact labels provided, small dataset limits generalization, may pick up spurious correlations

5. Evaluation

How you evaluated the model:
Both models were evaluated on the labeled posts in dataset.py.

Rule-based accuracy: 0.79
ML model accuracy: 1.0 (likely overfitting)

Examples of correct predictions:

“I love this class so much” → positive (both models correct)
“Today was a terrible day” → negative (both models correct)
“Highkey excited for the concert tonight 😂” → positive (both models correct)

Examples of incorrect predictions:

“Feeling tired but kind of hopeful” → predicted negative by rule-based, mixed by ML
“Lowkey stressed but kind of proud of myself 🥲” → predicted negative by rule-based, mixed by ML
“Chilling with friends, but kinda anxious 🫣” → predicted negative by rule-based, mixed by ML

Rule-based errors mostly involve mixed emotions, sarcasm, and nuanced emoji usage. ML model corrected these but may not generalize to unseen posts.

6. Limitations
Small dataset limits generalization
Rule-based model cannot reliably detect sarcasm, subtle mixed moods, or new slang
ML model overfits small datasets; accuracy on unseen posts may be lower
Emojis or rare expressions not in word lists are ignored by rule-based system
Both models assume English-language, social-media-style text

7. Ethical Considerations
Misclassifying distressing posts may lead to incorrect interpretation of mood
Cultural or dialect differences in language may cause misclassification
Users should not rely on this model for mental health, workplace, or sensitive decision-making contexts
Privacy should be respected when analyzing personal messages

8. Ideas for Improvement
Add more labeled data, especially for mixed and sarcastic posts
Use TF-IDF or word embeddings instead of simple bag-of-words
Enhance preprocessing to better handle emojis and slang
Experiment with small neural networks or transformer-based models
Improve rule-based scoring thresholds and word lists
Add a proper test set instead of evaluating only on training data