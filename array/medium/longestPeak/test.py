# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 30.05.2023

from longestPeak import longestPeak
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
        expected = 6
        self.assertEqual(longestPeak(array), expected)

    def test_case_2(self):
        array = [1, 3, 2]
        expected = 3
        self.assertEqual(longestPeak(array), expected)

    def test_case_3(self):
        array = [1, 2, 3]
        expected = 0
        self.assertEqual(longestPeak(array), expected)
