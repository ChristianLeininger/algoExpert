# copyright 2023
# author: Christian Leininger
# Email: leininic @ tf.uni-freiburg.de
# date: 25.05.2023

from nonConstructibleChange import nonConstructibleChange
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [4, 1, 1]
        expected = 3
        actual = nonConstructibleChange(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = [5, 7, 1, 1, 2, 3, 22]
        expected = 20
        actual = nonConstructibleChange(input)
        self.assertEqual(actual, expected)
