# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 01.06.2023

from binarySearch import binarySearch
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(binarySearch(
            [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)
