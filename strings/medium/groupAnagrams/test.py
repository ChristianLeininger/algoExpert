# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 12.06.2023


import unittest
from groupAnagrams import groupAnagrams


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
        expected = [
                ["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
        output = list(map(lambda x: sorted(x), groupAnagrams(words)))
        self.compare(expected, output)

    def compare(self, expected, output):
        if len(expected) == 0:
            self.assertEqual(output, expected)
            return
        self.assertEqual(len(expected), len(output))
        for group in expected:
            self.assertTrue(sorted(group) in output)
