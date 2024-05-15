# copyright 2024
# author: Christian Leininger
# Email: leiningc@tf.uni-freiburg.de
# date: 15.05.2024

import logging


def diskStacking(disks):
    """  Use dynamic programming to solve the disk stacking problem.
    The problem is as follows:
    You're given a non-empty array of arrays where each subarray holds 
    three integers and represents a disk.
    These integers denote each disk's width, depth, and height, respectively.
    Your goal is to stack up the disks and to maximize the total height of the stack.
    A disk must have a strictly smaller width, depth, and height than any other disk below it.
    Write a function that returns an array of the disks in the final stack, starting with the top disk and ending with the bottom disk.
    Note that you can't rotate disks; in other words, the integers in each subarray must represent [width, depth, height] at all times.
    You can assume that there will only be one stack with the greatest total height.
    Args:
        disks: list of lists of integers
    Returns:
        list of lists of integers representing the disks in the final stack
    """
    # first sort the disks by height in place
    disks.sort(key=lambda x: x[2])
    # create a list to store the heights of the disks
    heights = [disk[2] for disk in disks]
    # create a list to store the indices of the disks that are below the current disk
    sequence = [None for _ in disks]
    # track index of the disk with the maximum height
    max_height_idx = 0
    # start looping through the disks starting from the second disk
    for idx in range(1, len(disks)):
        current_disk = disks[idx]
        # print(heights)
        # loop through the disks before the current disk
        for j in range(0, idx):
            other_disk = disks[j]
            # check if the current disk can be stacked on top of the other disk
            #print(f"current_disk: {current_disk}, other_disk: {other_disk}")
            if check_dimensions(other_disk, current_disk):
                # check if the height of the current disk can be increased 
                # by stacking it on top of the other disk
                if heights[j] + current_disk[2] > heights[idx]:
                    heights[idx] = heights[j] + current_disk[2]
                    sequence[idx] = j
        if heights[idx] >= heights[max_height_idx]:
            max_height_idx = idx
    # return the stack
    return build_sequence(disks, sequence, max_height_idx)


def build_sequence(disks, sequence, current_idx):
    """Build the sequence of disks in the stack.
    Args:
        disks: list of lists of integers
        sequence: list of integers
        current_idx: integer
    Returns:
        list of lists of integers
    """
    # create a list to store the sequence of disks
    stack = []
    # loop through the sequence of disks
    while current_idx is not None:
        # append the current disk to the stack
        stack.append(disks[current_idx])
        # update the current index
        current_idx = sequence[current_idx]
    # stack is in order from bottom to top, so reverse it
    # print(stack)
    return list(reversed(stack))


def check_dimensions(disk1, disk2):
    """Check if disk1 can be stacked on top of disk2.
    Args:
        disk1: list of integers
        disk2: list of integers
    Returns:
        boolean that is True if disk1 can be stacked on top of disk2
    """
    # check if the width, depth, and height of disk1 are all strictly smaller than the width, depth, and height of disk2
    return disk1[0] < disk2[0] and disk1[1] < disk2[1] and disk1[2] < disk2[2]






if __name__ == "__main__":
    disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [2, 2, 1], [4, 4, 5]]
    diskStacking(disks)