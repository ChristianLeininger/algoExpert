# copyright 2023
# author: Christian Leininger
# Email: leininic @ tf.uni-freiburg.de
# date: 28.05.2023

import unittest
from balancedBrackets import balancedBrackets


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(balancedBrackets("([])(){}(())()()"), True)

    def test_case_2(self):
        self.assertEqual(balancedBrackets("([])(){}())()()"), False)

    def test_case_3(self):
        self.assertEqual(
                balancedBrackets("([])fsfs(){fdfdf}((fdfsf))()"), True)
