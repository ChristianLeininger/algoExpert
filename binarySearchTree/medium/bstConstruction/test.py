# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 13.06.2023

import unittest
from bstConstruction import BST


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)

        root.insert(12)
        self.assertTrue(root.right.left.left.value == 12)
        self.assertTrue(root.contains(15))
        # root.remove(10)
        # self.assertTrue(not root.contains(10))