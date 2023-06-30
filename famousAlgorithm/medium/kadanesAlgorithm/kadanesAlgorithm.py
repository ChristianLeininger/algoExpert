# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 29.06.2023

from typing import List


# O(n) time | O(n) space
def kadanesAlgorithmNaive(array: List[int]) -> int:
    """ Use a naive approach to solve the problem
        by using a array to store the max value at each index
        and update the max value at each index
        return the max value of the array
    Args:
        param1: (List[int]) array of integers
    Return: (int) max value of the array

    """
    sol = [None] * len(array)
    for i in range(len(array)):
        if i == 0:
            sol[i] = array[i]
        else:
            sol[i] = max(sol[i-1] + array[i], array[i])
    return max(sol)


def kadanesAlgorithm(array: List[int]) -> int:
    """ Idea is not to store the max value at each index
        but to use 2 variables to store the max value at each index
        and update the max value at each index

    Args:
        param1: (List[int]) array of integers
    Return: (int) max value of the array
    """

    maxEndingHere = array[0]
    maxSoFar = array[0]
    # loop over the array and update the max value at each index
    for i in range(1, len(array)):
        num = array[i]
        # decide to take the currrent value or start a new subarray
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar


if __name__ == "__main__":
    kadanesAlgorithmNaive(
            [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4])
