import unittest

from parameterized import parameterized

from preprocessing.base.strings.stem_lemma import StemLemmatizerString


class TestStemLemmatizer(unittest.TestCase):
    def setUp(self):
        self.stem_lemmatizer = StemLemmatizerString()

    @parameterized.expand(
        [
            ("butterflies", "butterfli"),
            ("children", "children"),
            ("playing", "play"),
            ("cried", "cri"),
            ("crying", "cri"),
            ("has played", "has play"),
            ("has", "has"),
            ("flies", "fli"),
            ("amazingly", "amaz"),
        ]
    )
    def test_stem(self, input, expected):
        self.assertEqual(self.stem_lemmatizer.stemmed(input), expected)

    @parameterized.expand(
        [
            ("children", "child"),
            ("loving", "love"),
            ("friendly", "friendly"),
            ("amazingly", "amazingly"),
        ]
    )
    def test_lemmatize(self, input, expected):
        self.assertEqual(self.stem_lemmatizer.lemmatize(input), expected)