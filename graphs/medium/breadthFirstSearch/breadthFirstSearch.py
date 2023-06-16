# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 16.06.2023

from typing import List
import queue


class Node:
    def __init__(self, name: str):
        """ Init Class with name and empty list of children
        Args:
            param1(str): name of the node
        """
        self.children = []
        self.name = name

    def addChild(self, name: str) -> object:
        """ Add a child to the node
        Args:
            param1(str): name of the child
        """
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array: List) -> List[str]:
        """ O(v + e) time | O(v) space
        where v is the number of vertices of
        the input graph and e is the number
        of edges of the input graph

        Args:
            param1(list): array
        Return list of all nodes in the tree in breadth-first order
        """
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)

        return array


if __name__ == '__main__':
    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")
    graph.breadthFirstSearch([])
