# copyright 2024
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 15.05.2024

from typing import List, Dict, Tuple
import logging
from itertools import combinations



def numbersInPi(pi: str, numbers: List[str]) -> int:
    """
    Compute the minimum number of spaces needed to make all the numbers in the pi string
    Task we are given a string representation of the first n digits of pi 
    and a list of positive integers
    Now find the minmum number of spaces that need to be created in the pi string

    Args:
        pi : str : string representation of the first n digits of pi
        numbers : List[str] : list of positive integers
    Returns:
        int : minimum number of spaces needed to make all the numbers in the pi string 
    
    """
    numbersTable = {number: True for number in numbers}
    cache = {}
    minSpaces = getMinSpaces(pi, numbersTable, cache, 0)
    return minSpaces if minSpaces != float("inf") else -1

def getMinSpaces(pi: str, numbersTable: Dict[str, bool], cache: Dict[int, int], idx: int) -> int:
    """   Takes a prefix of the pi string and returns the minimum number of spaces 
    needed to make all the numbers in the pi string
    Args:
        pi : str : string representation of the first n digits of pi
        numbersTable : Dict[str, bool] : dictionary of numbers
        cache : Dict[int, int] : dictionary of minimum spaces needed for a prefix
        idx : int : index of the pi string
    Returns:
        int : minimum number of spaces needed to make all the numbers in the pi string
    """
    # if we are at the end of the pi string
    if idx == len(pi):
        return -1
    # if we already calculated the min space for this idx
    if idx in cache:
        return cache[idx]
    # get the min space for the idx
    minSpaces = float("inf")
    for i in range(idx, len(pi)):
        prefix = pi[idx:i + 1]
        if prefix in numbersTable:
            minSpacesInSuffix = getMinSpaces(pi, numbersTable, cache, i + 1)
            minSpaces = min(minSpaces, minSpacesInSuffix + 1)
    cache[idx] = minSpaces
    logging.debug(f"cache: {cache}")
    return cache[idx]

   


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    pi = "3141592"
    numbers = ["3141", "5", "31", "2", "4159", "9", "42"]
    print(numbersInPi(pi=pi, numbers=numbers))