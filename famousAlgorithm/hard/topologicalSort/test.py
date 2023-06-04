# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 04.06.2023

from topologicalSort import topologicalSort, topologicalSortOwn
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        jobs = [1, 2, 3, 4]
        deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
        order = topologicalSortOwn(jobs, deps)
        self.assertEqual(isValidTopologicalOrder(order, jobs, deps), True)


def isValidTopologicalOrder(order, jobs, deps):
    """" Check if the order is valid for
         the order of jobs and the dependencies
    Args:
        param1: (list) order of jobs
        param2: (list) all jobs
        param3: (list) all dependencies
    Return: (bool) True if valid else False
    """
    visited = {}
    for candidate in order:
        for prereq, job in deps:
            if candidate == prereq and job in visited:
                return False
        visited[candidate] = True
    for job in jobs:
        if job not in visited:
            return False
    return len(order) == len(jobs)
