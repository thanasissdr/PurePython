import re


class Tokenizer:
    def tokenize(self, string, pattern=" "):
        return re.split(pattern, string)
