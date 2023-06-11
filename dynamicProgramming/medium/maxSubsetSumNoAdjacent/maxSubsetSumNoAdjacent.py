# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 09.06.2023


from typing import List


# time O(n) space O(1)
def maxSubsetSumNoAdjacent(array: List[int]) -> int:
    """ Return the max sum of non adjacent numbers
    Args:
        param1(list): list of numbers
    Return:
        int: max sum of non adjacent numbers
    """
    # egde case empty list
    for idx in range(2, len(array)):
        # if the new is bigger together with the sum 2 field earlier
        # take it  other wise the new sum is the sum one field earlier
        if array[idx] + array[idx - 2] >= array[idx - 1]:
            value = array[idx] + array[idx - 2]
        else:
            value = array[idx - 1]
        array[idx] = value
    return array[-1]
