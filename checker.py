class SimilarityChecker:
    def __init__(self, string_a, string_b):
        self.string_a = string_a
        self.string_b = string_b

    def alphabet_score(self):
        set_a = set(c for c in self.string_a if c.isupper())
        set_b = set(c for c in self.string_b if c.isupper())

        total = set_a | set_b
        if not total:
            return 0

        same = set_a & set_b
        return len(same) / len(total) * 40
