from preprocessing.base.sentences.convert_case import CaseConverter
from preprocessing.base.sentences.remove_punctuation import PunctuationRemover
from preprocessing.base.sentences.replace_token import TokenReplacer


class SentenceModifier:
    def __init__(self):
        pass

    def run(self, sentence):
        self.sentence = sentence.copy()

        self.replace_tokens()
        self.case_converter()
        self.remove_punctuation()

    def replace_token(self):
        token_replacer = TokenReplacer()
        self.sentence = token_replacer.replace_emails()
        return self

    def case_convert(self):
        case_converter = CaseConverter()
        self.sentence = case_converter.to_lower(self.sentence)
        return self

    def remove_punctuation(self, sentence):
        punctuation_remover = PunctuationRemover()
        self.sentence = punctuation_remover.remove_punctuation(self.sentence)
        return self

