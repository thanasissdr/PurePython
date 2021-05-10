import string


class PunctuationRemover:
    def __init__(self):
        pass

    def remove_something(g):
        def inner(self, sentence, keep_space=False):
            if keep_space:
                translate = str.maketrans(g(self), " " * len(g(self)))
            elif keep_space == False:
                translate = str.maketrans("", "", g(self))
            sentence = sentence.translate(translate)
            return sentence

        return inner

    @remove_something
    def remove_punctuation(self):
        return string.punctuation

