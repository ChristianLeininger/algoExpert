# copyright 2024
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 20.05.2024

from getYoungestCommonAncestor import getYoungestCommonAncestor, AncestralTree
import unittest


class AncestralTree(AncestralTree):
    def addDescendants(self, *descendants):
        for descendant in descendants:
            descendant.ancestor = self


def new_trees():
    ancestralTrees = {}
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        ancestralTrees[letter] = AncestralTree(letter)
    return ancestralTrees


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"])
        trees["B"].addDescendants(trees["D"], trees["E"])
        trees["D"].addDescendants(trees["H"], trees["I"])
        trees["C"].addDescendants(trees["F"], trees["G"])

        yca = getYoungestCommonAncestor(trees["A"], trees["E"], trees["I"])
        self.assertTrue(yca == trees["B"])