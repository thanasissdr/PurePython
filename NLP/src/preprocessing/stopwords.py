import copy
from typing import Set


class StopWords:
    def __init__(self, stopwords=set()):
        self.stopwords = copy.copy(stopwords)

    def add(self, add_stopwords):
        self.stopwords = self.stopwords.union(add_stopwords)
        return self

    def remove(self, remove_stopwords):
        for s in remove_stopwords:
            if s in self.stopwords:
                self.stopwords.remove(s)
        return self
