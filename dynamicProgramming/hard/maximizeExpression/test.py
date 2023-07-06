# copyright 2023
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 01.07.2023

import unittest
from maximizeExpression import maximizeExpressionNaive, maximizeExpression


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [3, 6, 1, -3, 2, 7]
        expected = 4
        actual = maximizeExpressionNaive(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = [3, 9, 10, 1, 30, 40]
        expected = 3
        actual = maximizeExpressionNaive(input)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        input = [40, 30, 1, 10, 9, 3]
        expected = 46
        actual = maximizeExpressionNaive(input)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        input = [-1, 2, -1, -2, -2, 1, -1]
        expected = 6
        actual = maximizeExpressionNaive(input)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        input = [10, 5, 10, 5]
        expected = 10
        actual = maximizeExpressionNaive(input)
        self.assertEqual(actual, expected)

    def test_case_6(self):
        input = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
        expected = 1
        actual = maximizeExpressionNaive(input)
        self.assertEqual(actual, expected)

    def test_case_7(self):
        input = [34, 21, 22, 0, -98, -72, 100, 23]
        expected = 209
        actual = maximizeExpressionNaive(input)
        self.assertEqual(actual, expected)

    def test_case_8(self):
        input = [5, 2, 2, 1, -2, 2, -9, 0]
        expected = 18
        actual = maximizeExpressionNaive(input)
        self.assertEqual(actual, expected)

    def test_case_9(self):
        input = [5, 10, 5, 10]
        expected = -10
        actual = maximizeExpressionNaive(input)
        self.assertEqual(actual, expected)

    def test_case_10(self):
        input = [3, -1, 1, -1, -2, 4, 5, -4]
        expected = 14
        actual = maximizeExpressionNaive(input)
        self.assertEqual(actual, expected)
