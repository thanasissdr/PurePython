from nltk.stem import PorterStemmer, SnowballStemmer, WordNetLemmatizer


class StemLemmatizer:
    def __init__(self):
        pass

    def stemmed(self, string):
        stemmer = SnowballStemmer(language="english")
        stemmed_string = stemmer.stem(string)
        return stemmed_string

    def lemmatized(self, string):
        lemmatizer = WordNetLemmatizer()
        for pos in ["v", "n", "a"]:
            lemmatized_string = lemmatizer.lemmatize(string, pos=pos)
        return lemmatized_string

    def lemma_stemmed(self, string):
        lemmatized_string = self.lemmatized(string)
        return self.stemmed(lemmatized_string)


if __name__ == "__main__":

    strings = [
        "butterflies",
        "children",
        "child",
        "training",
        "untrained",
        "rhymes",
        "flies",
    ]

    stemmed_lemmatizer = StemLemmatizer()
    print("\n")
    for s in strings:
        print(f"{s} -> {stemmed_lemmatizer.lemma_stemmed(s)}")

