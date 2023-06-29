# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 05.06.2023


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree: BinaryTree) -> int:
    """ Given a binary tree with operators and values
        values are positive and operators are negative
        values are only leaf nodes are operators are only internal nodes
        evaluate the tree and return the result
        Use a recursive approach
    Args:
        param1(BinaryTree): tree
    Return: result of the tree
    """
    # check if leaf node
    if tree.value >= 0:
        # both are leaf nodes
        return tree.value

    left_value = evaluateExpressionTree(tree=tree.left)
    right_value = evaluateExpressionTree(tree=tree.right)
    # import pdb; pdb.set_trace()
    return evaluate_operator(value1=left_value, value2=right_value, operator=tree.value)


def evaluate_operator(value1: int, value2: int, operator: int) -> int:
    """  evaluate the operator given
    two values and the operator

    Args:
        param1(int): value1
        param2(int): value2
        param3(int): operator
    Return: result of the operator
    """
    if operator == -1:
        return value1 + value2
    elif operator == -2:
        return value1 - value2
    elif operator == -3:
        return int(value1 / value2)
    elif operator == -4:
        return value1 * value2
    else:
        return None


if __name__ == '__main__':
    tree = BinaryTree(-1)
    tree.right = BinaryTree(-3)
    tree.right.left = BinaryTree(8)
    tree.right.right = BinaryTree(3)
    tree.left = BinaryTree(-2)
    tree.left.right = BinaryTree(2)
    tree.left.left = BinaryTree(-4)
    tree.left.left.right = BinaryTree(3)
    tree.left.left.left = BinaryTree(2)
    evaluateExpressionTree(tree=tree)   # expected = 6
