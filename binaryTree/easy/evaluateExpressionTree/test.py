
# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 05.06.2023

from evaluateExpressionTree import evaluateExpressionTree, BinaryTree
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(-1)
        tree.left = BinaryTree(2)
        tree.right = BinaryTree(-2)
        tree.right.left = BinaryTree(5)
        tree.right.right = BinaryTree(1)
        expected = 6
        actual = evaluateExpressionTree(tree)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        tree = BinaryTree(-2)
        tree.left = BinaryTree(7)
        tree.right = BinaryTree(3)
        expected = 4
        actual = evaluateExpressionTree(tree)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        tree = BinaryTree(-4)
        tree.left = BinaryTree(3)
        tree.right = BinaryTree(2)
        expected = 6
        actual = evaluateExpressionTree(tree)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        tree = BinaryTree(-3)
        tree.left = BinaryTree(9)
        tree.right = BinaryTree(3)
        expected = 3
        actual = evaluateExpressionTree(tree)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        tree = BinaryTree(-1)
        tree.left = BinaryTree(-4)
        tree.left.left = BinaryTree(4)
        tree.left.right = BinaryTree(5)
        tree.right = BinaryTree(-2)
        tree.right.left = BinaryTree(10)
        tree.right.right = BinaryTree(3)
        expected = 27
        actual = evaluateExpressionTree(tree)
        self.assertEqual(actual, expected)
