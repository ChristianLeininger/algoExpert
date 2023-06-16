# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 16.06.2023


import unittest
from mergeOverlappingIntervals import mergeOverlappingIntervals


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
        expected = [[1, 2], [3, 8], [9, 10]]
        actual = mergeOverlappingIntervals(intervals=intervals)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        intervals = [[1, 2], [4, 7], [6, 8], [3, 5], [9, 10]]
        expected = [[1, 2], [3, 8], [9, 10]]
        actual = mergeOverlappingIntervals(intervals=intervals)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        intervals = [[1, 11], [3, 5], [4, 7], [6, 8], [9, 10]]
        expected = [[1, 11]]
        actual = mergeOverlappingIntervals(intervals=intervals)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        intervals = []
        expected = []
        actual = mergeOverlappingIntervals(intervals=intervals)
        self.assertEqual(actual, expected)
