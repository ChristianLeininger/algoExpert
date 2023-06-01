# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 30.05.2023


def firstNonRepeatingCharacter(string: str) -> int:
    """ Find index of first non repeating character
        Use dictionary index to find the character in the string

    Args:
        param1: (str) string to check
    Return:
        (int) index of first non repeating character
    """
    char_dict = {}
    for idx, i in enumerate(string):
        if i not in char_dict:
            char_dict.update({i: [idx, 1]})
        else:
            char_dict[i][1] += 1
    for value in char_dict.values():
        if value[1] == 1:
            return value[0]
    return -1
