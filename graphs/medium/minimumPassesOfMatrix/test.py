# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 01.07.2023

import unittest
from minimumPassesOfMatrix import minimumPassesOfMatrixNaive


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        matrix = [
            [0, -1, -3, 2, 0],
            [1, -2, -5, -1, -3],
            [3, 0, 0, -4, -1],
        ]
        expected = 3
        actual = minimumPassesOfMatrixNaive(matrix=matrix)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        matrix = [
            [1, 0, 0, -2, -3],
            [-4, -5, -6, -2, -1],
            [0, 0, 0, 0, -1],
            [1, 2, 3, 0, -2]
            ]
        expected = 7
        actual = minimumPassesOfMatrixNaive(matrix=matrix)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        matrix = [
            [1, 0, 0, -2, -3],
            [-4, -5, -6, -2, -1],
            [0, 0, 0, 0, -1],
            [1, 2, 3, 0, 3]
        ]
        expected = 4
        actual = minimumPassesOfMatrixNaive(matrix=matrix)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        matrix = [
            [1, 0, 0, -2, -3],
            [-4, -5, -6, -2, -1],
            [0, 0, 0, 0, -1],
            [-1, 0, 3, 0, 3]
        ]
        expected = -1
        actual = minimumPassesOfMatrixNaive(matrix=matrix)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        matrix = [[-1]]
        expected = -1
        actual = minimumPassesOfMatrixNaive(matrix=matrix)
        self.assertEqual(actual, expected)

    def test_case_6(self):
        matrix = [
            [-1, -9, 0, -1, 0],
            [-9, -4, -5, 4, -8],
            [2, 0, 0, -3, 0],
            [0, -17, -4, 2, -5]
        ]
        expected = 3
        actual = minimumPassesOfMatrixNaive(matrix=matrix)
        self.assertEqual(actual, expected)

    def test_case_6(self):
        matrix = [
            [-2, -3, -4, -1, -9],
            [-4, -3, -4, -1, -2],
            [-6, -7, -2, -1, -1],
            [0, 0, 0, 0, -3],
            [1, -2, -3, -6, -1]
            ]
        expected = 12
        actual = minimumPassesOfMatrixNaive(matrix=matrix)
        self.assertEqual(actual, expected)

    def test_case_6(self):
        matrix = [[-2, 0, -2, 1], [-2, -1, -1, -1]]
        expected = 5
        actual = minimumPassesOfMatrixNaive(matrix=matrix)
        self.assertEqual(actual, expected)
