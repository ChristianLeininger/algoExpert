# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 20.06.2023


import unittest
from longestPalindromicSubstring import longestPalindromicSubstringNaive
from longestPalindromicSubstring import is_palindrom, generate_substrings


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
                generate_substrings("aba"), ['a', 'ab', 'aba', 'b', 'ba', 'a'])

    def test_case_2(self):
        self.assertEqual(is_palindrom("abaxyzzyxf"), False)

    def test_case_3(self):
        self.assertEqual(is_palindrom("abax"), False)

    def test_case_4(self):
        self.assertEqual(is_palindrom("aba"), True)

    def test_case_5(self):
        self.assertEqual(
                longestPalindromicSubstringNaive("abaxyzzyxf"), "xyzzyx")
