# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 20.06.2023


def oneEdit(stringOne: str, stringTwo: str) -> bool:
    """  Check if two strings are one edit away    """
    lenOne = len(stringOne)
    lenTwo = len(stringTwo)

    # case the length of both strings differ more than 1
    if abs(lenOne - lenTwo) > 1:
        return False

    # case both strings have the same length
    if lenOne == lenTwo:
        return checkSameLength(stringOne, stringTwo)
    # case one string is longer than the other
    edited = False
    index_stringOne = 0
    index_stringTwo = 0
    while index_stringOne < lenOne and index_stringTwo < lenTwo:
        if stringOne[index_stringOne] == stringTwo[index_stringTwo]:
            index_stringOne += 1
            index_stringTwo += 1
            continue
        if edited:
            return False
        edited = True
        # case delete one char in stringOne
        if lenOne > lenTwo:
            index_stringOne += 1
            continue
        # case delete one char in stringTwo
        if lenOne < lenTwo:
            index_stringTwo += 1
            continue
    # case one or edit
    return True


def checkSameLength(stringOne: str, stringTwo: str) -> bool:
    """  Check if two strings are one edit away
    Args:
        param1(str): stringOne
        param2(str): stringTwo
    Return: true if one edit away
    """
    count = 0
    for i in range(len(stringOne)):
        if stringOne[i] != stringTwo[i]:
            count += 1
    return count < 2
