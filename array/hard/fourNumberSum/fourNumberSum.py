# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 01.07.2023

from typing import List
import logging


def fourNumberSum(array: List[int], targetSum: int) -> List[List[int]]:
    """ Find all quadruplets that sum up to the target sum


    Args:
        param1: (List[int]) array of integers
        param2: (int) target sum
    Return List[List[int]]: List of all quadruplets that sum up to the target sum
    """

    array.sort()
    solution = []
    # loop over  elements in the array
    for i in range(len(array) - 3):
        # loop over the rest of the array
        for j in range(i + 1, len(array) - 2):
            # set left and right pointer
            left = j + 1
            right = len(array) - 1
            while left < right:
                currentSum = array[i] + array[j] + array[left] + array[right]
                if currentSum == targetSum:
                    solution.append([array[i], array[j], array[left], array[right]])
                    left += 1
                    right -= 1
                elif currentSum < targetSum:
                    left += 1
                elif currentSum > targetSum:
                    right -= 1

    logging.info(f"Solution {solution}")
    return solution


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    array = [7, 6, 4, -1, 1, 2]
    targetSum = 16
    logging.info(f"Input array {array} targetSum {targetSum}")
    fourNumberSum(array=array, targetSum=targetSum)
