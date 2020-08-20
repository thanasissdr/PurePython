from typing import List


class Preprocess:
    def __init__(self, s: str):
        self.s = s

    def preprocess(self, preprocessor):
        self.s = preprocessor.process(self.s)
        return self

    def tokenize(self, tokenizer):
        tokenized_s = tokenizer.tokenize(self.s)
        return tokenized_s

    @staticmethod
    def join_string(string_list: List):
        return " ".join(string_list)

    def run(self, processor, tokenizer):
        tokenized_s = self.preprocess(processor).tokenize(tokenizer)
        return self.join_string(tokenized_s)
