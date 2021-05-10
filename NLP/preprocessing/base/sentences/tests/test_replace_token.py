import re
import unittest

from parameterized import parameterized

from preprocessing.base.sentences.replace_token import TokenReplacer


class TestTokenizer(unittest.TestCase):
    def setUp(self):
        self.token_replacer = TokenReplacer()

    @parameterized.expand([("This is 1234.", "This is  #num# .")])
    def test_number_replacement(self, input, expected):
        self.assertEqual(self.token_replacer.replace_numbers(input), expected)

    @parameterized.expand(
        [
            ("The url is www.google.gr.", "The url is  #link# "),
            (
                "The url is http://apps.google.com/google/profile/view/123",
                "The url is  #link# ",
            ),
        ]
    )
    def test_link_replacement(self, input, expected):
        self.assertEqual(self.token_replacer.replace_urls(input), expected)

    @parameterized.expand(
        [("The email is google@google.com", "The email is  #email# ")]
    )
    def test_email_replacement(self, input, expected):
        self.assertEqual(self.token_replacer.replace_emails(input), expected)
