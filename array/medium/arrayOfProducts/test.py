# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 01.06.2023

from arrayOfProducts import arrayOfProducts, arrayOfProductsNaive
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 4, 2]
        expected = [8, 40, 10, 20]
        actual = arrayOfProducts(array)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        array = [5, 1, 4, 2]
        expected = [8, 40, 10, 20]
        actual = arrayOfProducts(array)
        self.assertEqual(actual, expected)
