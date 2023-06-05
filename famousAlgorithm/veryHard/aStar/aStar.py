# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 05.06.2023

import math
import heapq
from typing import List

from utils import euklid_distance, check_bounds, addNeighbors


def aStarAlgorithm(
        startRow: int, startCol: int, endRow: int, endCol: int, graph: list) -> list:
    """ A* Algorithm a popular path finding algorithm uses a heuristic to find the
        shortest path from a start point to a end point. It is informed graph search
        algorithm by using a heuristic For pathes one could use the euklid distance
        between the current point and the end point. The algorithm uses a priority
        queue to store the points with the current distance and the euklid distance.
        If the heuristic is admissible and consistent (satisfies the triangle inequality)
        the algorithm is optimal. Definition admissible heuristic:
        A heuristic is admissible if it never overestimates the cost
        of reaching the goal, i.e. the cost it estimates to reach the goal
        is not higher than the lowest possible cost from the current point in the path
        It uses a g score and h score
        g score: current dist from the start point to the current point in the path
        h score: euklid distance from the current point to the end point
        f score: is the sum of g score and h score
    Args:
        param1(int): startRow
        param2(int): startCol
        param3(int): endRow
        param4(int): endCol
        param5(list): graph
    Return: list of path coordinates x,y points
    """
    # Write your code here.
    path = []
    g_score = 0
    h_score = euklid_distance(startRow, startCol, endRow, endCol)
    f_score = g_score + h_score
    move_rigth = [0, 1]
    move_left = [0, -1]
    move_up = [-1, 0]
    move_down = [1, 0]
    move_dir = [move_rigth, move_left, move_up, move_down]
    current_state = [startRow, startCol]
    visited = dict()
    visited.update({(startRow, startCol): round(f_score, 3)})
    # priority queue
    min_heap_explored_nodes = []
    # Add elements to the min heap
    heapq.heappush(min_heap_explored_nodes, [f_score, [startRow, startCol, g_score]])
    while len(min_heap_explored_nodes) > 0:
        current_f, current_state = heapq.heappop(min_heap_explored_nodes)
        # compute the neighbors of the current state
        visited, min_heap_explored_nodes = addNeighbors(cs=current_state, g_score=current_state[2], goal_state=[endRow, endCol], move_dir=move_dir, graph=graph, visited=visited, mhexplnodes=min_heap_explored_nodes)
        if (endRow, endCol) in visited:
            import pdb; pdb.set_trace()
        # get the point with the lowest f score
        # and remove it from the queue
        # explore the neighbors of the current point


            # check if the move is valid
    return []


if __name__ == "__main__":
    startRow = 0
    startCol = 1
    endRow = 4
    endCol = 3
    graph = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [1, 0, 1, 1, 1], [0, 0, 0, 0, 0]]
    aStarAlgorithm(startRow=startRow, startCol=startCol, endRow=endRow, endCol=endCol, graph=graph)
