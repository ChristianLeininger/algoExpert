# copyright 2024
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 03.02.2024


import unittest
from lineThroughPoints import lineThroughPoints


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        points = [
            [1, 1],
            [2, 2],
            [3, 3],
        ]
        self.assertEqual(lineThroughPoints(points), 3)
    
    def test_case_2(self):
        points = [
            [1, 1],
            [3, 2],
            [5, 3],
            [4, 1],
            [2, 3],
            [1, 4],
        ]
        self.assertEqual(lineThroughPoints(points), 4)
    
    def test_case_3(self):
        points = [
            [1, 1],
            [2, 2],
            [3, 3],
            [4, 4],
            [5, 5],
        ]
        self.assertEqual(lineThroughPoints(points), 5)