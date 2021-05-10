import re

from functools import wraps


class StringIs:
    def is_short(self, string, length):
        if len(string) < length:
            return True
        return False


class StringIsRegex(StringIs):
    """
    This class only will refer to base strings, not sentences.
    """

    URL = r"((http|https)://)?(www\.)?[a-zA-Z0-9\-]+(\.[a-zA-Z\-]{2,256}){1,3}(/[a-zA-Z0-9]*)*([a-zA-Z-0-9\\&=\?\~\.\-\+]+)*"

    EMAIL = (
        r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,3}(\.[a-zA-Z0-9\-\.]{2,3})?"
    )
    NUMBER = r"(\+|\-)?[0-9]+(\.\d+)?"

    def __init__(self):
        pass

    def regex_based(f):
        @wraps(f)
        def inner(self, string):
            regex = f(self)
            if re.search(f"^{regex}$", string):
                return True
            return False

        return inner

    @regex_based
    def is_url(self):
        return self.URL

    @regex_based
    def is_email(self):
        return self.EMAIL

    @regex_based
    def is_number(self):
        return self.NUMBER


# class StringIsSpacy(StringIs):
#     import spacy

#     nlp = spacy.load("en_core_web_sm")

#     def is_something(g):
#         @wraps(g)
#         def inner(self, string):
#             doc = self.nlp(string)[0]
#             return g(self, doc)

#         return inner

#     @is_something
#     def is_email(self, x):
#         return x.like_email

#     @is_something
#     def is_url(self, x):
#         return x.like_url

