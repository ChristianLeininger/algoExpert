# copyright 2023
# author: Christian Leininger
# Email: leininic @ tf.uni-freiburg.de
# date: 28.05.2023


from nthFib import getNthFib, getNthFibFast
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(getNthFib(6), 5)

    def test_case_2(self):
        self.assertEqual(getNthFibFast(6), 5)
