# copyright 2023
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 06.07.2023


import unittest
from minimumAreaRectangle import minimumAreaRectangle


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [
                [1, 5], [5, 1], [4, 2], [2, 4],
                [2, 2], [1, 2], [4, 5], [2, 5], [-1, -2]]
        expected = 3
        actual = minimumAreaRectangle(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = [[-4, 4], [4, 4], [4, -2], [-4, -2], [0, -2], [4, 2], [0, 2]]
        expected = 16
        actual = minimumAreaRectangle(input)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        input = [
                [-4, 4], [4, 4], [4, -2], [-4, -2], [0, -2],
                [4, 2], [0, 2], [0, 4], [2, 3], [0, 3], [2, 4]]
        expected = 2
        actual = minimumAreaRectangle(input)
        self.assertEqual(actual, expected)
