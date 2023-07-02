# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 01.07.2023


import unittest
from validStartingCity import validStartingCity


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        distances = [5, 25, 15, 10, 15]
        fuel = [1, 2, 1, 0, 3]
        mpg = 10
        expected = 4
        actual = validStartingCity(distances, fuel, mpg)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        distances = [10, 20, 10, 15, 5, 15, 25]
        fuel = [0, 2, 1, 0, 0, 1, 1]
        mpg = 20
        expected = 1
        actual = validStartingCity(distances, fuel, mpg)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        distances = [30, 25, 5, 100, 40]
        fuel = [3, 2, 1, 0, 4]
        mpg = 20
        expected = 4
        actual = validStartingCity(distances, fuel, mpg)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        distances = [1, 3, 10, 6, 7, 7, 2, 4]
        fuel = [1, 1, 1, 1, 1, 1, 1, 1]
        mpg = 5
        expected = 6
        actual = validStartingCity(distances, fuel, mpg)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        distances = [5, 2, 3]
        fuel = [1, 0, 1]
        mpg = 5
        expected = 2
        actual = validStartingCity(distances, fuel, mpg)
        self.assertEqual(actual, expected)
