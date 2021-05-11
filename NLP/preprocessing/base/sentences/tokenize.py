import re


class Tokenizer:
    def tokenize(self, sentence, pattern=" "):
        return re.split(pattern, sentence)
