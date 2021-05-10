from typing import List


class Preprocess:
    def __init__(self, preprocessor, tokenizer):
        self.preprocessor = preprocessor
        self.tokenizer = tokenizer

    def preprocess(self, s):
        preprocessed_s = self.preprocessor.process(s)
        return preprocessed_s

    def tokenize(self, tokenizer):
        tokenized_s = tokenizer.tokenize(self.s)
        return tokenized_s

    @staticmethod
    def join_string(string_list: List):
        return " ".join(string_list)

    def run(self, s):
        preprocessed_s = self.preprocess(s)
        tokenized_s = self.tokenizer.tokenize(preprocessed_s)
        return self.join_string(tokenized_s)
