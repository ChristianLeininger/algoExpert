import unittest
from twoNumberSum import twoNumberSumNaive, twoNumberSumDict, twoNumberSumSort



class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = twoNumberSumNaive([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)
    
    def test_case_2(self):
        output = twoNumberSumNaive([21, 5, -4, -9, 11, 2, 1, 7], 10)
        self.assertTrue(len(output) == 0)
    
    def test_case_3(self):
        output = twoNumberSumDict([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)
    
    def test_case_4(self):
        output = twoNumberSumSort([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)
    
    def test_case_5(self):
        output = twoNumberSumSort([21, 5, -4, -9, 11, 1, -2, 7], 10)
        self.assertTrue(len(output) == 0)
        