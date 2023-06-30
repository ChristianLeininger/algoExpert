# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 29.06.2023

from typing import List


# O(n) time | O(1) space
def bestSeat(seats: List) -> int:
    """  Takes a list of seats and return the index of the best seat
    free seat is defined as 0 and taken as 1 find the seat with the
    longest distance to the next person to the left and right
    Args:
        param1(list): list of integers
    Return: index of the best seat
    """
    max_distance = 0
    best_seat = -1  # assume no best seat
    leftpointer = 0
    # this while terminate since the leftpointer is only increased
    # and this garanted since the last seat is always 1
    while leftpointer < len(seats):
        rightpointer = leftpointer + 1
        # while point on empty seat and not end of list
        while rightpointer < len(seats) and seats[rightpointer] == 0:
            rightpointer += 1
        # found a coupied seat
        # compute free seat distance with the difference of the pointers
        # and subtract 1 because the pointers point to the seat
        free_seats = rightpointer - leftpointer - 1
        # if the new free seat distance is bigger than the old one
        # update the max distance and the best seat
        if free_seats > max_distance:
            max_distance = free_seats
            best_seat = (leftpointer + rightpointer) // 2
        # move the left pointer to the next seat
        leftpointer = rightpointer
    return best_seat


if __name__ == "__main__":
    print(bestSeat([1, 0, 0, 1, 0, 0, 1]))
    print(bestSeat([1, 0, 0, 0, 1, 0, 1]))
