# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 12.06.2023


from typing import List, Tuple


# O(n^2) time | O(2^n) space
def maxSumIncreasingSubsequenceNaive(
        array: List[int]) -> Tuple[int, List[int]]:
    """ Calculate the maximum sum of increasing subsequence
        Naive solution create all possible increasing subsequence in
        O(2^n) time and then calculate the sum of each subsequence
        use only the strictly increasing subsequence and return the sum
        of the maximum subsequence and the subsequence
    Args:
        param1(list): list of integers
    Return: list of  target sum and the increasing subsequence
    """
    # edge case of negative numbers
    if sum(array) < 0:
        return [-1, [-1]]
    current_max = [0, []]
    sol = generate_subsets(array)
    for sub in sol:
        if not is_strictly_increasing(sub):
            continue
        totalsum = sum(sub)
        if totalsum > current_max[0]:
            current_max = [totalsum, sub]
    return current_max


def is_strictly_increasing(lst: List[int]) -> bool:
    """ Check if the list is strictly increasing
    Args:
        param1(list): list of integers
    Return: bool
    """
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            return False
    return True


def generate_subsets(lst: List[int]) -> List[List[int]]:
    """ Generate all subsets of the given list
        Recursive solution
    Args:
        param1(list): list of integers
    Return: list of all subsets
    """
    subsets = []

    def backtrack(start, subset):
        subsets.append(subset[:])
        for i in range(start, len(lst)):
            subset.append(lst[i])
            backtrack(i + 1, subset)
            subset.pop()
    backtrack(0, [])
    return subsets


def maxSumIncreasingSubsequence(array: List[int]) -> Tuple[int, List[int]]:
    """ """

    pass
