# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 09.06.2023

import unittest
from isMonotonic import isMonotonic


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        expected = True
        actual = isMonotonic(array)
        self.assertEqual(actual, expected)
