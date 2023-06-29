# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 29.06.2023


import unittest
from spiralTraverse import spiralTraverse


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(spiralTraverse(matrix), expected)

    def test_case_2(self):
        matrix = [[1]]
        expected = [1]
        self.assertEqual(spiralTraverse(matrix), expected)

    def test_case_3(self):
        matrix = [[1, 2], [4, 3]]
        expected = [1, 2, 3, 4]
        self.assertEqual(spiralTraverse(matrix), expected)

    def test_case_4(self):
        matrix = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(spiralTraverse(matrix), expected)

    def test_case_5(self):
        matrix = [
                [1,  2,  3,  4,  5],
                [16, 17, 18, 19,  6],
                [15, 24, 25, 20,  7],
                [14, 23, 22, 21,  8],
                [13, 12, 11, 10,  9]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
