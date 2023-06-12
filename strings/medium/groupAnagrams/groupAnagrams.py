# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 12.06.2023


from typing import List


# O(w * n * log(n)) time | O(wn) space
def groupAnagrams(words: List[str]) -> List[List[str]]:
    """ Group Anagrams from a list of words
        Idea is to sort each word and check if the
        sorted word is in the dict if not add it to
        the dict with the sorted word as key and
        the word as value if yes add the word
        to the list of the value of the dict
    Args:
        param1(list): list of words
    Return: list of list of anagrams
    """
    word_dict = {}
    for w in words:
        w2 = ''.join(sorted(w))
        if w2 not in word_dict:
            word_dict.update({w2: [w]})
        else:
            word_dict[w2].append(w)
    return list(word_dict.values())
