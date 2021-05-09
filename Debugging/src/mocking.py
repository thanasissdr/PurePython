import unittest

from unittest import mock


from basic import Simple


class TestSimple(unittest.TestCase):
    def test_simple(self):
        m = mock.Mock()
        m.help = 2

        self.assertEqual(m.help, 2)

    def test_function_call(self):
        m = mock.Mock()
        m.return_value.squared.return_value = 42
        m.squared()
        m.squared.assert_called_once()

    def test_function_result(self):
        m = mock.Mock()
        m.squared.return_value = 100
        self.assertEqual(m.squared(), 100)

