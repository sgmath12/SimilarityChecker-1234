class SimilarityChecker:
    def __init__(self, text: str):
        self.string_a, self.string_b = self._split_text(text)

    def get_alphabet_score(self) -> float:
        MAX_SCORE = 40

        set_a = set(c for c in self.string_a if c.isupper())
        set_b = set(c for c in self.string_b if c.isupper())

        total = set_a | set_b
        if not total:
            return 0

        same = set_a & set_b
        return len(same) / len(total) * MAX_SCORE

    def _split_text(self, text: str) -> tuple[str, str]:
        return text[:text.find(",")].strip(), text[text.find(",") + 1:].strip()
