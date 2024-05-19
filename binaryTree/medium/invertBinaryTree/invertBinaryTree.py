# copyright 2024
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 20.05.2024



def invertBinaryTree(tree):
    """ Invert a binary tree
        Using a recursive function to invert a binary tree
        Idee swap the left and right child then call the function recursively on the left and right child
        until the child is None
    Args:
        param1: (BinaryTree) tree 
    """
    if tree is None:
        return
    tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    return tree



def invertBinaryTreeIterative(tree):
    """ invert a binary tree
        Using a iterative function to invert a binary tree
        Use a queue to store the nodes that need to be inverted

    Args:
        param1: (BinaryTree) tree

    """
    # create a queue with the root node
    queue = [tree] 
    # while the queue is not empty
    while len(queue) > 0:
        current = queue.pop(0)
        if current is None:
            continue
        current.left, current.right = current.right, current.left
        queue.append(current.left)
        queue.append(current.right)
    return tree









