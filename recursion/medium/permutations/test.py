# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 20.06.2023

import unittest
from permutations import get_permutations


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        perms = get_permutations([])
        self.assertTrue(len(perms) == 0)

    def test_case_2(self):
        perms = get_permutations([1])
        self.assertTrue(len(perms) == 1)
        self.assertTrue([1] in perms)

    def test_case_3(self):
        perms = get_permutations([1, 2])
        self.assertTrue(len(perms) == 2)
        self.assertTrue([1, 2] in perms)
        self.assertTrue([2, 1] in perms)

    def test_case_4(self):
        perms = get_permutations([1, 2, 3])
        self.assertTrue(len(perms) == 6)
        self.assertTrue([1, 2, 3] in perms)
        self.assertTrue([1, 3, 2] in perms)
        self.assertTrue([2, 1, 3] in perms)
        self.assertTrue([2, 3, 1] in perms)
        self.assertTrue([3, 1, 2] in perms)
        self.assertTrue([3, 2, 1] in perms)
