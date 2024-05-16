

def twoColorable(edges):
    """ Find away to color all nodes in a graph with two colors such that 
        no two adjacent nodes have the same color.
    Args:
        edges: A list of edges in the graph.
    Returns:
        A boolean value indicating if the graph is two colorable.
    """
    color = [None for _ in range(len(edges))]
    color[0] = True # color the first node with 0
    stack = [0] # assume there is a node 0
    # loop through the stack until it is empty
    while stack:
        # pop the last node from the stack
        node = stack.pop()
        # check all the neighbors of the node
        for neighbor in edges[node]:
            # if the neighbor has not been colored, color it
            if color[neighbor] is None:
                color[neighbor] = not color[node]
                # add the neighbor to the stack to check its neighbors
                stack.append(neighbor)
            elif color[neighbor] == color[node]:
                # this means two adjacent nodes have the same color
                # so no coloring is possible
                return False

    # now all nodes have been colored 
    # without any two adjacent nodes having the same color
    
    return True




if __name__ == '__main__':
    edges = [
        [1, 3],
        [0, 2],
        [1, 3],
        [0, 2]
        ]
    print(twoColorable(edges)) # True