# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 30.05.2023

import unittest
from numberOfWaysToMakeChange import numberOfWaysToMakeChange


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(numberOfWaysToMakeChange(6, [1, 5]), 2)

    def test_case_2(self):
        self.assertEqual(numberOfWaysToMakeChange(0, [2, 3, 4, 7]), 1)

    def test_case_3(self):
        self.assertEqual(numberOfWaysToMakeChange(9, [5]), 0)

    def test_case_4(self):
        self.assertEqual(numberOfWaysToMakeChange(10, [1, 5, 10]), 4)
