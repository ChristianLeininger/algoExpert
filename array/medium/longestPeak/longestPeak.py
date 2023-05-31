# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 30.05.2023


from typing import List


# O(n) time | O(1) space
def longestPeak(array: List) -> int:
    """ compute the longest peak in the array
        which is defined as adjacent integers in the array
        that are strictly increasing until they reach a tip
        the tip is the highest value in the peak
        and adjacent integers in the array that are strictly decreasing
    Args:
        param1(list): list of integers
    Return: length of the longest peak
    """

    array = [float("inf")] + array + [float("inf")]
    longest_peak = 0
    for idx in range(1, len(array)):
        c_peak = 1
        mp = idx
        lp = idx - 1
        rp = idx + 1
        left, right = False, False
        while True:
            if lp >= 0 and array[mp] > array[lp]:
                c_peak += 1
                mp = lp
                lp -= 1
                left = True
            else:
                break
        # go right until peak ends
        mp = idx
        while True:
            if rp <= len(array) - 1 and array[rp] < array[mp]:
                c_peak += 1
                mp = rp
                rp += 1
                right = True
            else:
                break
        if c_peak > longest_peak and left and right:
            longest_peak = c_peak
    return longest_peak
