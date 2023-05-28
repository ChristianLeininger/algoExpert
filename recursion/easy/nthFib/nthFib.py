# copyright 2023
# author: Christian Leininger
# Email: leininic @ tf.uni-freiburg.de
# date: 28.05.2023

from typing import Dict


# O(2^n) time | O(n) space
def getNthFib(n: int) -> int:
    """ Compute the nth Fibonacci number use a recusion
        this is a naive solution with a time complexity of O(2^n)
        Args:
            param1(int): integer
        Return: the nth Fibonacci number

    """
    if n == 1:
        return 0
    if n == 2:
        return 1
    return getNthFib(n-1) + getNthFib(n-2)


# O(n) time | O(n) space
def getNthFibFast(n: int) -> int:
    """ Compute the nth Fibonacci number use a recusion
        and use a dictionary to save all previous calculated Fibonacci numbers
        new time complexity is O(n) and space complexity is O(n)
    Args:
        param1(int): integer

    Return: the nth Fibonacci number
    """
    return helper(n-1, {})


def helper(n: int, memory: Dict) -> int:
    """ helper function to compute the nth Fibonacci number

    Args:
        param1(int): integer
        param2(dict): dictionary to save all previous cal Fibonacci numbers
    Return: the nth Fibonacci number
    """
    if n == 0:
        memory.update({n: 0})
        return 0
    if n == 1:
        memory.update({n: 1})
        return 1
    if n in memory:
        return memory[n]
    if n-1 in memory and n-2 in memory:
        memory.update({n: memory[n-1] + memory[n-2]})
    return helper(n-1, memory) + helper(n-2, memory)
