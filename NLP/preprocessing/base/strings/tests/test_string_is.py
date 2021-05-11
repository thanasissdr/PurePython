import unittest

from parameterized import parameterized

from preprocessing.base.strings.string_is import StringIsRegex


class TestStringIs(unittest.TestCase):
    def setUp(self):
        self.string_is = StringIsRegex()

    @parameterized.expand(
        [
            ("wwww.abc.com@abcdefg.com", True),
            ("bob-alice@abcdefghij.com.uk.", True),
            (".@abc.co.uk", True),
        ]
    )
    def test_email(self, input, expected):

        self.assertEqual(self.string_is.is_email(input), expected)

    @parameterized.expand(
        [
            ("http://www.com@abcd.co.uk", False),
            ("www.abc.com@abcdefg.comm,", False),
            ("abcd@sldkf@abc.com", False),
            ("abcd@sldkf@abc.com", False),
            ("a@abc.com.comm", False),
            ("a@abcdefg.co.co.uk.", False),
            ("@abc.com", False),
        ]
    )
    def test_not_email(self, input, expected):

        self.assertEqual(self.string_is.is_email(input), expected)

    @parameterized.expand(
        [
            ("http://www.abc.com", True),
            ("http://www.abc.com.gr/sub/search?=search", True),
            ("https://www.abc.com/", True),
            ("www.google.co.uk", True),
            ("www.google.com/uk", True),
            ("google.com", True),
            ("www.abc.com/~tau", True),
            ("http://tb.fr/imjo", True),
            ("http://apps.fore.com/dogbook/profile/view/1234", True),
        ]
    )
    def test_is_url(self, input, expected):

        self.assertEqual(self.string_is.is_url(input), expected)

    @parameterized.expand(
        [
            ("today...but", False),
            ("http:///www.google.com", False),
            ("https:/www.google.com", False),
            ("www.t.com", False),
        ]
    )
    def test_not_url(self, input, expected):

        self.assertEqual(self.string_is.is_url(input), expected)

    @parameterized.expand(
        [
            ("1", True),
            ("10", True),
            ("-12345", True),
            ("+923409834", True),
            ("-1324.098234", True),
        ]
    )
    def test_is_number(self, input, expected):
        self.assertEqual(self.string_is.is_number(input), expected)

    @parameterized.expand([("--10", False), ("++449", False), ("-10-10", False)])
    def test_not_number(self, input, expected):

        self.assertEqual(self.string_is.is_number(input), expected)

    @parameterized.expand(
        [
            ("a", 3, True),
            ("ab", 3, True),
            ("abc", 3, False),
            ("qwerty", 5, False),
            ("blueberry", 20, True),
        ]
    )
    def test_short(self, input, short_threshold, expected):
        self.assertEqual(self.string_is.is_short(input, short_threshold), expected)

