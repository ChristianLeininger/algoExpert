# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 09.06.2023


from typing import List


# time O(n)  | space O(1)
def isMonotonic(array: List) -> bool:
    """ compute if array is monotonic
        Check if the array is increasing or decreasing
        then loop through the array and check if the array
        is increasing or decreasing for the whole array
    Args:
        param1: array
    Return: True or False
    """
    if len(array) <= 2:
        return True
    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue
        if breaksDirection(direction, array[i - 1], array[i]):
            return False
    return True


def breaksDirection(direction: int, previous_int: int, current_int: int) -> bool:
    """ helper function to check if the direction is broken
    Args:
        param1(int): direction
        param2(int): previous int
        param3(int): current int
    Return: True or False
    """
    difference = current_int - previous_int
    if direction > 0:
        return difference < 0
    return difference > 0
