# copyright 2023
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 01.07.2023

from typing import List, Tuple
import logging


def sweetAndSavory(dishes: List[int], target: int) -> List[int]:
    """  There are dishes represented by integers in the array dishes.
         A negative integer denotes a sweet dish,
         and a positive integer denotes a savory dish.
         Not too savory means it needs to be less than target.
         Return the dishes that are closest to target.
         If there is no dish that is not too savory, return [0, 0]
    Args:
        param1(list): list of integers
        param2(int): target value
    Return: list of integers
    """

    # idea seperate the array in two parts
    # one with negative values and one with positive values
    savorty_dishes, sweet_dishes = separate_and_sort(lst=dishes)

    logging.debug(f"savorty_dishes {savorty_dishes} sweet_dishes {sweet_dishes}")
    # edge case if one of the list is empty
    if len(savorty_dishes) == 0 or len(sweet_dishes) == 0:
        return [0, 0]

    # edge case the smallest savorty dish is bigger than the target

    sweet_p = 0
    savorty_p = len(savorty_dishes) - 1
    # init the dish combination with the first element of each list
    if savorty_dishes[savorty_p] + sweet_dishes[sweet_p] == target:
        return [sweet_dishes[sweet_p], savorty_dishes[savorty_p]]
    best_diff = float("inf")
    dish_combination = [0, 0]
    logging.debug(f"init {dish_combination}")
    # compare the values of the two lists
    while sweet_p < len(sweet_dishes) and savorty_p >= 0:
        logging.debug(f"----------------------------------------------------")
        current_sweet = sweet_dishes[sweet_p]
        current_savorty = savorty_dishes[savorty_p]
        dish = current_sweet + current_savorty
        logging.debug(f"current_sweet {current_sweet} current_savorty {current_savorty}")
        logging.debug(f"dish {dish}")
        # check if its too savorty
        if dish > target:
            savorty_p -= 1
            continue
        if dish == target:
            return [current_sweet, current_savorty]
        logging.debug(f"dish_combination {dish_combination}")
        logging.debug(f" abs(dish - target) {abs(dish - target)} abs(sum(dish_combination) - target) {abs(sum(dish_combination) - target)}")
        if abs(dish - target) < best_diff:
            best_diff = abs(dish - target)
            dish_combination = [current_sweet, current_savorty]
        # if the sum is to high move the savorty pointer to the left
        if current_sweet + current_savorty > target:
            savorty_p -= 1
        # if the sum is to low move the sweet pointer to the right
        elif current_sweet + current_savorty < target:
            sweet_p += 1
    logging.debug(f"dish_combination {dish_combination}")
    return dish_combination


def separate_and_sort(lst: List[int]) -> Tuple[List[int], List[int]]:
    """ seperate the list in two parts

    Args:
        param1(list): list of integers
    Return: 2 list one with negative values and one with positive values
    """
    positive_list = []
    negative_list = []

    for x in lst:
        if x > 0:
            positive_list.append(x)
        elif x < 0:
            negative_list.append(x)

    return sorted(positive_list), sorted(negative_list)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    dishes = [-3, -5, 1, 7]
    target = 8
    dishes = [5, -5, 5, -5, 5, -5]
    target = 5
    dishes = [5, -10]
    target = -4
    dishes = [-3, -5, 1, 7]
    target = 0
    sweetAndSavory(dishes=dishes, target=target)
