# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 01.06.2023

from typing import List


# naive solution O(n^2) time | O(n) space
def arrayOfProductsNaive(array: List) -> List:
    """  straight forward solution needs two loops
         to compute the product of all other numbers in the array
    Args:
        param1(list): list of integers
    Return: list of integers

    """
    products = [1 for _ in array]
    for i in range(len(array)):
        runningProduct = 1
        for j in range(len(array)):
            if i != j:
                runningProduct *= array[j]
        products[i] = runningProduct
    return products


# O(n) time | O(n) space
def arrayOfProducts(array: List) -> List:
    """ Computes the product of all other numbers in the array
        Use the fact that the product of all other numbers is
        equal to the product of all numbers to the left multiplied
        by the product of all numbers to the right. Loop through
        the array twice, once from left to right and once from right to left.
        see pdf explaition
    Args:
        param1(list): list of integers
    Return: list of integers
    """
    sol = [1 for i in array]
    runningProduct = 1
    for i in range(len(array)):
        sol[i] = runningProduct
        runningProduct *= array[i]
    runningProduct = 1
    for i in reversed(range(len(array))):
        sol[i] *= runningProduct
        runningProduct *= array[i]
    return sol
