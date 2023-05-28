# copyright 2023
# author: Christian Leininger
# Email: leininic @ tf.uni-freiburg.de
# date: 28.05.2023
from typing import List


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(BinaryTree):
    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


def branchSums(root: BinaryTree) -> List:
    """ Calculate the branch sum of a binary tree
    Args:
        param1 (object): root of the tree
    Return:
        list of all branch sum
    """
    return depthFirstSearch(root, 0, [])


# O(n) time | O(n) space - where n is the number of nodes in the Binary Tree
def depthFirstSearch(tree: BinaryTree, summe: int, save_numbers: List) -> List:
    """ Calculate the branch sum of a binary tree

    Args:
        param1 (object): root of the tree
        param2 (int): sum of the branch
        param3 (list): list of all branch sum
    Return:
        list of all branch sum
    """
    if tree is None:
        return
    summe += tree.value
    if tree.left is None and tree.right is None:
        save_numbers.append(summe)
    depthFirstSearch(tree.left, summe, save_numbers)
    # print(f"v {tree.value}, {summe}")
    depthFirstSearch(tree.right, summe, save_numbers)
    return save_numbers
