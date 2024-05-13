## Number of Ways to Traverse a Grid 


This repository provides an implementation of Dijkstra's Algorithm in Python, which is used to find the shortest paths between nodes in a graph. The algorithm works efficiently with graphs having non-negative edge weights.
No optimize uses a array to store nodes and weights cost O(n) to find Node with shortest path
for next node to explore.  Faster use min heap. 

### Idea of Dijkstra Algorithm:

1. Keep track of visited nodes
2. Create list of current shortes path
   Initilize all unknown paths with inf and the known start node with 0.

3. Loop over all nodes until all are visited.
   Then loop over the egdes of the current node.
   	Update the distance if the distance of the current node plus the egde weight 
   	is less then the current.
   Mark current node as visited
   Get the next node by taking the not visited node with the shortest path.
   Can be expensive if not a min heap is used 

Requirements  - Python 3.x 

Installation No additional installation is required. The standard Python library is sufficient to run the program and tests. 

To run the program:
```
python numberOfWaysToTraverseGraph.py
```
To run the test:
```
python -m unittest tests.py