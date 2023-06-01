# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 01.06.2023

from typing import List


# O(log(n)) time | O(1) space
def binarySearch(array: List, target: int) -> int:
    """  Find the index of the target value in a sorted array
         Use the fact that the array is sorted and use binary search
         to find the target value in O(log(n)) time. If not found return -1
    Args:
        param1(list): list of integers
        param2(int): target value
    Return: index of the target value
    """
    lp = 0
    rp = len(array) - 1

    while lp <= rp:
        pointer = (rp - lp) // 2 + lp
        if target == array[pointer]:
            return pointer
        if target > array[pointer]:
            # target needs to be in the upper half
            lp = pointer + 1
        else:
            # target needs to be in lower half
            rp = pointer - 1
    return -1
