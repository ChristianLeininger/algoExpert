# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 28.06.2023


import unittest
from bestDigits import bestDigits


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        number = "462839"
        numDigits = 2
        expected = "6839"
        actual = bestDigits(number, numDigits)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        number = "991199"
        numDigits = 2
        expected = "9999"
        actual = bestDigits(number, numDigits)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        number = "998159"
        numDigits = 3
        expected = "999"
        actual = bestDigits(number, numDigits)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        number = "1234567890"
        numDigits = 5
        expected = "67890"
        actual = bestDigits(number, numDigits)
        self.assertEqual(actual, expected)
