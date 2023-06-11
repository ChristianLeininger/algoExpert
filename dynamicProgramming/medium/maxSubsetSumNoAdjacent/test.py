# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 09.06.2023


from maxSubsetSumNoAdjacent import maxSubsetSumNoAdjacent
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(maxSubsetSumNoAdjacent(
            [75, 105, 120, 75, 90, 135]), 330)

    def test_case_2(self):
        self.assertEqual(maxSubsetSumNoAdjacent([]), 0)

    def test_case_3(self):
        self.assertEqual(maxSubsetSumNoAdjacent([1, 2]), 2)

    def test_case_4(self):
        self.assertEqual(maxSubsetSumNoAdjacent([75, 105, 120]), 195)
