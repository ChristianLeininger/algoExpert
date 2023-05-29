# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 29.05.2023

from threeNumberSum import threeNumberSum
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
                threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0),
                [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])
