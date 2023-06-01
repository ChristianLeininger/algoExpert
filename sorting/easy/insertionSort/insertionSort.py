# copyright 2023
# author: Christian Leininger
# Email: leininic @ tf.uni-freiburg.de
# date: 28.05.2023

from typing import List


# run time O(n^2) and space O(1)
def insertionSort(array: List) -> List:
    """ use the insertion sort algo
    It sorts the array in place with run time O(n^2) and space O(1)
    It keeps the left side of the array sorted and insert the elment
    at the right position until the array is sorted
    Args:
        param1(array): array of integers
    Return:
        sorted array
    """
    # edge case array with one element or empty
    if len(array) <= 1:
        return array
    unp = 1   # unsorted position
    while True:
        for sorted_pos in range(0, unp):
            if array[sorted_pos] > array[unp]:
                # move element to the right position
                array = move_element(array=array, pos1=sorted_pos,  pos2=unp)
                break
        unp += 1
        if unp == len(array):
            # array is sorted
            return array


def move_element(array: List, pos1: int, pos2: int) -> List:
    """ helper function to move element from pos2 to pos1
    Args:
        param1(array): array of integers
        param2(int): position of element to move
        param3(int): position to move to
    Return:
        array with moved element
    """
    item = array.pop(pos2)
    return array[:pos1] + [item] + array[pos1:]
