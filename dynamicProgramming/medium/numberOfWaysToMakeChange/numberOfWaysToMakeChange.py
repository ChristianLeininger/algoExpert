# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 30.05.2023

from typing import List


# O(nd) time | O(n) space
def numberOfWaysToMakeChange(n: int, denoms: List) -> int:
    """ use dynamic programming to solve the problem of
    number of ways to make change
    First create a array with n+1 entries
    and fill it with 0 entries and the first entry is 1
    Iterate over the denoms and check if the denom is smaller than the
    current value in the array. If this is the case add the value of the
    array at the position value - denom to the current value in the array
    The array has size n + 1 and run time is O(nd) where n is the target value
    and d is the number of denoms
    Args:
        param1:(int) n
        param2:(list) denoms
    Return: (int) number of ways to make change
    """
    # edge case n = 0
    if n == 0:
        return 1
    # create array with n+1 entries
    possible_changes = [1] + [0 for _ in range(n)]

    for d in denoms:
        # start at the current denom
        for v in range(d, n + 1):
            possible_changes[v] += possible_changes[v - d]
    return possible_changes[-1]
