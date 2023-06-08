# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 09.06.2023


from typing import List


# O(n^2) time | O(1) space
def ZeroSumSubarrayNaive(array: List[int]) -> bool:
    """  check if there is a subarray with sum 0
        if  a subarray with sum 0 exists return True else False
        use a naive approach with two loops of the array of length n
        and try all possible combinations
    Args:
        param1: array

    Return: bool
    """

    for i in range(len(array)):
        current_sum = 0
        for j in range(i, len(array)):
            current_sum += array[j]
            if current_sum == 0:
                return True
    return False


# O(n) time | O(n) space
def zeroSumSubarray(array: List[int]) -> bool:
    """ create an aray with the sum of all subarrays
        use a hash table to store the sum of the subarray
        if the sum is already in the hash table return True else False
        or if the sum is 0 return True
    Args:
        param1: array
    Return: bool
    """
    hash_table = {}
    current_sum = 0
    for i in range(len(array)):
        current_sum += array[i]
        if current_sum == 0:
            return True
        if current_sum in hash_table:
            return True
        hash_table[current_sum] = True
    return False
