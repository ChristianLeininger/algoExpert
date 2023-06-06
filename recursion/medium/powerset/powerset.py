# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 05.06.2023

from typing import List


# O(n*2^n) time | O(n*2^n) space
def powerset(array: List) -> List[List[int]]:
    """ Return the powerset of the given array
        use recursion to calculate the powerset

    Args:
        param1(list): list of integers
    Return: list of all subsets
    """
    return create_powerset(array, 0, [[]])


def create_powerset(array: List, pointer: int, sol: List[List[int]]) -> List[List[int]]:
    """ Recursive function to calculate the powerset
        First add the current element to all subsets
        and then call the function recursively
    Args:
        param1(list): list of integers
        param2(int): pointer to the current element
        param3(list): list of all subsets
    Return: list of all subsets
    """
    if pointer >= len(array):
        return sol
    for idx in range(len(sol)):
        sol.append(sol[idx] + [array[pointer]])
    sol = create_powerset(array, pointer+1, sol)
    return sol
