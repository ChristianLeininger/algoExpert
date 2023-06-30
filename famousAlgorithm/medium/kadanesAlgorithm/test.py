# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 29.06.2023

import unittest
from kadanesAlgorithm import kadanesAlgorithmNaive, kadanesAlgorithm


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
                kadanesAlgorithmNaive(
                    [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]), 19)

    def test_case_2(self):
        self.assertEqual(
            kadanesAlgorithmNaive(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 55)

    def test_case_3(self):
        self.assertEqual(
                kadanesAlgorithmNaive(
                    [-2, 1]), 1)

    def test_case_4(self):
        self.assertEqual(
                kadanesAlgorithmNaive(
                    [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), -1)

    def test_case_5(self):
        self.assertEqual(
                kadanesAlgorithmNaive(
                    [100, 8, 5, -9, 1, 3, -2, 3, 4, 7, 2, -18, 6, 3, 1, -5, 6, 20, -23, 15, 1, -3, 4]), 135)

    def test_case_6(self):
        self.assertEqual(
                kadanesAlgorithmNaive(
                    [8, 5, -9, 1, 3, -2, 3, 4, 7, 2, -18, 6, 3, 1, -5, 6, 20, -23, 15, 1, -3, 4]), 35)

    def test_case_7(self):
        self.assertEqual(
                kadanesAlgorithm(
                    [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]), 19)

    def test_case_8(self):
        self.assertEqual(
                kadanesAlgorithm(
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 55)

    def test_case_9(self):
        self.assertEqual(
                kadanesAlgorithm(
                    [-2, 1]), 1)

    def test_case_10(self):
        self.assertEqual(
                kadanesAlgorithm(
                    [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), -1)

    def test_case_11(self):
        self.assertEqual(
                kadanesAlgorithm(
                    [100, 8, 5, -9, 1, 3, -2, 3, 4, 7, 2, -18, 6, 3, 1, -5, 6, 20, -23, 15, 1, -3, 4]), 135)

    def test_case_12(self):
        self.assertEqual(
                kadanesAlgorithm(
                    [8, 5, -9, 1, 3, -2, 3, 4, 7, 2, -18, 6, 3, 1, -5, 6, 20, -23, 15, 1, -3, 4]), 35)
