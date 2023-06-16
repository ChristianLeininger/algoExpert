# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 16.06.2023


from typing import List


def searchForRange(array: List, target: int) -> List:
    """ O(log(n)) time | O(1) space

    Args:
        param1(list): array
        param2(int): target
    Return list of start and end index of target
    """
    start = 0
    end = len(array) - 1
    while start <= end:
        idx = (start + end) // 2
        if array[idx] == target:
            start = idx
            end = idx
            while start > 0 and array[start - 1] == target:
                start -= 1
            while end < len(array) - 1 and array[end + 1] == target:
                end += 1
            return [start, end]
        elif array[idx] < target:
            # go right
            start = idx + 1
        else:
            # go left
            end = idx - 1
    return [-1, -1]


if __name__ == '__main__':
    searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45)
