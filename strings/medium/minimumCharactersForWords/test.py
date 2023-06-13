# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 13.06.2023

import unittest
from minimumCharactersForWords import minimumCharactersForWords


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = ["this", "that", "did", "deed", "them!", "a"]
        expected = ["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
        actual = minimumCharactersForWords(input)
        self.assertCountEqual(actual, expected)

    def test_case_2(self):
        input = ["a", "abc", "ab", "boo"]
        expected = ["a", "b", "c", "o", "o"]
        actual = minimumCharactersForWords(input)
        self.assertCountEqual(actual, expected)

    def test_case_3(self):
        input = ["this", "that", "they", "them", "their", "there", "time"]
        expected = ["a", "e", "e", "h", "i", "m", "r", "s", "t", "t", "y"]
        actual = minimumCharactersForWords(input)
        self.assertCountEqual(actual, expected)
