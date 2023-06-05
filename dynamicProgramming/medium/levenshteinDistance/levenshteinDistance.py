# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 05.06.2023


def create_array(n: int, m: int) -> list:
    """ uses the input of n and m to create a 2d array
        with n rows and m columns as a list of lists
        of size n x m with zero entries
    Args:
        param1(int): n
        param2(int): m
    Return: 2d array of size n x m
    """
    # Create an empty list
    array = []
    # Fill the first row with values 0, 1, 2, ..., n-1
    array.append(list(range(n)))
    # Fill the remaining rows
    for i in range(1, m):
        row = [0] * n
        row[0] = i
        array.append(row)
    return array


# iterative solution O(nm) time | O(nm) space
def levenshteinDistanceIterativ(word1: str, word2) -> int:
    """ Takes two words and calculate the minimum number
        of edit operations w.r. t. the levenshtein distance
        that computes the minimum number of edit operations
        that need to be performed on the first string to
        obtain the second string. Edit operations are
        insertion, deletion, or substitution of a single character.
    Args:
        param1(str): word1
        param2(str): word2
    Return: the minimum number of edit operations
    """
    distance_array = create_array(n=len(word1) + 1, m=len(word2) + 1)
    for r in range(1, len(distance_array)):
        for c in range(1, len(distance_array[0])):
            # compare the 2 letters
            if word1[c-1] == word2[r-1]:
                # case 2 letters are the same take the top left value
                distance_array[r][c] = distance_array[r-1][c-1]
            else:
                # compute the min over the top_left, left and top distance
                left = distance_array[r][c-1]

                top = distance_array[r-1][c]
                top_left = distance_array[r-1][c-1]
                distance_array[r][c] = min(left, top, top_left) + 1

    return distance_array[-1][-1]


# recursive solution O(nm) time | O(mim(n,m)) space
def levenshteinDistanceDynamicProgramming(word1: str, word2: str) -> int:
    """ Returns the minimum number of edit operations that need to be
        performed on the first string to obtain the second string.
        Edit operations are insertion, deletion, or substitution of
        a single character. Use the fact that only the current and
        previous row are needed to compute the next row.
        Disadvantage: can not be used to reconstruct the edit
        operations that were performed.

    Args:
        param1(str): word1
        param2(str): word2
    Return: the minimum number of edit operations
    """
    smaller = word1 if len(word1) < len(word2) else word2
    bigger = word1 if len(word1) >= len(word2) else word2
    even_edits = [x for x in range(len(smaller) + 1)]
    odd_edits = [None for x in range(len(smaller) + 1)]
    for i in range(1, len(bigger) + 1):
        if i % 2 == 1:
            # even row
            current_edits = odd_edits
            previous_edits = even_edits
        else:
            current_edits = even_edits
            previous_edits = odd_edits
        current_edits[0] = i  # first element in the row
        for j in range(1, len(smaller) + 1):
            if bigger[i - 1] == smaller[j - 1]:
                # case 2 letters are the same take the top left value
                current_edits[j] = previous_edits[j - 1]
            else:
                # min over the top_left, left and top distance add 1
                top_left = previous_edits[j - 1]
                top = previous_edits[j]
                left = current_edits[j - 1]
                current_edits[j] = 1 + min(top_left, top, left)
    # return the last element of the even or odd array
    return even_edits[-1] if len(bigger) % 2 == 0 else odd_edits[-1]
