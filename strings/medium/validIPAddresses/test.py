# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 26.06.2023


import unittest
from validIPAddresses import validIPAddresses


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = "1921680"
        expected = [
            "1.9.216.80",
            "1.92.16.80",
            "1.92.168.0",
            "19.2.16.80",
            "19.2.168.0",
            "19.21.6.80",
            "19.21.68.0",
            "19.216.8.0",
            "192.1.6.80",
            "192.1.68.0",
            "192.16.8.0",
        ]
        actual = validIPAddresses(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = "17216211"
        expected = ['1.7.216.211',
                    '1.72.16.211',
                    '1.72.162.11',
                    '17.2.16.211',
                    '17.2.162.11',
                    '17.21.6.211',
                    '17.21.62.11',
                    '17.216.2.11',
                    '17.216.21.1',
                    '172.1.6.211',
                    '172.1.62.11',
                    '172.16.2.11',
                    '172.16.21.1',
                    '172.162.1.1']
        actual = validIPAddresses(input)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        input = "88881234"
        expected = ['8.88.81.234',
                    '88.8.81.234',
                    '88.88.1.234',
                    '88.88.12.34',
                    '88.88.123.4']
        actual = validIPAddresses(input)
        self.assertEqual(actual, expected)

    def test_case_6(self):
        input = "00010"
        expected = ['0.0.0.10']
        actual = validIPAddresses(input)
        self.assertEqual(actual, expected)
