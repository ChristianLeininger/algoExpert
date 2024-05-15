
# copyright 2024
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 15.05.2024

from diskStacking import diskStacking
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            diskStacking(
                [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [2, 2, 1], [4, 4, 5]]
            ),
            [[2, 1, 2], [3, 2, 3], [4, 4, 5]],
        )
    
    def test_case_2(self):
        disks = [
            [2, 1, 2],
            [3, 2, 3],
            [2, 2, 8],
            [2, 3, 4],
            [1, 3, 1],
            [4, 4, 5]
            ]
        sol = [
            [2, 1, 2],
            [3, 2, 3],
            [4, 4, 5]
            ]
        self.assertEqual(diskStacking(disks), sol)
    
    def test_case_3(self):
        disks = [
            [2, 1, 2],
            [3, 2, 3],
            [2, 2, 8],
            [2, 3, 4],
            [1, 3, 1],
            [4, 4, 5],
            [1, 1, 4]
            ]
        sol = [
            [1, 1, 4],
            [2, 2, 8]
            ]
        self.assertEqual(diskStacking(disks), sol) 

    def test_case_4(self):
        disks = [
            [2, 1, 2],
            [3, 2, 3],
            [2, 2, 8],
            [2, 3, 4],
            [1, 2, 1],
            [4, 4, 5],
            [1, 1, 4]
        ]
        sol = [
            [1, 1, 4],
            [2, 2, 8]
        ]
        self.assertEqual(diskStacking(disks), sol)