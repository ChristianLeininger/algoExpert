# copyright 2023
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 01.07.2023

from typing import List
import logging


def largestRangeNaive(array: List[int]) -> List[int]:
    """ get the longest range in the array

    Args:
        param1: array to check
    Return the array with the longest range
    """

    sortedArray = sorted(set(array))
    longestRange = []
    currentRange = [sortedArray[0]]
    logging.debug(f"sortedArray {sortedArray}")
    for i in range(1, len(sortedArray)):
        if sortedArray[i-1] + 1 == sortedArray[i]:
            logging.debug(f"currentRange {currentRange} append {sortedArray[i]}")
            currentRange.append(sortedArray[i])
        else:
            if len(currentRange) > len(longestRange):
                longestRange = currentRange
                logging.debug(f"longestRange {longestRange}")
            currentRange = [sortedArray[i]]
    logging.debug(f"currentRange {currentRange} longestRange {longestRange}")
    if len(currentRange) > len(longestRange):
        longestRange = currentRange
        logging.debug(f"longestRange {longestRange}")
    return [longestRange[0], longestRange[-1]]


# O(n) time | O(n) space
def largestRange(array: List[int]) -> List[int]:
    """ get the longest range in the array
    Idea: use a hash table to store the numbers
    and a boolean to check if the number is already visited

    Args:
        param1: array to check
    Return the start and end of the longest range
    """
    bestRange = []
    longestLength = 0
    nums = {}
    for num in array:
        nums[num] = True
    logging.debug(f"nums {nums}")
    for num in array:
        # explore the number only if it is not already visited
        if not nums[num]:
            logging.debug(f"continue {num}")
            continue
        # use a boolean to check if the number is already visited
        nums[num] = False
        currentLength = 1
        left = num - 1
        right = num + 1
        # go left as long as the number is in the array
        while left in nums:
            nums[left] = False
            currentLength += 1
            left -= 1
        # go right as long as the number is in the array
        while right in nums:
            nums[right] = False
            currentLength += 1
            right += 1
        # check if the current length is the longest
        if currentLength > longestLength:
            longestLength = currentLength

            bestRange = [left + 1, right - 1]
    return bestRange


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    array = [-7, -7, -7, -7, 8, -8, 0, 9, 19, -1, -3, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, -6, 8, 7, 6, 15, 12, 12, -5, 2, 1, 6, 13, 14, -4, -2]
    array = [8, 4, 2, 10, 3, 6, 7, 9, 1]
    # largestRange(array)
    largestRangeNaive(array)
