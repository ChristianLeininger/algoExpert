# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 01.07.2023

from typing import List
import logging


# O(n) time | O(1) space
def subarraySort(array: List[int]) -> List[int]:
    """  Find start and end index of subarray that needs to be sorted

    Args:
        param1: array to be sorted
    Return the start and end index of subarray that needs to be sorted
    """
    # first find the smallest and largest number out of order
    # in a single loop over the array
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")
    for i in range(1, len(array)):
        num = array[i]
        # if left number is bigger than right number
        if num < array[i - 1]:
            if minOutOfOrder > num:
                minOutOfOrder = num
            if maxOutOfOrder < array[i - 1]:
                maxOutOfOrder = array[i - 1]
    logging.debug(f"minOutOfOrder {minOutOfOrder} maxOutOfOrder {maxOutOfOrder}")
    # if array is already sorted
    if minOutOfOrder == float("inf"):
        return [-1, -1]
    # find the correct position of minOutOfOrder and maxOutOfOrder
    # find min position go from left to right
    subarrayLeftIdx = 0
    for idx in range(len(array)):
        if minOutOfOrder < array[idx]:
            subarrayLeftIdx = idx
            break
    # find max position go from right to left
    subarrayRightIdx = len(array) - 1
    for idx in reversed(range(len(array))):
        if maxOutOfOrder > array[idx]:
            subarrayRightIdx = idx
            break
    logging.debug(f"subarrayLeftIdx {subarrayLeftIdx} subarrayRightIdx {subarrayRightIdx}")
    return [subarrayLeftIdx, subarrayRightIdx]


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    out = subarraySort(array)
