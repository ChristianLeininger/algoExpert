# copyright 2023
# author: Christian Leininger
# Email: leininic @ tf.uni-freiburg.de
# date: 25.05.2023

from typing import List


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name: str):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array: List) -> List:
        """ Add the name of the node to the array
            and call the function recursively

        Args:
            param1(list): list of all nodes
        Return: list of all nodes in depth first search order
        """
        array.append(self.name)  # add the name of the node to the array
        for child in self.children:  # iterate over all children
            child.depthFirstSearch(array)  # call the function recursively
        return array
