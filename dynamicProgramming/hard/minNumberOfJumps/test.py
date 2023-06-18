# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 18.06.2023


import unittest
from minNumberOfJumps import minNumberOfJumpsNaive


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
                minNumberOfJumpsNaive([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]), 4)

    def test_case_2(self):
        self.assertEqual(minNumberOfJumpsNaive([2, 1, 2, 3, 1, 1, 1]), 3)
