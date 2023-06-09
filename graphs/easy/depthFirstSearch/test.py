# copyright 2023
# author: Christian Leininger
# Email: leininic @ tf.uni-freiburg.de
# date: 25.05.2023

from depthFirstSearch import Node
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        graph = Node("A")
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[2].addChild("G").addChild("H")
        graph.children[0].children[1].addChild("I").addChild("J")
        graph.children[2].children[0].addChild("K")
        self.assertEqual(
                graph.depthFirstSearch([]),
                ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"])
