import string
from src.preprocessing.tokenize import StringTokenize


class StringRemove(StringTokenize):
    def __init__(self, string):
        self.string = string

    def remove_something(g):
        """
        Remove the punctuation/digit etc.
        There will be NO empty space between when the
         punctuation/digits are removed.
        """

        def inner(self, keep_space=False):
            if keep_space:
                translate = str.maketrans(g(self), " " * len(g(self)))
            elif keep_space == False:
                translate = str.maketrans("", "", g(self))
            self.string = self.string.translate(translate)
            return self

        return inner

    def simple_tokenize(self):
        return self.tokenize(pattern="\s+")

    @remove_something
    def remove_digits(self):
        return string.digits

    @remove_something
    def remove_punctuation(self):
        return string.punctuation

    def remove_outer_space(self):
        self.string = self.string.strip()
        return self

    def remove_inner_space(self):
        tokenized = self.simple_tokenize()
        self.string = " ".join(tokenized)
        return self

    def remove_stopwords(self, stopwords):
        tokenized = self.simple_tokenize()
        string = " "
        for w in tokenized:
            if w not in stopwords:
                string += " " + w
        self.string = string.strip()
        return self
