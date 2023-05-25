# copyright 2023
# author: Christian Leininger
# Email: leininic @ tf.uni-freiburg.d
# date: 24.05.2023


def isValidSubsequence(array, sequence):
    """ find if the sequence is in the array
        Iterate once through the array and
        check if the element is in the sequence
        remove the element from the sequence if found
        if the sequence is empty return True
        else return False
    Args:
        param1(list): array
        param2(list): sequence
    Return: bool
    """
    for num in array:
        if len(sequence) == 0:
            return True
        if num == sequence[0]:
            sequence.pop(0)
    if len(sequence) == 0:
        return True
    else:
        return False