# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 20.06.2023


from typing import List


# Solution 1
# O(n^2 * n!) time | O(n * n!) space
def get_permutations(array: List[int]) -> List[int]:
    """ Return all permutations of the input array
    Args:
        param1(list): list of integers
    Return: list of all permutations
    """
    permutations = []
    permutations_helper(array, [], permutations)
    return permutations


def permutations_helper(
        array: List[int], current_permutation: List[int],
        permutations: List[int]):
    """ Helper function to get all permutations
    Args:
        param1(list): list of integers
        param2(list): current permutation
        param3(list): list of all permutations
    Return: list of all permutations
    """
    if not len(array) and len(current_permutation):
        # case array is empty  means the current permutation is complete
        permutations.append(current_permutation)
    else:
        for i in range(len(array)):
            new_array = array[:i] + array[i + 1:]
            # add the current ele to the cur perm
            new_permutation = current_permutation + [array[i]]
            # call the func again with the new array and the new permutation
            permutations_helper(new_array, new_permutation, permutations)
    return permutations


if __name__ == "__main__":
    array = [1, 2, 3]
    print(get_permutations(array))
