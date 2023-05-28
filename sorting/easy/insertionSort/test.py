# copyright 2023
# author: Christian Leininger
# Email: leininic @ tf.uni-freiburg.de
# date: 28.05.2023


import unittest
from insertionSort import insertionSort


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
                insertionSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])
