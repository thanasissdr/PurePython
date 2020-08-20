from preprocessing.preprocessors import Preprocess
from string_matching.fuzzywuzzy_style.fuzzy import Fuzzy


class FuzzyPipeline:
    def __init__(self, preprocessor, tokenizer):
        self.preprocessor = preprocessor
        self.tokenizer = tokenizer

    def token_set_ratio(self, s1, s2):

        # preprocess & tokenize
        normalized_s1 = Preprocess(s1).run(self.preprocessor, self.tokenizer)
        normalized_s2 = Preprocess(s2).run(self.preprocessor, self.tokenizer)

        # token_sort_ratio
        fuzzy_obj = Fuzzy(normalized_s1, normalized_s2)
        return fuzzy_obj.token_set_ratio()

