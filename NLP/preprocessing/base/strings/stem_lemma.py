from nltk.stem import PorterStemmer, SnowballStemmer, WordNetLemmatizer


class StemLemmatizerStringBase:
    def __init__(self, stemmer, lemmatizer):
        self.stemmer = stemmer
        self.lemmatizer = lemmatizer

    def stemmed(self, string):
        stemmed_string = self.stemmer.stem(string)
        return stemmed_string

    def lemmatize(self, string):
        tmp_lemma = self.lemmatizer.lemmatize(string, pos="v")
        for pos in ["n", "a"]:
            lemmatized_string = self.lemmatizer.lemmatize(string, pos=pos)
            if len(lemmatized_string) < len(tmp_lemma):
                tmp_lemma = lemmatized_string
        return tmp_lemma

    def lemma_stemmed(self, string):
        lemmatized_string = self.lemmatize(string)
        return self.stemmed(lemmatized_string)


class StemLemmatizerString(StemLemmatizerStringBase):
    def __init__(self):
        super().__init__(
            stemmer=SnowballStemmer(language="english"), lemmatizer=WordNetLemmatizer()
        )
