import unittest

from parameterized import parameterized

from preprocessing.base.sentences.convert_case import CaseConverter


class TestCaseConverter(unittest.TestCase):
    def setUp(self):
        self.case_converter = CaseConverter()

    @parameterized.expand(
        [
            ("A", "a"),
            ("ABC", "abc"),
            ("this iS tHE bEst Apple!", "this is the best apple!"),
            ("there is", "there is"),
            ("12 ?!E#$ wrong 1", "12 ?!e#$ wrong 1"),
        ]
    )
    def test_lower(self, input, expected):

        self.assertEqual(self.case_converter.to_lower(input), expected)

    @parameterized.expand(
        [
            ("a", "A"),
            ("abc", "ABC"),
            ("this iS tHE bEst Apple!", "THIS IS THE BEST APPLE!"),
            ("THERE IS", "THERE IS"),
            ("12 ?!e#$ wrong 1", "12 ?!E#$ WRONG 1"),
        ]
    )
    def test_upper(self, input, expected):

        self.assertEqual(self.case_converter.to_upper(input), expected)

