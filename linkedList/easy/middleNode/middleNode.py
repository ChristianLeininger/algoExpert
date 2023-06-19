# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 18.06.2023


class LinkedList:
    def __init__(self, value: int):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def middleNodeNaive(linkedList: LinkedList) -> LinkedList:
    """ Return the middle node of the linked list
        naive approach with two passes
        first pass count the length of the linked list
        second pass return the middle node
    Args:
        param1: linkedList: LinkedList

    Return: LinkedList
    """
    length = 0
    element = linkedList
    while element is not None:
        length += 1
        element = element.next
    middle = length // 2
    element = linkedList
    count = 0
    while count < middle:
        count += 1
        element = element.next
    return element


def middleNode(linkedList: LinkedList) -> LinkedList:
    """ Use the idea of to pointer
        one pointer move two steps
        the other pointer move one step
        if the fast pointer is at the end the slow pointer is in the middle
    Args:
        param1: linkedList: LinkedList
    Return: middle node of the linked list
    """
    slow = linkedList
    fast = linkedList
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
