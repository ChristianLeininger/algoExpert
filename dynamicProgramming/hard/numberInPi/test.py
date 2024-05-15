# copyright 2024
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 15.05.2024

import unittest

from numberInPi import numbersInPi

PI = "3141592653589793238462643383279"


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        numbers = ["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]
        self.assertEqual(numbersInPi(PI, numbers), 2)
    
    def test_case_2(self):
        numbers = ["314159265358979323846264338327", "9"]
        self.assertEqual(numbersInPi(PI, numbers), 1)
    
    def test_case_3(self):
        numbers = ["3", "1", "4", "592", "65", "55"]
        self.assertEqual(numbersInPi(PI, numbers), -1)
    
    def test_case_4(self):
        numbers = ["3", "1", "4", "592", "65", "55", "35", "8", "9793", "23846264", "383279"]
        self.assertEqual(numbersInPi(PI, numbers), 11)
    
    def test_case_5(self):
        numbers = ["3", "141", "592", "65", "55", "35", "8", "9793", "23846264", "3832798"]
        self.assertEqual(numbersInPi(PI, numbers), -1)