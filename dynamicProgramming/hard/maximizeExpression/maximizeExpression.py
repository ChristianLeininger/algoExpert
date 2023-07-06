# copyright 2023
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 01.07.2023


from typing import List
import logging


# O(n^4) time | O(1) space
def maximizeExpressionNaive(array: List[int]) -> int:
    """ Find 4 index with the constraint i < j < k < m
    and return the maximum value of
    array[i] - array[j] + array[k] - array[m] re
    Brute force solution try all possible combinations
    Args:
        param1: array of integer
    Return: maximum value of array[i] - array[j] + array[k] - array[m]
    """
    logging.info("Start program")
    logging.info(f"Input {array}")
    # edge case array is to small
    if len(array) < 4:
        return 0
    # check all possible combinations
    # i < j < k < m
    max_value = float("-inf")
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            for k in range(j + 1, len(array)):
                for m in range(k + 1, len(array)):
                    value = array[i] - array[j] + array[k] - array[m]
                    max_value = max(max_value, value)
                    logging.info(f"i {i} j {j} k {k} m {m}")
                    logging.info(
                            f"array[i] {array[i]} array[j] {array[j]}"
                            f"array[k] {array[k]} array[m] {array[m]}"
                            f" = {max_value}"
                            )

    logging.info(f"max_value {max_value}")
    return max_value


def maximizeExpression(array: List[int]) -> int:
    """ DP solution """
    # edge case array is to small
    if len(array) < 4:
        return 0
    return 0


if __name__ == '__main__':
    logging.basicConfig(
            level=logging.DEBUG, format="%(levelname)s: %(message)s")
    array = [3, 6, 1, -3, 2, 7]
    maximizeExpressionNaive(array)
