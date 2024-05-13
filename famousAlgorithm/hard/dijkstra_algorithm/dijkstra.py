



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





if __name__ == "__main__":
    start = 0
    edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
    expected = [0, 7, 13, 27, 10, -1]
    actual = dijkstrasAlgorithm(start, edges)
    print(actual)