# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 12.06.2023


# O(n) time | O(n) space
def sunsetViews(buildings, direction):
    if len(buildings) == 0:
        return []
    if direction == "EAST":
        tallest_build_sf = buildings[-1]
        sol = [len(buildings)-1]
        for idx, build in enumerate(reversed(buildings)):
            idx = len(buildings) - 1 - idx
            if build > tallest_build_sf:
                sol = [idx] + sol
                tallest_build_sf = build
        return sol
    tallest_build_sf = buildings[0]
    sol = [0]
    for idx, build in enumerate(buildings):
        if build > tallest_build_sf:
            sol.append(idx)
            tallest_build_sf = build
    return sol
