import re


class StringIs:
    """
    This class only will refer to base strings, not sentences.
    """

    URL = r"(https?://)?(www\.)?[a-zA-Z0-9]+(\.[a-zA-Z]{2,3})(\.[a-zA-Z]{2,3})?"
    EMAIL = r"(\w.+)@[a-zA-Z]+\.[a-zA-Z]"
    DIGIT = r"\d+"

    def __init__(self, string):
        self.string = string

    def is_something(f):
        def inner(self):
            if re.search(f"^{f(self)}$", self.string):
                return True
            return False

        return inner

    @is_something
    def is_url(self):
        return self.URL

    @is_something
    def is_email(self):
        return self.EMAIL

    @is_something
    def is_digit(self):
        return self.DIGIT

    def is_short(self, length):
        if len(self.string) < length:
            return True
        return False
