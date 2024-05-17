

def zigzagTraverse(array):
    """ Input is a 2D array. Output is a 1D array of all elements in the 2D array in zigzag order.
    
    Args:
        array: 2D array of integers.
    Returns:
        1D array of integers.
    """
    # Initialize variables to keep track of the current row, column, and direction.
    row = 0
    col = 0
    goingDown = True
    result = []
    height = len(array) - 1
    width = len(array[0]) - 1
    # Loop through the 2D array until we reach the end.
    while not isOutOfBounds(row, col, height, width):
        result.append(array[row][col])
        # If we are going down, we need to check if we are at the bottom or the right edge.
        if goingDown:
            if col == 0 or row == height:
                # reached the left edge or the bottom need to go up
                goingDown = False
                # If hit the bottom, move to the right. Otherwise, move down.
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                # move diagonally down
                row += 1
                col -= 1
        else:
            # modus going up now
            # check if we hit the top or the right edge
            if row == 0 or col == width:
                goingDown = True
                if col == width:
                    # case where we hit the right edge
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return result


def isOutOfBounds(row, col, height, width):
    """ Helper function to check if the current row and column are out of bounds.
    
    Args:
        row: Integer.
        col: Integer.
        height: Integer.
        width: Integer.
    Returns:
        Boolean.
    """
    return row < 0 or row > height or col < 0 or col > width

if __name__ == '__main__':
    test = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
    print(zigzagTraverse(test))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]