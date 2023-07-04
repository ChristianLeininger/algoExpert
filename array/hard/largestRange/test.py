# copyright 2023
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 01.07.2023

import unittest
from largestRange import largestRangeNaive, largestRange


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(largestRangeNaive([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]), [0, 7])

    def test_case_2(self):
        self.assertEqual(largestRangeNaive([1]), [1, 1])

    def test_case_3(self):
        self.assertEqual(largestRangeNaive([4, 2, 1, 3, 6]), [1, 4])

    def test_case_4(self):
        self.assertEqual(largestRangeNaive([4, 2, 1, 3, 6]), [1, 4])

    def test_case_5(self):
        self.assertEqual(largestRangeNaive([8, 4, 2, 10, 3, 6, 7,  1]), [1, 4])

    def test_case_6(self):
        self.assertEqual(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]), [0, 7])

    def test_case_7(self):
        self.assertEqual(largestRange([1]), [1, 1])

    def test_case_8(self):
        self.assertEqual(largestRange([4, 2, 1, 3, 6]), [1, 4])

    def test_case_9(self):
        self.assertEqual(largestRange([4, 2, 1, 3, 6]), [1, 4])

    def test_case_10(self):
        self.assertEqual(largestRange([8, 4, 2, 10, 3, 6, 7,  1]), [1, 4])
