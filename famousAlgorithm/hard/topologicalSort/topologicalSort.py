# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 04.06.2023

from typing import List


def topologicalSortOwn(jobs: List, deps: List) -> List:
    """  Compute  a valid order of jobs using topological sort
         create( dict) with all jobs and empty list add all
         dependencies to the list if the list is empty add the
         job to the order list and remove the job from the dict
         remove the job from all dependencies until the dict is
         empty or no empty list is found in the dict
    Args:
        param1: (list) all jobs
        param2: (list) all dependencies
    Retrun (list) order of jobs
    """
    dict_deps = {item: [] for item in jobs}
    for d in deps:
        dict_deps[d[1]].append(d[0])
    order = []
    key = None
    for k, v in dict_deps.items():
        if v == []:
            key = k
            find_empty = True
            break
    while True:
        if len(dict_deps) == 0:
            break
        for k, v in dict_deps.items():
            if v == []:
                key = k
                order.append(k)
                dict_deps.pop(key)
                break
        else:
            # no empty list
            return []
        for k in dict_deps.keys():
            if key in dict_deps[k]:
                dict_deps[k].remove(key)
        if len(dict_deps) == 0:
            return order


def topologicalSort(jobs, deps):
    """  Master solution  """
    return []
