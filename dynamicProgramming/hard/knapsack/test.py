# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 20.06.2023


import unittest
from knapsack import knapsackProblem


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
                knapsackProblem(
                    [[2, 1], [3, 4], [6, 5], [7, 6]], 10), [11, [0, 1, 2]])

    def test_case_2(self):
        self.assertEqual(
                knapsackProblem(
                    [[1, 2], [4, 3], [5, 6], [6, 7]], 10), [10, [1, 3]])

    def test_case_3(self):
        self.assertEqual(
                knapsackProblem(
                    [[6, 1], [10, 2], [12, 3], [15, 5]], 5), [22, [1, 2]])

    def test_case_4(self):
        self.assertEqual(
                knapsackProblem(
                    [[3, 4], [5, 8], [7, 9], [2, 3]], 10), [7, [2]])

    def test_case_5(self):
        self.assertEqual(
                knapsackProblem(
                    [[1, 2], [4, 3], [5, 8], [6, 7]], 10), [10, [1, 3]])
