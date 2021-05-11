from preprocessing.base.strings.stem_lemma import StemLemmatizerString
from preprocessing.base.sentences.tokenize import Tokenizer


class StemLemmatizerSentenceBase:
    def __init__(self, stem_lemmatizer, tokenizer):
        self.stem_lemmatizer = stem_lemmatizer
        self.tokenizer = tokenizer

    def run(self, sentence):
        tokenized_sentence = self.tokenizer.tokenize(sentence, pattern=" ")

        stemmed_lemma_list = []
        for s in tokenized_sentence:
            stemmed_lemma = self.stem_lemmatizer.lemma_stemmed(s)
            stemmed_lemma_list.append(stemmed_lemma)
        return " ".join(stemmed_lemma_list)


class StemLemmatizerSentence(StemLemmatizerSentenceBase):
    def __init__(self):
        super().__init__(StemLemmatizerString(), Tokenizer())