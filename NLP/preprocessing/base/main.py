import contractions
import copy

from preprocessing.base.sentences.convert_case import CaseConverter
from preprocessing.base.sentences.remove_punctuation import PunctuationRemover
from preprocessing.base.sentences.replace_token import TokenReplacer
from preprocessing.base.sentences.remove_space import SpaceRemover
from preprocessing.base.sentences.stem_lemmatize import StemLemmatizerSentence


class SentenceModifierBase:
    def __init__(self):
        pass

    def replace_tokens(self):
        token_replacer = TokenReplacer()
        self.sentence = token_replacer.replace_emails(self.sentence)
        self.sentence = token_replacer.replace_urls(self.sentence)
        self.sentence = token_replacer.replace_numbers(self.sentence)
        return self

    def case_convert(self):
        case_converter = CaseConverter()
        self.sentence = case_converter.to_lower(self.sentence)
        return self

    def remove_punctuation(self, keep_space):
        punctuation_remover = PunctuationRemover()
        self.sentence = punctuation_remover.remove_punctuation(
            self.sentence, keep_space=keep_space
        )
        return self

    def remove_space(self):
        space_remover = SpaceRemover()
        self.sentence = space_remover.remove_inner_space(self.sentence)
        return self

    def replace_contractions(self):
        self.sentence = contractions.fix(self.sentence)
        return self

    def replace_with_stemmed_lemma(self):
        stem_lemmatizer = StemLemmatizerSentence()
        self.sentence = stem_lemmatizer.run(self.sentence)
        return self


class SentenceModifierFull(SentenceModifierBase):
    def run(self, sentence):
        self.sentence = copy.copy(sentence)

        self.replace_tokens()
        self.replace_contractions()
        self.case_convert()
        self.remove_punctuation(keep_space=True)
        self.remove_space()
        self.replace_with_stemmed_lemma()

        return self.sentence
