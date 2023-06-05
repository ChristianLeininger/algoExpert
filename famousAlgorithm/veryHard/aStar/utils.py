# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 05.06.2023


import math
import heapq
from typing import List


def euklid_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    """ calculate the euklid distance between two points
    Args:
        param1(int): x1
        param2(int): y1
        param3(int): x2
        param4(int): y2
    Return: int
    """
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def check_bounds(row: int, col: int, graph: list) -> bool:
    """  check if the row and col are in the bounds of the graph

    Args:
        param1(int): row
        param2(int): col
        param3(list): graph
    Return: bool
    """
    return row >= 0 and row < len(graph) and col >= 0 and col < len(graph[0])


def addNeighbors(
        cs: List, move_dir: List, g_score: int, goal_state: List, graph: List, visited: dict, mhexplnodes: heapq) -> list:
    """  compute the neighbors of the current state and add them to the neighbors list
         if they are in the bounds of the graph and not free to walk
    Args:
        param1(list): current_state
        param2(list): neighbors
        param3(list): graph
        param4(heapq): visited
    Return: list of visited nodes and the min heap
    """
    for move in move_dir:
        ns = [cs[0] + move[0], cs[1] + move[1]]
        if check_bounds(row=ns[0], col=ns[1], graph=graph) and graph[ns[0]][ns[1]] != 1 and (ns[0], ns[1]) not in visited:
            h_score = euklid_distance(x1=ns[0], y1=ns[1], x2=goal_state[0], y2=goal_state[1])
            new_g_score = g_score + 1
            f_score = new_g_score + h_score
            visited.update({(ns[0], ns[1]): [new_g_score, round(f_score, 3)]})
            heapq.heappush(mhexplnodes, [f_score, [ns[0], ns[1], new_g_score]])
    # import pdb; pdb.set_trace()
    return visited, mhexplnodes
