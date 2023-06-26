# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 20.06.2023


import unittest
from oneEdit import oneEdit


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        stringOne = "hello"
        stringTwo = "helo"
        expected = True
        actual = oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        stringOne = "hello"
        stringTwo = "hello"
        expected = True
        actual = oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        stringOne = "hello"
        stringTwo = "hells"
        expected = True
        actual = oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        stringOne = "hello"
        stringTwo = "mello"
        expected = True
        actual = oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        stringOne = "hello"
        stringTwo = "helloo"
        expected = True
        actual = oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test_case_6(self):
        stringOne = "hello"
        stringTwo = "hela"
        expected = False
        actual = oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test_case_7(self):
        stringOne = "hello"
        stringTwo = "he"
        expected = False
        actual = oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test_case_8(self):
        stringOne = ""
        stringTwo = "h"
        expected = True
        actual = oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test_case_9(self):
        stringOne = ""
        stringTwo = ""
        expected = True
        actual = oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test_case_10(self):
        stringOne = "a"
        stringTwo = ""
        expected = True
        actual = oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)
