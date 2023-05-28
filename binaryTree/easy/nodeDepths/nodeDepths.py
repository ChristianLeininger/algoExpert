# copyright 2023
# author: Christian Leininger
# Email: leininic @ tf.uni-freiburg.de
# date: 28.05.2023

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(h) space - where n is the number of nodes in the Binary Tree
# and h is the height of the Binary Tree
def nodeDepths(root):
    """ main function for calc the sum of all depth of the tree

    Args:
        param1 (object): root of the tree
    Return:
        sum of all depth of the tree
    """
    return helper(root, 0, [])


def helper(root, depth, depth_sum):
    """ helper function for calc the sum of all depth of the tree
        with recursion  and depth first search
    Args:
        param1 (object): root of the tree
        param2 (int): depth of the tree
        param3 (list): list of all depth of the tree
    Return:
        sum of all depth of the tree
    """

    if root is None:
        return depth_sum

    depth_sum.append(depth)
    helper(root.left, depth+1, depth_sum)
    helper(root.right, depth+1, depth_sum)
    return sum(depth_sum)
