# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 13.06.2023

from typing import List


# Solution 1
def minimumCharactersForWords(words: List[str]) -> List[str]:
    """  Compute the minimum characters for words
         and return the list of characters
         use a dictionary to store the characters and the count

    Args:
        param1(list): list of strings
    Return: list of characters

    """
    char_dict = dict()

    for w in words:
        w_dict = dict()
        for c in w:
            if c in w_dict:
                w_dict[c] += 1
            else:
                w_dict.update({c: 1})
        for k in w_dict:
            if k in char_dict:
                if w_dict[k] > char_dict[k]:
                    char_dict[k] = w_dict[k]
            else:
                char_dict.update({k: w_dict[k]})
    return [k for k, v in char_dict.items() for _ in range(v)]
