# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 01.07.2023

import unittest
from subarraySort import subarraySort


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
                subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [3, 9])

    def test_case_2(self):
        self.assertEqual(
                subarraySort([1, 2, 3, 4]), [-1, -1])

    def test_case_3(self):
        self.assertEqual(
                subarraySort([2, 1]), [0, 1])

    def test_case_4(self):
        self.assertEqual(
                subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 13, 14, 16, 18, 19]), [4, 6])

    def test_case_5(self):
        self.assertEqual(
                subarraySort([1, 2, 8, 4, 5]), [2, 4])

    def test_case_6(self):
        self.assertEqual(
                subarraySort([4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 51, 7]), [0, 12])

    def test_case_7(self):
        self.assertEqual(
                subarraySort([4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57]), [0, 11])

    def test_case_8(self):
        self.assertEqual(
                subarraySort([-41, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 51, 7]), [1, 12])

    def test_case_9(self):
        self.assertEqual(
                subarraySort([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]), [-1, -1])
