# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 01.07.2023


from typing import List


def validStartingCity(distances: List[int], fuel: List[int], mpg: int) -> int:
    """ Use a greedy approach to solve the problem
        Assumption: there is always a valid starting city
        and there is acactly enought fuel to travel to all cities
    Args:
        param1(list): distances between cities
        param2(list): fuel at each city
        param3(int): miles per gallon
    Return: valid starting city
    """
    # since there is always a valid start city we can start at the first city
    # use the fact there is axectly enought fuel to travel to all cities
    valid_starting_city = 0
    current_fuel = 0
    for i in range(1, len(distances)):
        # compute how  much fuel is left if traveled to this city
        current_fuel += fuel[i-1] * mpg - distances[i-1]
        # if the fuel is negative the old valid start city is not valid anymore
        # and the current city is the new valid starting city
        if current_fuel < 0:
            valid_starting_city = i
            current_fuel = 0
    return valid_starting_city


if __name__ == "__main__":
    distances = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10
    print(validStartingCity(distances=distances, fuel=fuel, mpg=mpg))
