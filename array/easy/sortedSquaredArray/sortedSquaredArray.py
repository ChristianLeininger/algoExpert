# copyright 2023
# author: Christian Leininger
# Email: leininic @ tf.uni-freiburg.d
# date: 24.05.2023

# -----------------------------------------------------------------------------
# time O(nlog(n)) | space O(n)
def sortedSquaredArrayNaive(array):

    res = []
    for num in array:
        res.append(num**2)
    res.sort()
    return res


# -----------------------------------------------------------------------------
# time O(n) | space O(n)
def sortedSquaredArray(array):
    """ assume that the array is sorted
    edge case: negative numbers
    use two pointer left and right left
        to find the smaller and bigger number of the array
        to avoid sorting the array
    Args:
        param1(list): array of numbers

    """

    left_pointer = 0
    right_pointer = len(array) - 1
    res = []
    # move the pointers until they cross each other
    while left_pointer <= right_pointer:
        if abs(array[left_pointer]) > abs(array[right_pointer]):
            # case 1: left is bigger than right
            # add the square of the left to
            res.insert(0, array[left_pointer]**2)
            left_pointer += 1
        else:
            # case 2: right is bigger than left
            res.insert(0, array[right_pointer]**2)
            right_pointer -= 1

    return res
