from typing import List, Optional
from dataset import POSITIVE_WORDS, NEGATIVE_WORDS, NEUTRAL_WORDS
import re

class MoodAnalyzer:
    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        self.positive_words = set(w.lower() for w in (positive_words or POSITIVE_WORDS))
        self.negative_words = set(w.lower() for w in (negative_words or NEGATIVE_WORDS))
        self.neutral_words = set(w.lower() for w in NEUTRAL_WORDS)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------
    def preprocess(self, text: str) -> List[str]:
        text = text.lower().strip()
        tokens = re.findall(r'\b\w+\b|[^\w\s]', text)
        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------
    def score_text(self, text: str) -> float:
        tokens = self.preprocess(text)
        score = 0.0

        emoji_scores = {
            "💀": -1.0,
            "🥲": -0.5,
            "😅": 0.0,
            "😊": 1.0,
            "😍": 1.0,
            "😬": -0.5,
            "😔": -1.0,
            "💪": 1.0,
            "🔥": 1.0,
            "🙂": 0.5,
            "🫣": -0.5
        }

        # Split by "but" to handle mixed emotions
        if "but" in tokens:
            but_index = tokens.index("but")
            pre_but = tokens[:but_index]
            post_but = tokens[but_index + 1:]

            score_pre = self._score_tokens(pre_but, emoji_scores)
            score_post = self._score_tokens(post_but, emoji_scores)

            # Return separate scores so predict_label can detect mixed
            return score_pre, score_post

        else:
            return self._score_tokens(tokens, emoji_scores)


    def _score_tokens(self, tokens, emoji_scores):
        score = 0.0
        skip_next = False
        for i, token in enumerate(tokens):
            if skip_next:
                skip_next = False
                continue

            # Negation handling
            if token in ["not", "no", "never"] and i + 1 < len(tokens):
                next_word = tokens[i + 1]
                if next_word in self.positive_words:
                    score -= 1
                    skip_next = True
                    continue
                if next_word in self.negative_words:
                    score += 1
                    skip_next = True
                    continue

            # Word scoring
            multiplier = 1.0
            if i > 0 and tokens[i - 1] in ["kinda", "lowkey"]:
                multiplier = 0.5  # reduce weight for hedges

            if token in self.positive_words:
                score += 1 * multiplier
            elif token in self.negative_words:
                score -= 1 * multiplier

            # Emoji scoring
            if token in emoji_scores:
                score += emoji_scores[token]

        return score
        # ---------------------------------------------------------------------
        # Label prediction
        # ---------------------------------------------------------------------
    def predict_label(self, text: str) -> str:
        result = self.score_text(text)
        
        # If score_text returned a tuple (pre_but, post_but)
        if isinstance(result, tuple):
            score_pre, score_post = result
            if score_pre * score_post < 0:  # opposing signs
                return "mixed"
            elif score_pre > 0 or score_post > 0:
                return "positive"
            elif score_pre < 0 or score_post < 0:
                return "negative"
            else:
                return "neutral"

        # Normal case
        score = result
        if score > 0:
            return "positive"
        elif score < 0:
            return "negative"
        else:
            return "neutral"

    # ---------------------------------------------------------------------
    # Explanations (optional)
    # ---------------------------------------------------------------------
    def explain(self, text: str) -> str:
        tokens = self.preprocess(text)
        positive_hits = [t for t in tokens if t in self.positive_words]
        negative_hits = [t for t in tokens if t in self.negative_words]
        score = len(positive_hits) - len(negative_hits)
        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )