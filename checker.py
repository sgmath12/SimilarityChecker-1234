class StringChecker:
    def __init__(self, string_a, string_b):
        self.string_a = string_a
        self.string_b = string_b

    def length_score(self):
        long_len = max(len(self.string_a), len(self.string_b))
        short_len = min(len(self.string_a), len(self.string_b))

        if short_len == 0 or long_len >= 2 * short_len:
            return 0

        gap = long_len - short_len
        return (1 - gap / short_len) * 60
