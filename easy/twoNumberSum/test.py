import unittest
from twoNumberSum import twoNumberSumNaive, twoNumberSumDict



class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = twoNumberSumNaive([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)
    
    def test_case_2(self):
        output = twoNumberSumNaive([3, 5, -4, 8, 11, 2, 1, 6], [])
        self.assertTrue(len(output) == 0)
    
    def test_case_3(self):
        output = twoNumberSumDict([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)
    
    def test_case_4(self):
        output = twoNumberSumNaive([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)