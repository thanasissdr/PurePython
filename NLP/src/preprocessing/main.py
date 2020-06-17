import re
from src.preprocessing.stem_lemma import StemLemmatize
from src.preprocessing.convert import StringConvert
from src.preprocessing.remove import StringRemove
from src.preprocessing.string_is import StringIs



class StringSentence(StringIs, StringRemove, StringConvert):
    """
    This class will manipulate sentences as a string.
    """
    
    def __init__(self, string):
        self.string = string
    
    def sub_pattern(pattern_to_replace):
        def wrapper(g):
            def inner(self):
                pattern = re.compile(pattern_to_replace)
                self.string = pattern.sub(g, self.string)
                return self
            return inner
        return wrapper
    
    @sub_pattern(StringIs.DIGIT)
    def replace_numbers(self):
        return '#num#'
    
    @sub_pattern(f'\s?{StringIs.URL}\s?')
    def replace_urls(self):
        return ' #link# '
    
    
    def lemmatize(self):
        string_list = [StemLemmatize(i).lemmatized().string for i in self.tokenize()]
        self.string = " ".join(string_list)
        return self
