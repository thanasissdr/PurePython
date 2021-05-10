import re
import unittest

from parameterized import parameterized

from preprocessing.base.sentences.tokenize import Tokenizer


class TestTokenizer(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer()

    @parameterized.expand(
        [
            ("this is a string", " ", ["this", "is", "a", "string"]),
            ("this;is;a;string", ";", ["this", "is", "a", "string"]),
            ("this is a string", re.compile(" "), ["this", "is", "a", "string"]),
        ]
    )
    def test_tokenize(self, string, pattern, expected):
        self.assertEqual(self.tokenizer.tokenize(string, pattern), expected)
