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
    return


if __name__ == '__main__':
    string = "abaxyzzyxf"
    longestPalindromicSubstring(string)
