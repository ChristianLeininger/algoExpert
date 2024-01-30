# copyright 2024
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 30.01.2024


import unittest
from numberOfWaysToTraverseGraph import numberOfWaysToTraverseGraph


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        rows  = 3
        columns = 4
        expcted = 10
        self.assertEqual(numberOfWaysToTraverseGraph(rows, columns), expcted)
    
    def test_case_2(self):
        rows  = 2
        columns = 2
        expcted = 2
        self.assertEqual(numberOfWaysToTraverseGraph(rows, columns), expcted)
    
    def test_case_3(self):
        rows  = 4
        columns = 3
        expcted = 10
        self.assertEqual(numberOfWaysToTraverseGraph(rows, columns), expcted)
    
    def test_case_4(self):
        rows  = 4
        columns = 4
        expcted = 20
        self.assertEqual(numberOfWaysToTraverseGraph(rows, columns), expcted)
    
    def test_case_5(self):
        rows  = 5
        columns = 5
        expcted = 70
        self.assertEqual(numberOfWaysToTraverseGraph(rows, columns), expcted)