# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 29.05.2023


from typing import List


def partition(array: List, left: int, right: int) -> List:
    """ Partition the array into two parts
        left part all elements smaller then pivo
        right part all elements bigger then pivo

    Args:
        param1(list): array of integers
        param2(int): left index
        param3(int): right index
    Return: array, index of pivo element
    """
    pivot = array[left]
    low = left + 1
    high = right
    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer,
        # since that indicates we have already moved all the elements
        # to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1
        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1
        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break
    # swap the pivo element with value from right pointer
    array[left], array[high] = array[high], array[left]

    return array, high


def recusion(array: List, left: int, right: int) -> List:
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

    if left >= right:
        return array

    # call recusion for left part
    array, pivot_idx = partition(array=array, left=left, right=right)
    array = recusion(array, left=left, right=pivot_idx - 1)
    # call recusion for right part
    array = recusion(array, left=pivot_idx + 1, right=right)
    return array


# O(nlog(n)) time | O(1) space
def quickSort(array: List) -> List:
    """ Compute the quicksort algorithm in place
        use divide and conquer to sort the array
    Args:
        param1(list): array of integers
    Return: sorted array
    """
    # edge case array is empty or has only one element
    if len(array) < 2:
        return array
    return recusion(array, left=0, right=len(array) - 1)


if __name__ == "__main__":
    array = [8, 5, 2, 9, 5, 6, 3]
    array = [8, 5, 2, 1]
    array = [3, -1, 4, 1, -5, 9, 2, -6, 5, 3, -5]
    array = array = [8, 5, 2]
    print(quickSort(array))
