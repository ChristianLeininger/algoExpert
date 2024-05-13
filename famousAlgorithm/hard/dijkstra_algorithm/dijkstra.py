



def dijkstrasAlgorithm(start, edges):
    """ 
        Use dijkstra's algorithm to find the shortest path 
        from start to all other nodes graph.
        Its directed graph with positive weights.
        The graph is represented as an adjacency list.
        The first element of the edge is the node and the second is the weight.
    
    Args:
        start: int
        edges: list of list of list of int
    
    """
    amount_edges = len(edges)
    # Initialize the distance array with infinity
    distance = [float("inf") for _ in range(amount_edges)]
    # Initialize the start node with 0
    distance[start] = 0
    # Initialize the visited array with False
    visited = [False for _ in range(amount_edges)]
    # Initialize the current node with the start node
    current_node = start
    # Loop through all the nodes until all nodes are visited
    # get the next node with the minimum distance or -1 if all nodes are visited
    while current_node != -1:
        # Get the edges of the current node
        for edge in edges[current_node]:
            # Get the node and the weight
            node, weight = edge
            # Update the distance array with the minimum distance
            distance[node] = min(distance[node], distance[current_node] + weight)
        # Mark the current node as visited
        visited[current_node] = True
        # Get the next node with the minimum distance
        current_node = get_next_node(distance, visited)
    # Return the distance array
    return list(map(lambda x: -1 if x == float("inf") else x, distance))




def get_next_node(distance, visited):
    """ 
        Get the next node with the minimum distance.
        If nodes are in array its expenisve to find the minimum distance.
        Worst case is O(n) where n is the number of nodes.
    
    Args:
        distance: list of int
        visited: list of bool
    
    """
    # Initialize the minimum distance with infinity
    min_distance = float("inf")
    # Initialize the next node with -1
    next_node = -1
    # Loop through all the nodes
    for node, dist in enumerate(distance):
        # If the node is not visited and the distance is less than the minimum distance
        if not visited[node] and dist < min_distance:
            # Update the minimum distance
            min_distance = dist
            # Update the next node
            next_node = node
    # Return the next node
    return next_node    



if __name__ == "__main__":
    start = 0
    edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
    expected = [0, 7, 13, 27, 10, -1]
    actual = dijkstrasAlgorithm(start, edges)
    print(actual)