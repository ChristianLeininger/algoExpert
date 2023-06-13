# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 12.06.2023


from maxSumIncreasingSubsequence import maxSumIncreasingSubsequenceNaive
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(maxSumIncreasingSubsequenceNaive(
            [10, 70, 20, 30, 50, 11, 30]), [110, [10, 20, 30, 50]])

    def test_case_2(self):
        self.assertEqual(maxSumIncreasingSubsequenceNaive(
            [10, 70, 20, 30]), [80, [10, 70]])
