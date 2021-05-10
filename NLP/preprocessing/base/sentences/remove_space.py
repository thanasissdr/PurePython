class SpaceRemover:
    def remove_outer_space(self, sentence):
        return sentence.strip()

    def remove_inner_space(self, sentence):
        return " ".join(sentence.split())
