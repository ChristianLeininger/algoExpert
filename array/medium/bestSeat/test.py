# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 29.06.2023


import unittest
from bestSeat import bestSeat


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [1, 0, 1, 0, 0, 0, 1]
        expected = 4
        actual = bestSeat(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = [1]
        expected = -1
        actual = bestSeat(input)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        input = [1, 0, 1]
        expected = 1
        actual = bestSeat(input)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        input = [1, 1, 1]
        expected = -1
        actual = bestSeat(input)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        input = [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1]
        expected = 5
        actual = bestSeat(input)
        self.assertEqual(actual, expected)
