# copyright 2024
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 04.02.2024

import logging
from typing import List

def water_area(heights: List[int]) -> int:
    """ """
    if len(heights) == 0:
        return 0
    tallest_left = [0] * len(heights)
    tallest_right = [0] * len(heights)
    tallest_left[0] = 0
    idx = 1
    while idx < len(heights):
        # importent show only the left side
        num = heights[idx-1]
        if num >= tallest_left[idx-1]:
            tallest_left[idx] = num
        else:
            tallest_left[idx] = tallest_left[idx-1]
        idx +=1
    logging.debug(f"tallest_left {tallest_left}")
    # compute the tallest right
    idx = len(heights) - 2
    tallest_right[-1] = 0
    while idx >= 0:
        num = heights[idx+1]
        if num >= tallest_right[idx+1]:
            tallest_right[idx] = num
        else:
            tallest_right[idx] = tallest_right[idx+1]
        idx -= 1
    
    logging.debug(f"tallest_left {tallest_left}")
    # compute the water area by taking the minimum of the tallest left and right
    # and subtracting the current height
    water_area = []
    for i in range(len(heights)):
        water_area.append(max(0, min(tallest_left[i], tallest_right[i]) - heights[i]))
    return sum(water_area)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
    # water_area [0,0,8,8,3,8,8,0,3,3,2,2,3,0]
    water_area(heights)
    # print(water_area(heights))