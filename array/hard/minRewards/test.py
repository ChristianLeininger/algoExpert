# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 01.07.2023

import unittest
from minRewards import minRewards


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(minRewards(array=[8, 4, 2, 1, 3, 6, 7, 9, 5]), 25)

    def test_case_2(self):
        self.assertEqual(minRewards(array=[5, 10]), 3)

    def test_case_3(self):
        self.assertEqual(minRewards(array=[4, 2, 1, 3]), 8)

    def test_case_4(self):
        self.assertEqual(minRewards(array=[0, 4, 2, 1, 3]), 9)

    def test_case_5(self):
        self.assertEqual(minRewards(array=[1, 2, 2]), 4)

    def test_case_6(self):
        self.assertEqual(minRewards(array=[1, 2, 3, 4, 5]), 15)

    def test_case_7(self):
        self.assertEqual(minRewards(array=[5, 4, 3, 2, 1]), 15)

    def test_case_8(self):
        self.assertEqual(minRewards(array=[9, 19, 29, 39, 49, 59, 69, 79]), 36)

    def test_case_9(self):
        self.assertEqual(minRewards(array=[8, 4, 6, 2, 9, 7, 1, 3, 5]), 17)

    def test_case_10(self):
        self.assertEqual(minRewards(array=[7, 10, 9, 4, 2, 1, 3, 6, 5]), 22)
