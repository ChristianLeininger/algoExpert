# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 01.07.2023

from typing import List
import logging


# O(wh) time | O(wh) space
def minimumPassesOfMatrixNaive(matrix: List[List[int]]) -> int:
    """ Use a naive approach to solve the problem
        Iterate over the matrix and check if the entry is negative
        if yes check if the neighbors are positive
        if yes change the entry to positive

    Args:
        param1: matrix
    Return: int amount of passes to convert all negative entries to positive

    """
    adjacents = matrix_to_graph(matrix)
    max_iterate = len(matrix) * len(matrix[0])
    # create new matrix with same size only 0

    count = 0
    while True:
        only_positive = True
        count += 1
        new_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for key in adjacents.keys():
            # check if entry is positive
            if matrix[key[0]][key[1]] >= 0:
                new_matrix[key[0]][key[1]] = matrix[key[0]][key[1]]
                continue
            # check if neighbors are positive
            only_positive = False
            for node in adjacents[key]:
                # check neighbors of node
                if matrix[node[0]][node[1]] > 0:
                    new_matrix[key[0]][key[1]] = matrix[key[0]][key[1]] * -1

                    break
                else:
                    new_matrix[key[0]][key[1]] = matrix[key[0]][key[1]]
        matrix = new_matrix.copy()
        if count > max_iterate:
            return -1
        if only_positive:
            logging.debug(f"count {count} max_iterate {max_iterate} only_positive {only_positive}")
            return count - 1


def matrix_to_graph(matrix: List[List[int]]) -> dict:
    """ Convert the matrix to a graph  use
        the node as key and the neighbors as value
        The graph is going to represent with an adjacency list

    Args:
        param1: matrix

    Return: dict with node as key and neighbors as value
    """
    rows, cols = len(matrix), len(matrix[0])
    graph = {}
    for row in range(rows):
        for col in range(cols):
            node = (row, col)
            neighbors = []
            # check the node above
            if row > 0:
                neighbors.append((row - 1, col))
            # check the node below
            if row < rows - 1:
                neighbors.append((row + 1, col))
            # check the node to the left
            if col > 0:
                neighbors.append((row, col - 1))
            # check the node to the right
            if col < cols - 1:
                neighbors.append((row, col + 1))
            graph[node] = neighbors
    return graph


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    matrix = [
            [0, -1, -3, 2, 0],
            [1, -2, -5, -1, -3],
            [3, 0, 0, -4, -1],
            ]
    minimumPassesOfMatrixNaive(matrix)
