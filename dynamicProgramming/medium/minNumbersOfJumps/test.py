# copyright 2024
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 03.02.2024

from minNumbersOfJumps import minNumberOfJumps
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
        expected = 4
        self.assertEqual(minNumberOfJumps(array), expected)
    
    def test_case_2(self):
        array = [1]
        expected = 0
        self.assertEqual(minNumberOfJumps(array), expected)
    
    def test_case_3(self):
        array = [1, 1]
        expected = 1
        self.assertEqual(minNumberOfJumps(array), expected)
    
    def test_case_4(self):
        array = [3, 1]
        expected = 1
        self.assertEqual(minNumberOfJumps(array), expected)
    
    def test_case_5(self):
        array = [1, 1, 1]
        expected = 2
        self.assertEqual(minNumberOfJumps(array), expected)

    def test_case_6(self):
        array = [2, 1, 1]
        expected = 1
        self.assertEqual(minNumberOfJumps(array), expected)
    
    def test_case_7(self):
        array = [2, 1, 2, 3, 1]
        expected = 2
        self.assertEqual(minNumberOfJumps(array), expected)
    
    def test_case_8(self):
        array = [2, 1, 2, 3, 1, 1, 1]
        expected = 3
        self.assertEqual(minNumberOfJumps(array), expected)
    
    def test_case_9(self):
        array = [2, 1, 2, 2, 1, 1, 1]
        expected = 4
        self.assertEqual(minNumberOfJumps(array), expected)
    
    def test_case_10(self):
        array = [2, 1, 2, 2, 1, 1, 1, 1]
        expected = 5
        self.assertEqual(minNumberOfJumps(array), expected)