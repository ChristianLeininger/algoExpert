
from dijkstra import dijkstrasAlgorithm

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        start = 0
        edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
        expected = [0, 7, 13, 27, 10, -1]
        actual = dijkstrasAlgorithm(start, edges)
        self.assertEqual(actual, expected)
    
    def test_case_2(self):
        start = 4
        edges = [
                [
                [1, 3],
                [2, 2]
                ],
                [
                [3, 7]
                ],
                [
                [1, 2],
                [3, 4],
                [4, 1]
                ],
                [],
                [
                [0, 2],
                [1, 8],
                [3, 1]
                ]
                ]
        expected =[2, 5, 4, 1, 0]
        actual = dijkstrasAlgorithm(start, edges)
        self.assertEqual(actual, expected)
    
    def test_case_3(self):
        start = 7
        edges = [
                [
                [1, 1],
                [3, 1]
                ],
                [
                [2, 1]
                ],
                [
                [6, 1]
                ],
                [
                [1, 3],
                [2, 4],
                [4, 2],
                [5, 3],
                [6, 5]
                ],
                [
                [5, 1]
                ],
                [
                [4, 1]
                ],
                [
                [5, 2]
                ],
                [
                [0, 7]
                ]
            ]
        expected = [7, 8, 9, 8, 10, 11, 10, 0]
        actual = dijkstrasAlgorithm(start, edges)
        self.assertEqual(actual, expected)






