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
        return re.findall(r'\b\w+\b|[^\w\s]', text)

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------
    def score_text(self, text: str):
        tokens = self.preprocess(text)

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

        contrast_words = ["but", "though", "however", "yet", "still"]

        for w in contrast_words:
            if w in tokens:
                idx = tokens.index(w)
                pre = tokens[:idx]
                post = tokens[idx + 1:]

                return (
                    self._score_tokens(pre, emoji_scores),
                    self._score_tokens(post, emoji_scores)
                )

        return self._score_tokens(tokens, emoji_scores)

    # ---------------------------------------------------------------------
    # Token scoring engine (UPGRADED)
    # ---------------------------------------------------------------------
    def _score_tokens(self, tokens, emoji_scores):
        score = 0.0
        skip_next = False

        intensifiers = ["very", "so", "really", "absolutely", "super"]
        negations = ["not", "no", "never", "n't"]

        for i, token in enumerate(tokens):
            if skip_next:
                skip_next = False
                continue

            # -------------------------
            # Negation handling (STRONGER)
            # -------------------------
            if token in negations and i + 1 < len(tokens):
                next_word = tokens[i + 1]

                if next_word in self.positive_words:
                    score -= 1.5
                    skip_next = True
                    continue

                if next_word in self.negative_words:
                    score += 1.5
                    skip_next = True
                    continue

            # -------------------------
            # Intensifier handling
            # -------------------------
            multiplier = 1.0
            if i > 0 and tokens[i - 1] in intensifiers:
                multiplier = 1.5

            # Hedge handling
            if i > 0 and tokens[i - 1] in ["kinda", "lowkey"]:
                multiplier *= 0.5

            # -------------------------
            # Word scoring
            # -------------------------
            if token in self.positive_words:
                score += 1 * multiplier
            elif token in self.negative_words:
                score -= 1 * multiplier

            # Emoji scoring
            if token in emoji_scores:
                score += emoji_scores[token]

        # -------------------------
        # FIX: single-word fallback (IMPORTANT)
        # -------------------------
        if len(tokens) <= 2:
            if any(t in self.positive_words for t in tokens):
                score += 0.8
            if any(t in self.negative_words for t in tokens):
                score -= 0.8

        return score

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------
    def predict_label(self, text: str) -> str:
        result = self.score_text(text)

        if isinstance(result, tuple):
            pre, post = result

            if pre * post < 0:
                return "mixed"
            if pre > 0 or post > 0:
                return "positive"
            if pre < 0 or post < 0:
                return "negative"
            return "neutral"

        if result > 0:
            return "positive"
        elif result < 0:
            return "negative"
        else:
            return "neutral"

    # ---------------------------------------------------------------------
    # Explainability (simplified)
    # ---------------------------------------------------------------------
    def explain(self, text: str) -> str:
        tokens = self.preprocess(text)

        positive_hits = [t for t in tokens if t in self.positive_words]
        negative_hits = [t for t in tokens if t in self.negative_words]

        return (
            f"Score = {len(positive_hits) - len(negative_hits)} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )