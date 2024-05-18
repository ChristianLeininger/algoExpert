# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 01.07.2023

from typing import List
import logging
import math


def knightConnection(knightA: List[int], knightB: List[int]) -> int:
    """ solving the problems of the 2 knights  
        How many move does it take knightA and knightB so that they are on the same field
        First Idea only one knight needs to move to the other knight needs
        Second Idea: see it as a graph problem


    """
    logging.info(f"KnightA: {knightA} KnightB: {knightB}")
    # check if the knights are on the same field no move is needed
    if knightA == knightB:
        return 0
    # possible moves of a knight
    actions = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    # use BSF to find the shortest path
    queue = [[knightA, 0]]   # position of knight and the number of moves
    visited = dict({tuple(knightA) : True}) # keep track of visited positions to avoid cycles
    # BFS loop until queue is empty or knightB is found
    while queue:
        current, moves = queue.pop(0)
        for move in actions:
            new_pos = [current[0] + move[0], current[1] + move[1]]
            if new_pos == knightB:
                return math.ceil((moves + 1) / 2)
            if tuple(new_pos) not in visited:
                visited.update({tuple(new_pos): True})
                queue.append([new_pos, moves + 1])
                

    return - 1



if __name__ == "__main__":
    knightA = [0, 0]
    knightB = [4, 2]
    expected = 1
    actual = knightConnection(knightA, knightB)
    print(actual)