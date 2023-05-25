# copyright 2023
# author: Christian Leininger
# Email: leininic @ tf.uni-freiburg.de
# date: 25.05.2023


# O(nlogn) time | O(1) space
def nonConstructibleChange(coins):
    """ computes the minimum amount of change that you cannot create
    given a list of coins
    First sort the coins in ascending order then iterate over the coins
    there are two cases if the current coin is greater than the change + 1
    then return change + 1
    else add the current coin to the change
    we use the change variable to keep track of the minimum amount of change
    and we use the coin variable to iterate over the coins
    Args:
        param1: list of coins
    Return: minimum amount of change that you cannot create
    """
    change = 1
    coins.sort()
    for coin in coins:
        if coin > change:
            return change
        change += coin
