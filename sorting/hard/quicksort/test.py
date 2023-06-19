# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 29.05.2023


from quicksort import partition, quickSort
import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        array = [5, 8, 2]
        self.assertEqual(
             partition(array=array, left=0, right=len(array) - 1)[0],
                [2, 5, 8])

    def test_case_2(self):
        array = [2, 3, -1, 4, 1, -5, 9, 2, -6, 5, 3, -5]
        self.assertEqual(
             partition(array=array, left=0, right=len(array) - 1)[0],
                [-5, -5, -1, -6, 1, 2, 9, 2, 4, 5, 3, 3])

    def test_case_3(self):
        array = [3, -1, 4, 1, -5, 9, 2, -6, 5, 3, -5]
        self.assertEqual(
             partition(array=array, left=0, right=len(array) - 1)[0],
                [2, -1, -5, 1, -5, -6, 3, 9, 5, 3, 4])

    def test_case_4(self):
        array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.assertEqual(
             partition(array=array, left=0, right=len(array) - 1)[0],
                [1, 1, 2, 3, 5, 9, 4, 6, 5, 3, 5])

    def test_case_5(self):
        array = [8]
        self.assertEqual(
             partition(array=array, left=0, right=len(array) - 1)[0],  [8])

    def test_case_6(self):
        array = [10, 7, 8]
        self.assertEqual(
             partition(array=array, left=0, right=len(array) - 1)[0],
                [8, 7, 10])

    def test_case_7(self):
        array = [1, -9, 3, -2, 10, 7, 8]
        self.assertEqual(
             partition(array=array, left=0, right=len(array) - 1)[0],
                [-2, -9, 1, 3, 10, 7, 8])

    def test_case_8(self):
        self.assertEqual(
            quickSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])

    def test_case_9(self):
        self.assertEqual(
            quickSort([2, 2, 2, 1, 2, 3, 2, 2]), [1, 2, 2, 2, 2, 2, 2, 3])

    def test_case_10(self):
        self.assertEqual(quickSort([]), [])

    def test_case_11(self):
        self.assertEqual(quickSort([1]), [1])
