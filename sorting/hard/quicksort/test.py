# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 29.05.2023


from quicksort import pivo_sort
import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        array = [5, 8, 2]
        self.assertEqual(
                pivo_sort(array=array, left=0, right=len(array) - 1, pivo_idx=0),
                [2, 5, 8])

    def test_case_2(self):
        array = [2, 3, -1, 4, 1, -5, 9, 2, -6, 5, 3, -5]
        self.assertEqual(
                pivo_sort(array=array, left=0, right=len(array) - 1, pivo_idx=0),
                [-5, -5, -1, -6, 1, 2, 9, 2, 4, 5, 3, 3])

    def test_case_3(self):
        array = [3, -1, 4, 1, -5, 9, 2, -6, 5, 3, -5]
        self.assertEqual(
                pivo_sort(array=array, left=0, right=len(array) - 1, pivo_idx=0),
                [2, -1, -5, 1, -5, -6, 3, 9, 5, 3, 4])

    def test_case_4(self):
        array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.assertEqual(
                pivo_sort(array=array, left=0, right=len(array) - 1, pivo_idx=0),
                [1, 1, 2, 3, 5, 9, 4, 6, 5, 3, 5])

    def test_case_5(self):
        array = [8]
        self.assertEqual(
                pivo_sort(array=array, left=0, right=len(array) - 1, pivo_idx=0),  [8])

    def test_case_6(self):
        array = [10, 7, 8]
        self.assertEqual(
                pivo_sort(array=array, left=0, right=len(array) - 1, pivo_idx=0),
                [8, 7, 10])

    def test_case_7(self):
        array = [1, -9, 3, -2, 10, 7, 8]
        self.assertEqual(
                pivo_sort(array=array, left=0, right=len(array) - 1, pivo_idx=0),
                [-2, -9, 1, 3, 10, 7, 8])
