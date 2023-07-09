# copyright 2023
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 06.07.2023


import unittest
from laptopRentals import laptopRentalsNaive, laptopRentals


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[0, 2], [1, 4], [4, 6], [0, 4], [7, 8], [9, 11], [3, 10]]
        expected = 3
        actual = laptopRentalsNaive(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = [[0, 4], [2, 3], [2, 3], [2, 3]]
        expected = 4
        actual = laptopRentalsNaive(input)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        input = [[1, 5], [5, 6], [6, 7], [7, 9]]
        expected = 1
        actual = laptopRentalsNaive(input)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        # Test with empty input
        input = []
        expected = 0
        actual = laptopRentalsNaive(input)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        # Test with one rental
        input = [[1, 3]]
        expected = 1
        actual = laptopRentalsNaive(input)
        self.assertEqual(actual, expected)

    def test_case_6(self):
        # Test with multiple rentals having the same start and end times
        input = [[1, 3], [1, 3], [1, 3]]
        expected = 3
        actual = laptopRentalsNaive(input)
        self.assertEqual(actual, expected)

    def test_case_7(self):
        # Test with multiple rentals where one rental
        # covers the entire time period of the others
        input = [[1, 8], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
        expected = 2
        actual = laptopRentalsNaive(input)
        self.assertEqual(actual, expected)

    def test_case_8(self):
        # Test with multiple rentals that do not overlap at all
        input = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
        expected = 1
        actual = laptopRentalsNaive(input)
        self.assertEqual(actual, expected)

    def test_case_9(self):
        # Test with multiple rentals that overlap exactly
        input = [[1, 3], [3, 5], [5, 7], [7, 9]]
        expected = 1
        actual = laptopRentalsNaive(input)
        self.assertEqual(actual, expected)

    def test_case_10(self):
        # Test with multiple rentals that all start at the same time
        input = [[1, 3], [1, 4], [1, 5]]
        expected = 3
        actual = laptopRentalsNaive(input)
        self.assertEqual(actual, expected)

    def test_case_11(self):
        # Test with multiple rentals that all end at the same time
        input = [[1, 5], [2, 5], [3, 5]]
        expected = 3
        actual = laptopRentalsNaive(input)
        self.assertEqual(actual, expected)

    def test_case_12(self):
        # Test with a large number of rentals
        input = [[i, i+1] for i in range(1000)]
        expected = 1
        actual = laptopRentalsNaive(input)
        self.assertEqual(actual, expected)

    def test_case_13(self):
        # Test with rentals that end at the start time of others
        input = [[1, 2], [2, 3], [3, 4]]
        expected = 1
        actual = laptopRentalsNaive(input)
        self.assertEqual(actual, expected)

    def test_case_14(self):
        # Test with rentals that end at the start time of others
        input = [[1, 2], [2, 3], [3, 4]]
        expected = 1
        actual = laptopRentals(input)
        self.assertEqual(actual, expected)
