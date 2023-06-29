# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 29.06.2023


from typing import List


# O(n) time | O(n) space
def spiralTraverse(array: List[int]) -> List:
    """  traverse the array in spiral order


    Args:
        param1(list): list of integers
    Return: list of integers in spiral order
    """
    res = []
    # intialize the start and end row and col
    start_row, end_row = 0, len(array) - 1
    start_col, end_col = 0, len(array[0]) - 1
    while start_row <= end_row and start_col <= end_col:
        # traverse to the right until end_col
        for col in range(start_col, end_col + 1):
            res.append(array[start_row][col])
        # traverse down until end_row
        for row in range(start_row + 1, end_row + 1):
            res.append(array[row][end_col])
        # traverse left until start_col
        for col in reversed(range(start_col, end_col)):
            # edge case if there is a single row in the middle of the matrix
            if start_row == end_row:
                break
            res.append(array[end_row][col])
        for row in reversed(range(start_row + 1, end_row)):
            # edge case if there is a single column in the middle of the matrix
            if start_col == end_col:
                break
            res.append(array[row][start_col])
        # update the start and end row and col for the next iteration
        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1
    return res


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
    matrix = [
            [1,  2,  3,  4,  5],
            [16, 17, 18, 19,  6],
            [15, 24, 25, 20,  7],
            [14, 23, 22, 21,  8],
            [13, 12, 11, 10,  9]]
    spiralTraverse(array=matrix)
