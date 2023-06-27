# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 20.06.2023

# O(n) time | O(1) space
def oneEdit(stringOne: str, stringTwo: str) -> bool:
    """  check if two strings are one edit away    
    
    
    Args:   
        param1(str): first string
        param2(str): second string
    Return: bool true if one edit away else false
    """
    lenOne = len(stringOne)
    lenTwo = len(stringTwo)
    # if one string is longer than the other
    # by more than one character, they can't
    # be one edit away from each other
    if abs(lenOne - lenTwo) > 1:
        return False
    
    for idx in range(min(lenOne, lenTwo)):
        if stringOne[idx] != stringTwo[idx]:
            # to chars are different 
            # means the rest needs to be the same
            # if strings have the same length
            if lenOne == lenTwo:
                # check if the rest of the strings are the same
                return stringOne[idx + 1:] == stringTwo[idx + 1:]
            # if the first string is longer than the second
            elif lenOne > lenTwo:
                # check if the rest of the first string is the same as the second
                return stringOne[idx + 1:] == stringTwo[idx:]
            # if the second string is longer than the first
            else:
                # check if the rest of the second string is the same as the first
                return stringOne[idx:] == stringTwo[idx + 1:]
    
    # all characters are the same
    return True

if __name__ == "__main__":
    stringOne = "a"
    stringTwo = "ba"
    print(oneEdit(stringOne, stringTwo))