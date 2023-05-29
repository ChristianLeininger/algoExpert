# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 29.05.2023

from typing import List


# O(n^2) time | O(n) space
def threeNumberSum(array: List, targetSum: int):
    """ Find all triplets that sum up to targetSum
        use a 2 inner loops and a outer loop
        sort the elements in the array and
        sort the triplets in descending order
        Args:
            param1(list): list of integers
            param2(int): target sum
        Return: list of triplets
    """
    sol = []
    end = len(array)
    for idx in range(end):
        rest = targetSum - array[idx]
        for i in range(idx+1, end):
            for j in range(i+1, end):
                if array[i] + array[j] == rest:
                    sol.append(sorted([array[idx], array[i], array[j]]))
    return sorted(sol)
