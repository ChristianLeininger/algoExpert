# copyright 2023
# author: Christian Leininger
# Email: leininic @ tf.uni-freiburg.d
# date: 25.05.2023


# average: O(log(n)) time | O(1) space
# worst: O(n) time | O(1) space
def findClosestValueInBstIterative(tree, target):
    """ Find the closest value in binary search tree
        Proberty of binary search tree:
        left node is smaller than parent node
        right node is bigger than parent node
        Traverse the tree and update the closest value
        in an iterative way
    Args:
        param1(BST): tree
        param2(int): target value
    Return:
        int: closest value to target
    """
    current_node = tree
    closest_value = current_node.value
    while True:
        if abs(closest_value-target) >= abs(current_node.value-target):
            closest_value = current_node.value
        if current_node.value == target:
            break
        if current_node.value > target:
            # go left
            if current_node.left is None:
                break
            current_node = current_node.left
        else:
            if current_node.right is None:
                break
            current_node = current_node.right
    return closest_value


# average: O(log(n)) time | O(log(n)) space
# worst: O(n) time | O(n) space
def findClosestValueInBstRecursive(tree, target):
    """ Find the closest value in binary search tree
        Proberty of binary search tree:
        left node is smaller than parent node
        right node is bigger than parent node
        Traverse the tree and update the closest value
        in an recursive way
    Args:
        param1(BST): tree
        param2(int): target value
    Return:
        int: closest value to target
    """
    return findClosestValueInBstHelper(tree, target, tree.value)


def findClosestValueInBstHelper(tree, target, closest):
    """ Helper function for findClosestValueInBstRecursive

    Args:
        param1(BST): tree
        param2(int): target value
        param3(int): closest value
    Return:
        int: closest value to target
    """
    if tree is None:
        return closest
    if abs(closest-target) >= abs(tree.value-target):
        closest = tree.value
    if tree.value > target:
        return findClosestValueInBstHelper(tree.left, target, closest)
    if tree.value < target:
        return findClosestValueInBstHelper(tree.right, target, closest)
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
