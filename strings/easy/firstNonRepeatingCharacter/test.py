# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 30.05.2023

import unittest
from firstNonRepeatingCharacter import firstNonRepeatingCharacter


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = "abcdcaf"
        expected = 1
        actual = firstNonRepeatingCharacter(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = "bcddcaabff"
        expected = -1
        actual = firstNonRepeatingCharacter(input)
        self.assertEqual(actual, expected)
