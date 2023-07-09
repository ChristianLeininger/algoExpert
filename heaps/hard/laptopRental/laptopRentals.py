# copyright 2023
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 06.07.2023

from typing import List, Dict, Tuple
import logging


def laptopRentalsNaive(times: List[List[int]]) -> int:
    """ Return the number of laptops needed

    Args:
        param1: times: List[List[int]]
    Return: int laptop needed

    """
    logging.info(f"Times {times}")
    times.sort(key=lambda x: x[0])
    logging.info(f"Times {times}")
    usedLaptops = []
    for time in times:
        logging.info(f"Time {time} usedLaptops {usedLaptops}")
        laptopUsed = False
        for idx, laptop in enumerate(usedLaptops):
            if laptop[1] <= time[0]:
                usedLaptops[idx] = time
                laptopUsed = True
                break
        if not laptopUsed:
            usedLaptops.append(time)
    logging.info(f"UsedLaptops {usedLaptops}")
    return len(usedLaptops)


def laptopRentals(times: List[List[int]]) -> int:
    """ Return the number of laptops needed

    Args:
        param1: times: List[List[int]]
    Return: int laptop needed

    """
    if len(times) == 0:
        return 0
    startTimes = sorted([time[0] for time in times])
    endTimes = sorted([time[1] for time in times])
    usedLaptops = 0
    startIterator = 0
    endIterator = 0

    while startIterator < len(times):
        if startTimes[startIterator] >= endTimes[endIterator]:
            logging.info(
                    f"startTimes[startIterator] {startTimes[startIterator]}"
                    f"endTimes[endIterator] {endTimes[endIterator]}")
            usedLaptops -= 1
            endIterator += 1
        usedLaptops += 1
        startIterator += 1
        logging.info(
                f"usedLaptops {usedLaptops} startIterator "
                f"{startIterator} endIterator {endIterator}")
    return usedLaptops


if __name__ == '__main__':
    logging.basicConfig(
            level=logging.DEBUG, format="%(levelname)s: %(message)s")
    times = [[0, 2], [1, 4], [4, 6], [0, 4], [7, 8], [9, 11], [3, 10]]
    expected = 3
    actual = laptopRentalsNaive(times)
    actual = laptopRentals(times)
