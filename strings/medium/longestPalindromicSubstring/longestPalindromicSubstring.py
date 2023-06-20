# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 20.06.2023

from typing import List


# Navie solution
# O(n^3) time | O(n^2) space
def longestPalindromicSubstringNaive(string: str) -> str:
    """ Find the longest palindromic substring in the input string
        Naive solution create all substring and check if it is a palindrom
    Args:
        param1(str): input string
    Return:
        str: longest palindromic substring
    """
    sub_strings = generate_substrings(string)
    longest = ""
    for sub_string in sub_strings:
        if len(sub_string) > len(longest) and is_palindrom(sub_string):
            longest = sub_string
    return longest


def is_palindrom(s: str) -> bool:
    """ Check if the input string is a palindrom
    Args:
        param1(str): input string
    Return:
        bool: True if the string is a palindrom else False
    """
    left_idx = 0
    right_idx = len(s) - 1
    while left_idx < right_idx:
        if s[left_idx] != s[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1
    return True


def generate_substrings(s: str) -> List[str]:
    """ Generate all substrings of the input string

    Args:
        param1(str): input string
    Return:
        list: list of all substrings
    """
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings


# O(n^2) time | O(n) space
def longestPalindromicSubstring(string: str) -> str:
    """ Find the longest palindromic substring in the input string """

    current_range = [0, 1]
    for i in range(len(string)):
        odd = check_odd(string, i)
        even = check_even(string, i)
        if odd > even:

            new_range = [i - odd // 2, i + odd // 2 + 1]
            # import pdb; pdb.set_trace()
        else:
            new_range = [i - even // 2, i + even // 2]
            # print(f"solution {string[new_range[0]:new_range[1]]}" )
        if new_range[1] - new_range[0] > current_range[1] - current_range[0]:
            current_range = new_range
    return string[current_range[0]:current_range[1]]


def check_odd(string: str, idx: int) -> int:
    """ compute the longest palindrom with odd length
    Args:
        param1(str): input string
        param2(int): index of the string
    Return:
        int: length of the palindrom at idx
    """
    left_idx = idx - 1
    right_idx = idx + 1
    while left_idx >= 0 and right_idx < len(string):
        if string[left_idx] != string[right_idx]:
            break
        left_idx -= 1
        right_idx += 1
    return right_idx - left_idx - 1


def check_even(string: str, idx: int) -> int:
    """  check at position idx if the string is a palindrom with even length

    Args:
        param1(str): input string
        param2(int): index of the string
    Return: length of the palindrom at idx
    """
    left_idx = idx - 1
    right_idx = idx
    while left_idx >= 0 and right_idx < len(string):
        if string[left_idx] != string[right_idx]:
            break
        left_idx -= 1
        right_idx += 1
    return right_idx - left_idx - 1


if __name__ == '__main__':
    string = "abaxyzzyxf"
    longestPalindromicSubstring(string)
