# copyright 2023
# author: Christian Leininger
# Email: leininic @ tf.uni-freiburg.de
# date: 25.05.2023

import unittest
from optimalFreelancing import optimalFreelancing



class TestProgram(unittest.TestCase):
    def test_case_1(self):
        jobs= [
            {
                "deadline": 2,
                "payment": 1
            },
            {
                "deadline": 2,
                "payment": 2
            },
            {
            "deadline": 2,
            "payment": 3
            },
            {
            "deadline": 2,
            "payment": 4
            },
            {
            "deadline": 2,
            "payment": 5
            },
            {
            "deadline": 2,
            "payment": 6
            },
            {
            "deadline": 2,
            "payment": 7
            }
        ]
        actual = optimalFreelancing(jobs)
        expected = 8
        self.assertEqual(actual, expected)
    def test_case_2(self):
        jobs =  [
            {
            "deadline": 2,
            "payment": 2
            },
            {
            "deadline": 4,
            "payment": 3
            },
            {
            "deadline": 5,
            "payment": 1
            },
            {
            "deadline": 7,
            "payment": 2
            },
            {
            "deadline": 3,
            "payment": 1
            },
            {
            "deadline": 3,
            "payment": 2
            },
            {
            "deadline": 1,
            "payment": 3
            }
        ]
        actual = optimalFreelancing(jobs)
        expected = 8
        self.assertEqual(actual, expected)

