# copyright 2024
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 04.02.2024

from waterArea import water_area
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
        self.assertEqual(water_area(heights), 48)
    
    def test_case_2(self):
        heights = [0, 1, 0, 1, 0, 2, 0, 3, 0, 2, 0, 1, 0, 1]
        self.assertEqual(water_area(heights), 8)

    def test_case_3(self):
        heights = [0, 1, 0, 1, 0, 2, 0, 3, 0, 2, 0, 1, 0, 2]
        self.assertEqual(water_area(heights), 11)
    
    def test_case_4(self):
        heights = []
        self.assertEqual(water_area(heights), 0)
    
    def test_case_5(self):
        heights = [10, 10, 10, 10, 10]
        self.assertEqual(water_area(heights), 0)
    
    def test_case_6(self):
        heights = [10, 0, 10, 0, 10]
        self.assertEqual(water_area(heights), 20)
    
    def test_case_7(self):
        heights = [10, 0, 10, 0, 10, 0, 10, 0, 10]
        self.assertEqual(water_area(heights), 40)
    
    def test_case_8(self):
        heights = [10, 0, 10, 0, 5, 0, 10, 0, 15, 0, 10]
        self.assertEqual(water_area(heights), 55)