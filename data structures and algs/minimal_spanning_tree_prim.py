from weighted_graph import *

class BinaryHeap:
    # attributes:
    #    heap (an array)

    def __init__(self, heap=None):
        if heap is not None:
            self.heap = heap
        else:
            self.heap = []

    def parent(self, i):
        return (i-1) // 2

    def left(self, i):
        return ((2 * i) + 1)

    def right(self, i):
        return ((2 * i) + 2)

    # in linear time!
    def initialize(self, nums):
        self.heap = nums
        for i in range(len(self.heap) - 1, -1, -1):
            self.__heapify_down(i)

    def __str__(self):
        s = ""
        for item in self.heap:
            s += (str(item) + ", ")
        return s

    # private (not accessible outside of the class)
    def __heapify_up(self):
        pos = len(self.heap)-1  # position of newest item
        # Continue until the new element's parent is <= to the new element
        # OR it reaches the root
        while (pos > 0 and self.heap[pos].weight < self.heap[self.parent(pos)].weight):  # changed this to .weight
            self.swap(pos, self.parent(pos))
            pos = self.parent(pos)

    # Fix the heap order by continually swapping node at pos with its child
    # if the child is smaller that the node at pos
    def __heapify_down(self, pos):
        smallest = pos

        # if the left value is smaller than pos value
        if (self.left(pos) < len(self.heap) and self.heap[smallest].weight > self.heap[self.left(pos)].weight):
            smallest = self.left(pos)
        # if the right value is smaller than the "smallest" value
        if (self.right(pos) < len(self.heap) and self.heap[smallest].weight > self.heap[self.right(pos)].weight):
            smallest = self.right(pos)
        # if no leaves exist or already in min heap order
        if smallest == pos:
            return

        # Recurse!
        self.swap(pos, smallest)
        self.__heapify_down(smallest)

    # insert calls heapify up
    def insert(self, num):
        self.heap.append(num)
        self.__heapify_up()  # start at the end of the array

    # Just the root by the heap condition
    def get_min(self):
        return self.heap[0]

    # delete_min removes the smallest node and calls heapify down
    def delete_min(self):
        self.heap[0] = self.heap[-1]  # place last item at root
        self.heap.pop()
        self.__heapify_down(0)  # reheap down from the root

    def is_empty(self):
        return (len(self.heap) == 0)

    # Swap two nodes
    def swap(self, pos1, pos2):
        placeholder = self.heap[pos1]
        self.heap[pos1] = self.heap[pos2]
        self.heap[pos2] = placeholder


# Runtime: O(E log V)
# What is wrong with the approach in the handout is that the pqueue might be giving you edges with 2 undiscovered nodes.
# This is very inefficient and might force you to remove every edge from the PQ, so it will actually take VE log E time. 

def MST_Prim(graph):
    vertices = graph.get_vertices()
    if len(vertices)==0:
        return ({}, 0)
    else:
        start = list(vertices)[0]

    pq = BinaryHeap()
    visited_nodes = set()
    visited_nodes.add(start)
    visited_edges = set()
    sum_of_weights = 0

    for edge in graph.get_edges(start):
        if edge.weight is not None:
            pq.insert(edge)

    while not pq.is_empty() and len(visited_edges) < (len(vertices)-1):
        edge = pq.get_min()
        pq.delete_min()
        n1, n2 = edge.vertices
        w = edge.weight

        if n2 not in visited_nodes and n1 in visited_nodes:
            new_vertex = n2
        elif n1 not in visited_nodes and n2 in visited_nodes:
            new_vertex = n1
        else:
            continue

        visited_nodes.add(new_vertex)
        visited_edges.add(edge)
        sum_of_weights += w

        for edge in graph.get_edges(new_vertex):
            if edge.weight is not None and edge not in visited_edges:
                pq.insert(edge)

    return (visited_edges, sum_of_weights)




