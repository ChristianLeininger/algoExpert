# copyright 2024
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 03.02.2024

from typing import List
import logging

def lineThroughPoints(points: List[List[int]]):
    """ """
    # compute slope and intercept for each pair of points
    # and store it in a dictionary
    slope_intercept = {}
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 == x2:
                slope = float('inf')
                intercept = x1
            else:
                slope = (y2 - y1) / (x2 - x1)
                intercept = y1 - slope * x1
            if (slope, intercept) in slope_intercept:
                continue
            else:
                slope_intercept[(slope, intercept)] = [(points[i], points[j])]
    # find the slope and intercept with the most points
    line_points = []
    logging.info(slope_intercept)
    # find the slope and intercept with the most points
    # check for each slope and intercept how many points are on the line
    for line in slope_intercept:
        points_on_line = 0
        for point in points:
            x = point[0]
            y = point[1]
            # edge case: if the slope is infinity
            if line[0] == float('inf'):
                if x == line[1]:
                    points_on_line += 1
                continue
            if y == line[0] * x + line[1]:
                points_on_line += 1
        line_points.append(points_on_line)
    max_points = max(line_points)
    return max_points









if __name__ == '__main__':
    points = [
        [1, 1],
        [2, 2],
        [3, 3],
        [0, 4],
        [-2, 6],
        [4, 0],
        [2, 1]
        ]
    
    points = [
        [1, 1],
        [1, 2],
        [1, 3],
        [1, 4],
        [1, 5],
        [2, 1],
        [2, 2],
        [2, 3],
        [2, 4],
        [2, 5],
        [3, 1],
        [3, 2],
        [3, 4],
        [3, 5],
        [4, 1],
        [4, 2],
        [4, 3],
        [4, 4],
        [4, 5],
        [5, 1],
        [5, 2],
        [5, 3],
        [5, 4],
        [5, 5],
        [6, 6],
        [2, 6]
        ]
    logging.basicConfig(level=logging.DEBUG)
    print(lineThroughPoints(points))