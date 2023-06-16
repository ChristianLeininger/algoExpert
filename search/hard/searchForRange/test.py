# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 16.06.2023

import unittest

from searchForRange import searchForRange


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
                searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45), [4, 9])

    def test_case_2(self):
        self.assertEqual(
                searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 3), [-1, -1])

    def test_case_3(self):
        self.assertEqual(
                searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 75), [-1, -1])

    def test_case_4(self):
        self.assertEqual(
                searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 0), [0, 0])

    def test_case_5(self):
        self.assertEqual(
                searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 1), [1, 1])
