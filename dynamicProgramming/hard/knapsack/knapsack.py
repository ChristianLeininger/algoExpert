# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 20.06.2023


from typing import List


# O(nc) time | O(nc) space
def knapsackProblem(items: List[List[int]], capacity: int) -> List:
    """ Calculate the maximum value of items
    that can be contained in the knapsack
    first element of the list is the value of the item
    second element of the list is the weight of the item
    Use dynamic programming to solve the problem
    first use 1 item then 2 items and so on
    the value of the knapsack is the max of the previous value
    or the current value + the value of the remaining space

    Args:
        param1(list): list of items with value and weight
        param2(int): capacity of the knapsack
    Return: list of maximum value and list of indices of items
    """
    # init the knapsack with 0
    knapsack_values = [
            [0 for _ in range(0, capacity + 1)]
            for _ in range(0, len(items) + 1)]
    # go through all items
    for i in range(1, len(items) + 1):
        current_weight = items[i - 1][1]
        current_value = items[i - 1][0]
        # go through all capacity
        for c in range(0, capacity + 1):
            # case not enough space
            if current_weight > c:
                knapsack_values[i][c] = knapsack_values[i - 1][c]
            else:
                # case enough space take the max of the previous value
                # or the current value + the value of the remaining space
                not_taking_current = knapsack_values[i - 1][c]
                # the case taking the current item
                # the new weight need to be subtracted from the capacity
                # the value of the current item need 
                # to be added to the previ value
                taking_current = knapsack_values[i - 1][c - current_weight] + current_value
                knapsack_values[i][c] = max(not_taking_current, taking_current)
    # import pdb; pdb.set_trace()
    return [knapsack_values[-1][-1], get_indices(knapsack_values, items)]


def get_indices(knapsack_values: List[List[int]], items: List[List[int]]) -> List[int]:
    """ Get the indices of the items that are in the knapsack

    Args:
        param1(list): list of items with value and weight
        param2(list): list of the knapsack items
    Return: list of indices of taken items
    """
    sequence = []
    i = len(knapsack_values) - 1
    c = len(knapsack_values[0]) - 1
    while i > 0:
        # if the value is the same as the value of the previous item
        # the item is not in the knapsack
        if knapsack_values[i][c] == knapsack_values[i - 1][c]:
            i -= 1
        else:
            # the item is in the knapsack
            # add the index to the sequence
            sequence.append(i - 1)
            # subtract the weight of the item from the capacity
            c -= items[i - 1][1]
            i -= 1
        # if the capacity is 0 the knapsack is full
        if c == 0:
            break
    return list(reversed(sequence))
