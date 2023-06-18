# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 18.06.2023


class LinkedList:
    def __init__(self, value: int):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def removeDuplicatesFromLinkedList(linkedList: LinkedList) -> LinkedList:
    """ Remove duplicates from linked list
        Idea: 1. iterate over the linked list
        While the next element is not None
        2. check if the current value is greater or equal to the next value
        3. if yes, delete the next value by setting
        the next pointer to the next next pointer
    Args:
        param1: linkedList: LinkedList
    Return: LinkedList
    """

    element = linkedList
    # iterate over the linked list
    while element.next is not None:
        if element.value >= element.next.value:
            element.next = element.next.next
        else:
            element = element.next
    # return the linked list without duplicates
    return linkedList
