# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 20.06.2023


import unittest
from longestPalindromicSubstring import longestPalindromicSubstringNaive
from longestPalindromicSubstring import longestPalindromicSubstring
from longestPalindromicSubstring import is_palindrom, generate_substrings
from longestPalindromicSubstring import check_odd, check_even


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

    def test_case_6(self):
        self.assertEqual(
                check_odd(string="aba", idx=1), 3)

    def test_case_7(self):
        self.assertEqual(
                check_odd(string="dcabacd", idx=1), 1)

    def test_case_8(self):
        self.assertEqual(
                check_odd(string="dcabacd", idx=3), 7)

    def test_case_9(self):
        self.assertEqual(
                check_even(string="dcabbacd", idx=4), 8)

    def test_case_10(self):
        self.assertEqual(
                longestPalindromicSubstring("abaxyzzyxf"), "xyzzyx")

    def test_case_11(self):
        self.assertEqual(
                longestPalindromicSubstring("abcdefghfedcbaa"), "aa")

    def test_case_12(self):
        self.assertEqual(
                longestPalindromicSubstring("ab12365456321bb"), "b12365456321b")
