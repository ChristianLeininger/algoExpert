# copyright 2024
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 03.02.2024


import logging



def minNumberOfJumps(array: list) -> int:
    """ Returns the minimum number of 
        jumps to reach the end of the array
    Args:
        param1: (list) array
    Returns:
        int: number of jumps
    """
    # edge case if array has only one element
    if len(array) == 1:
        return 0
    # intialize jumps, maxReach and steps
    jumps = 0
    maxReach = array[0]  # represents the maximum index that can be reached
    steps = array[0]   # represents the number of steps that can still be taken
    # each element in the array represents the maximum number 
    # of steps that can be taken from that position
    for i in range(1, len(array) - 1):
        # only update maxReach if you can reach further than before
        maxReach = max(maxReach, i + array[i])
        steps -= 1  # we use a step to get to the current index
        if steps == 0:
            # now we need to take a jump
            jumps += 1
            steps = maxReach - i # steps from the current index to the max idnex
            logging.info(f" need to jump at {i} and steps {steps} maxReach {maxReach}")
    logging.info(f"Result {jumps + 1}")
    return jumps + 1



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
    expected = 4
    result = minNumberOfJumps(array)