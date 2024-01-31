# copyright 2024
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 30.01.2024




def numberOfWaysToTraverseGraph(rows: int , columns: int) -> int:
    """ Compute all ways to traverse a graph if the
        you can only move down or right use dynamic programming
        
    Args:
        param1:(int) rows
        param2:(int) columns
    Return: (int) number of ways to traverse the graph
    """
    array_2d = [[0 for _ in range(columns)] for _ in range(rows)]
    # intialize the first row and column to 1 that is the base case
    # Setting the first row to 1
    for i in range(columns):
        array_2d[0][i] = 1

    # Setting the first column to 1
    for j in range(1, rows):
        array_2d[j][0] = 1
    
    # realtionship between the current and the previous row and column
    # number of ways to get to the current position is the sum of the number of ways to get to the previous row and column
    for i in range(1, rows):
        for j in range(1, columns):
            array_2d[i][j] = array_2d[i-1][j] + array_2d[i][j-1]
    # last element is the number of ways to traverse the graph
    return array_2d[rows-1][columns-1]


if __name__ == "__main__":
    rows = 3
    columns = 4
    res = numberOfWaysToTraverseGraph(rows=rows, columns=columns)