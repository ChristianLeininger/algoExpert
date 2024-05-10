from longest_common_subsequenz import longest_common_sub_sequenz_naive
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = longest_common_sub_sequenz_naive("ZXVVYZW", "XKYKZPW")
        self.assertEqual(output, ["X", "Y", "Z", "W"])
    
    def test_no_common_subsequence(self):
        output = longest_common_sub_sequenz_naive("ABC", "DEF")
        self.assertEqual(output, [])

    def test_one_empty_string(self):
        output = longest_common_sub_sequenz_naive("", "ABC")
        self.assertEqual(output, [])

    def test_both_empty_strings(self):
        output = longest_common_sub_sequenz_naive("", "")
        self.assertEqual(output, [])

    def test_same_strings(self):
        output = longest_common_sub_sequenz_naive("ABC", "ABC")
        self.assertEqual(output, ["A", "B", "C"])

    def test_one_character_common(self):
        output = longest_common_sub_sequenz_naive("A", "BAC")
        self.assertEqual(output, ["A"])

    def test_repeated_characters(self):
        output = longest_common_sub_sequenz_naive("AAB", "ABA")
        self.assertEqual(output, ["A", "A"])
    