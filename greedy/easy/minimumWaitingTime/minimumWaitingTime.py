# copyright 2023
# author: Christian Leininger
# Email: leininic @ tf.uni-freiburg.de
# date: 25.05.2023

from typing import List


def minimumWaitingTime(queries: List) -> int:
    """ Calculate the minimum waiting time for all queries
        First sort the queries and then calculate the time
        to wait for each query
    Args:
        param1(list): list of integers
    Return: the minimum waiting time
    """
    time_to_wait = 0
    total_time = 0
    queries.sort()
    for query in queries[:-1]:
        time_to_wait = time_to_wait + query
        total_time += time_to_wait
    return total_time
