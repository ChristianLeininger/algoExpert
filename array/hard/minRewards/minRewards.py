# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 01.07.2023

from typing import List
import logging


# ______________________________________________________________________________
# O(n) time | O(n) space
def minRewards(array: List[int]) -> int:
    """ Calculate the min Rewards of a given array
        it represents the score of a game rules are
        if the number is higher than the left and right neighbor
        the reward is 1 higher than the left and right neighbor
        every number has to have at least one reward
    Args:
        param1: (List[int]) array of integers
    Return: (int) min Rewards
    """

    # need to give every number at least one reward
    soluntion = [1 for _ in range(len(array))]
    # first loop from left to right
    for i in range(1, len(array)):
        # check if current number is higher than the left neighbor
        if array[i] > array[i - 1]:
            soluntion[i] = soluntion[i - 1] + 1
    # second loop from right to left
    logging.debug(f"soluntion {soluntion}")
    for i in reversed(range(len(array) - 1)):
        # check if the number is higher than the right neighbor
        if array[i] > array[i + 1]:
            # case current reward is higher than the right neighbor
            # it is check if the current reward is higher than the right neighbor + 1
            soluntion[i] = max(soluntion[i], soluntion[i + 1] + 1)
    logging.debug(f"soluntion {soluntion}")
    # import pdb; pdb.set_trace()
    return sum(soluntion)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    print(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]))
