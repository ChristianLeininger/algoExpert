# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 30.05.2023

from typing import List

# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array: List):
        self.heap = []
        for iten in array:
            self.insert(iten)   
        return self.heap
    
    def siftDown(self):
        # Write your code here.
        pass

    def siftUp(self):
        """"  """
        root_sub_tree = len(self.heap) // 2 -1
        idx = len(self.heap) - 1
        while True:
            if idx == 0:
                break
            if self.heap[idx] < self.heap[root_sub_tree]:
                self.heap[idx], self.heap[root_sub_tree] = self.heap[root_sub_tree], self.heap[idx]
                idx = root_sub_tree
                root_sub_tree = idx // 2 
            else:
                break
            
    def peek(self):
        # Write your code here.
        pass

    def remove(self):
        # Write your code here.
        pass

    def insert(self, value):
        self.heap.append(value)
        self.siftUp()
