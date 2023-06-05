# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 05.06.2023


from levenshteinDistance import levenshteinDistanceIterativ
from levenshteinDistance import levenshteinDistanceDynamicProgramming
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(levenshteinDistanceIterativ("abc", "yabd"), 2)

    def test_case_2(self):
        self.assertEqual(
                levenshteinDistanceDynamicProgramming("abc", "yabd"), 2)
