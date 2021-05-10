import re


from preprocessing.base.strings.string_is import StringIsRegex


class TokenReplacer:
    def sub_pattern(pattern_to_replace):
        def wrapper(g):
            def inner(self, sentence):
                pattern = re.compile(f"{pattern_to_replace}")
                sentence = pattern.sub(g, sentence)
                return sentence

            return inner

        return wrapper

    @sub_pattern(StringIsRegex.NUMBER)
    def replace_numbers(self):
        return " #num# "

    @sub_pattern(StringIsRegex.URL)
    def replace_urls(self):
        return " #link# "

    @sub_pattern(StringIsRegex.EMAIL)
    def replace_emails(self):
        return " #email# "
