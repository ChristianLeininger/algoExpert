# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 09.06.2023

import unittest
from zeroSumSubarray import zeroSumSubarray, ZeroSumSubarrayNaive


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [4, 2, -1, -1, 3]
        expected = True
        actual = ZeroSumSubarrayNaive(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = [4, 2, -1, -1, 3]
        expected = True
        actual = zeroSumSubarray(input)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        input = [2, 1, -3]
        expected = True
        actual = zeroSumSubarray(input)
        self.assertEqual(actual, expected)
