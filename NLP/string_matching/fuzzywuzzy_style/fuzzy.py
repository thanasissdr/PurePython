import itertools
import Levenshtein as lev


class Fuzzy:
    """
    Implement fuzzywuzzy functions in a similar fashion.
    """

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
        self.p1 = self.s1.split()  # tokenize s1
        self.p2 = self.s2.split()  # tokenize s2
        self.common_tokens = self.tokens_intersection()

    def tokens_intersection(self):
        common_tokens = set(self.p1).intersection(self.p2)
        return common_tokens

    @staticmethod
    def ratio(a: str, b: str):
        return lev.ratio(a, b)

    def token_set_ratio(self):
        """
        Implement token_set_ratio in a similar way to
        fuzzywuzzy.fuzz.token_set_ratio(). Source:
        https://www.datacamp.com/community/tutorials/fuzzy-string-python
        """

        if not (self.s1 and self.s2):
            return 0

        common_tokens = self.common_tokens

        rest_s1 = set(self.p1).difference(common_tokens)
        rest_s2 = set(self.p2).difference(common_tokens)

        new_s1 = " ".join(sorted(common_tokens))
        new_s2 = " ".join(sorted(common_tokens) + sorted(rest_s1))
        new_s3 = " ".join(sorted(common_tokens) + sorted(rest_s2))

        combinations = itertools.combinations([new_s1, new_s2, new_s3], 2)

        maximum = 0
        for pair in combinations:
            ratio = self.ratio(pair[0], pair[1])
            if ratio > maximum:
                maximum = ratio
        return maximum
