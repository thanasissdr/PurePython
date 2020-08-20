from abc import ABC, abstractmethod
from base.main import StringSentence


class ProcessorCreator(ABC):
    @abstractmethod
    def process(self):
        pass


class WhiteSpaceProcessor(ProcessorCreator):
    def process(self, s: str):
        processed_s = (
            StringSentence(s).remove_outer_space().remove_inner_space().to_lower()
        )
        return processed_s.string


class WhiteSpacePunctuationProcessor(ProcessorCreator):
    def __init__(self, keep_space=True):
        self.keep_space = keep_space

    def process(self, s: str):
        processed_s = (
            StringSentence(s)
            .remove_outer_space()
            .remove_inner_space()
            .remove_punctuation(keep_space=self.keep_space)
            .to_lower()
        )
        return processed_s.string


print(
    WhiteSpacePunctuationProcessor(keep_space=False).process(
        "lskjdflj 234!#!#$!@#$!#$!@#$#!$!@#$!32          lk3j1l3kj4l3 k4l12jk3 4l1k32j 4l13j24          s       "
    )
)

