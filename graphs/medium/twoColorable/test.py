from twoColorable import twoColorable
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[1], [0]]
        expected = True
        actual = twoColorable(input)
        self.assertEqual(actual, expected)
    
    def test_case_2(self):
        input =   [
            [1, 2],
            [0, 2, 3],
            [0, 1, 3],
            [1, 2]
        ]
        expected = False
        actual = twoColorable(input)
        self.assertEqual(actual, expected)
    

    def test_case_3(self):
        input = [
            [1, 4],
            [0, 2, 3],
            [1, 3, 4],
            [1, 2],
            [0, 2]
        ]
        expected = False
        actual = twoColorable(input)
        self.assertEqual(actual, expected)
    
    def test_case_4(self):
        input = [[1], [0]]
        expected = True
        actual = twoColorable(input)
        self.assertEqual(actual, expected)

    
    









    
   