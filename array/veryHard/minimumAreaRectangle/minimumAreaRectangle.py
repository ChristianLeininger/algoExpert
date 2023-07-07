# copyright 2023
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 06.07.2023


from typing import List
import logging


def minimumAreaRectangle(points: List[List[int]]) -> int:
    """ Given a list of x,y coordinates of points on a 2D plane,
    return the area of the smallest rectangle that can be formed
    from these points, with sides parallel to the x and y axes.
    If there is not any such rectangle, return 0.
    """
    logging.info("Start program")
    logging.info(f"Input {points}")
    # find all points that have the same x or y coordinate
    # create a dictionary with key x and value all y coordinates
    same_x, same_y = sort_coordinates(points)
    logging.info(f"Same x {same_x} same y {same_y}")
    return find_rectangle_min_area(same_x, same_y)


def find_rectangle_min_area(x_dict, y_dict):
    """ """
    min_area = float("inf")
    for x_list in x_dict.values():
        if len(x_list) < 2:
            continue
        for i in range(len(x_list)):
            for j in range(i + 1, len(x_list)):
                P1 = x_list[i]
                P3 = x_list[j]
                # p1 and p3 have the same x coordinate
                # now find two points with the same x coordinate
                # while in same time one needs to have the same y p1 or p3
                # P1 (x1|y1) P2 (x1|y2) P3 (x2|y1) P4 (x2|y2)
                y = [P1[1], P3[1]]
                y.sort()
                if y[0] in y_dict and y[1] in y_dict and len(y_dict[y[0]]) >= 2 and len(y_dict[y[1]]) >= 2:
                    y_dict[y[0]].sort()
                    y_dict[y[1]].sort()
                    for point in y_dict[y[0]]:
                        if point[0] == P1[0] or point[0] == P3[0]:
                            continue
                        P2 = [point[0], P1[1]]
                        for other_point in y_dict[y[1]]:
                            if other_point[0] == P2[0]:
                                P4 = [P2[0], P3[1]]
                                area = abs(P1[0] - P2[0]) * abs(P1[1] - P3[1])
                                if area < min_area:
                                    min_area = area
                                logging.info(f"Found rectangle {P1} {P2} {P3} {P4} -> {area}")
    if min_area == float("inf"):
        return 0
    return min_area


def sort_coordinates(coordinates: List[List[int]]):
    """ Sort the coordinates in a dictionary
      with key x and value all y coordinates
      also remove keys with only one value
    Args:
        param1(list): list of coordinates
    Return: two dictionaries with key x and value all y coordinates
    """
    x_dict = {}
    y_dict = {}

    for coordinate in coordinates:
        x, y = coordinate

        if x in x_dict:
            x_dict[x].append(coordinate)
        else:
            x_dict[x] = [coordinate]

        if y in y_dict:
            y_dict[y].append(coordinate)
        else:
            y_dict[y] = [coordinate]

    x_dict = remove_singletons(x_dict)
    y_dict = remove_singletons(y_dict)
    return x_dict, y_dict


def remove_singletons(d: dict) -> dict:
    """ Remove all keys with only one value
    Args:
        param1(dict): dictionary with key x and value all y coordinates
    Return: dictionary with key x and value all y co without singletons
    """
    for key in list(d.keys()):  # use list to create a copy of keys
        if len(d[key]) == 1:
            del d[key]
    return d


if __name__ == '__main__':
    logging.basicConfig(
            level=logging.DEBUG, format="%(levelname)s: %(message)s")

    points = [
            [1, 5], [5, 1], [4, 2], [2, 4],
            [2, 2], [1, 2], [4, 5], [2, 5], [-1, -2]]
    expected = 3
    actual = minimumAreaRectangle(points)
    logging.info(f"Expected {expected} Actual {actual}")
