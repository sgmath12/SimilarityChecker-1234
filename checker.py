class SimilarityChecker:
    def __init__(self, text: str):
        self.string_a, self.string_b = self._split_text(text)

    def get_length_score(self) -> float:
        MAX_SCORE = 60

        left_length = len(self.string_a)
        right_length = len(self.string_b)

        if left_length == right_length:
            return MAX_SCORE

        min_length = min(left_length, right_length)
        if min_length == 0:
            return 0

        length_diff = abs(left_length - right_length)
        return max(0, (min_length - length_diff) * MAX_SCORE / min_length)

    def _split_text(self, text: str) -> tuple[str, str]:
        return text[:text.find(",")].strip(), text[text.find(",") + 1:].strip()
