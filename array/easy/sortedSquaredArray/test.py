# copyright 2023
# author: Christian Leininger
# Email: leininic @ tf.uni-freiburg.d
# date: 24.05.2023

from sortedSquaredArray import sortedSquaredArrayNaive, sortedSquaredArray
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = sortedSquaredArrayNaive(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = [-11, 1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81, 121]
        actual = sortedSquaredArrayNaive(input)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        input = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = sortedSquaredArray(input)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        input = [-11, 1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81, 121]
        actual = sortedSquaredArray(input)
        self.assertEqual(actual, expected)
