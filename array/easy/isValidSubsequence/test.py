# copyright 2023
# author: Christian Leininger
# Email: leininic @ tf.uni-freiburg.d
# date: 24.05.2023

import unittest
from isValidSubsequence import isValidSubsequence


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertTrue(isValidSubsequence(array, sequence))

    def test_case_2(self):
        array = [5, 1, 22, 25, 0, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertFalse(isValidSubsequence(array, sequence))