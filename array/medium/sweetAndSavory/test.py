# copyright 2023
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 01.07.2023

import unittest
from sweetAndSavory import sweetAndSavory


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        dishes = [-3, -5, 1, 7]
        target = 8
        expected = [-3, 7]
        actual = sweetAndSavory(dishes, target)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        dishes = [4]
        target = 10
        expected = [0, 0]
        actual = sweetAndSavory(dishes, target)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        dishes = [5, -10]
        target = -4
        expected = [-10, 5]
        actual = sweetAndSavory(dishes, target)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        dishes = [-5, 10]
        target = 0
        expected = [0, 0]
        actual = sweetAndSavory(dishes, target)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        dishes = [5, -5, 5, -5, 5, -5]
        target = 5
        expected = [-5, 5]
        actual = sweetAndSavory(dishes, target)
        self.assertEqual(actual, expected)

    def test_case_6(self):
        dishes = [5, -5, 5, -5, 5, -5]
        target = 0
        expected = [-5, 5]
        actual = sweetAndSavory(dishes, target)
        self.assertEqual(actual, expected)

    def test_case_7(self):
        dishes = [2, 5, -4, -7, 12, 100, -25]
        target = -7
        excepted = [-25, 12]
        actual = sweetAndSavory(dishes, target)
        self.assertEqual(actual, excepted)
