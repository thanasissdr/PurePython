from nltk.stem import PorterStemmer, SnowballStemmer, WordNetLemmatizer


class StemLemmatize:

    def __init__(self, string):
        self.string = string

    def stemmed(self):
        stemmer = SnowballStemmer(language='english')
        self.string = stemmer.stem(self.string)
        return self

    def lemmatized(self):
        lemmatizer = WordNetLemmatizer()
        for pos in ['v', 'n', 'a']:
            self.string = lemmatizer.lemmatize(self.string, pos=pos)
        return self

    def lemma_stemmed(self):
        return self.lemmatized().stemmed()

