from abc import ABC, abstractmethod
from preprocessing.base.tokenize import StringTokenize


class TokenizerCreator(ABC):
    @abstractmethod
    def tokenize(self):
        pass


class SpaceTokenizer(TokenizerCreator):
    def tokenize(self, s: str):
        tokenized_s = StringTokenize(s).tokenize("\s")
        return tokenized_s

