# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 29.05.2023


from typing import List


def pivo_sort(array: List, left: int, right: int, pivo_idx: int) -> List:
    """ use the  pivo element to sort the array
        move all elements smaller then pivo to the left
        and all elements bigger to the right
    Args:
        param1(list): array of integers
        param2(int): index of the pivo element
    Return: half sorted array with pivo element at the right position
    """
    lp = left
    rp = right
    pivot = array[pivo_idx]
    # swap pivo elemtent at first
    array[lp], array[pivo_idx] = array[pivo_idx], array[lp]
    lp += 1
    # now swap all elements smaller then pivo to the left
    # all elements bigger to the right
    while True:
        # find element bigger then pivo from left
        # and smaller from right then swap
        # print(f"left {lp} right {rp} array {array}")
        while lp < right and array[lp] < pivot:
            # left needs to point to element bigger then pivo
            lp += 1
        # now lp points to element bigger then pivo

        while rp > left and array[rp] >= pivot:

            rp -= 1
            print(f"decrease right {rp} -> {array[rp]} is {pivot}")
        if lp >= rp:
            # swap pivo element back to the right position
            # case if pivo element is bigger then elemet at rp
            if pivot > array[rp]:
                array[left], array[rp] = array[rp], array[left]
                return array
            array[left], array[rp - 1] = array[rp - 1], array[left]
            return array

        array[lp], array[rp] = array[rp], array[lp]


def quick_sort(array: List, left: int, right: int) -> List:
    """ Use the quick_sort algorithm to sort the array
        first divide the array into two parts
        left part all elements smaller then pivo
        right part all elements bigger then pivo
        then sort the two parts
        The most left element is the pivo element
        move all elements smaller then pivo to the left
        and all elements bigger to the right

    Args:
        param1(list): array of integers

    Return: sorted array
    """

    if len(array) <= 1:
        return array
    pivo_idx = 0
    array = pivo_sort(array, left=left, right=right, pivo_idx=pivo_idx)
    print(f" pivot {array[pivo_idx]} to the right position {array}")


if __name__ == "__main__":
    array = [8, 5, 2, 9, 5, 6, 3]
    array = [8, 5, 2, 1]
    array = [3, -1, 4, 1, -5, 9, 2, -6, 5, 3, -5]
    array = array = [8, 5, 2]
    print(quick_sort(array, left=0, right=len(array) - 1))
