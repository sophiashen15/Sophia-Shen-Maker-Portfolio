from weighted_graph import *

class Vertex:
    # attributes:
    #   node (str)
    #   d_value (int)

    def __init__(self, node='', d_val=None):
        self.node = node
        if d_val == None:
            self.d_val = float('inf')
        else:
            self.d_val = d_val

    def get_d_val(self):
        return self.d_val

    def change_d_val(self, new_val):
        self.d_val = new_val

    def __str__(self):
        return "(" + self.node + ", " + str(self.d_val) + ")"


class ModifiableBinaryHeap:
    # attributes:
    #    heap (an array)

    def __init__(self, heap=None):
        if heap is not None:
            self.heap = heap
            self.nodes_to_indicies = {}
            for i in range(len(heap)):
                self.nodes_to_indicies[heap[i]] = i
        else:
            self.heap = []
            self.nodes_to_indicies = {}

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
            self.nodes_to_indicies[self.heap[i]] = i
            self.__heapify_down(i)

    def __str__(self):
        return ", ".join(str(item) for item in self.heap)

    # private (not accessible outside of the class)
    def __heapify_up(self, pos=None):
        if pos == None:
            pos = len(self.heap)-1  # position of newest item
        # Continue until the new element's parent is <= to the new element
        # OR it reaches the root
        while (pos > 0 and self.heap[pos].d_val < self.heap[self.parent(pos)].d_val):  # changed this to .d_val
            self.swap(pos, self.parent(pos))
            pos = self.parent(pos)

    # Fix the heap order by continually swapping node at pos with its child
    # if the child is smaller that the node at pos
    def __heapify_down(self, pos):
        smallest = pos

        # if the left value is smaller than pos value
        if (self.left(pos) < len(self.heap) and self.heap[smallest].d_val > self.heap[self.left(pos)].d_val): # changed this to .d_val
            smallest = self.left(pos)
        # if the right value is smaller than the "smallest" value
        if (self.right(pos) < len(self.heap) and self.heap[smallest].d_val > self.heap[self.right(pos)].d_val): # changed this to .d_val
            smallest = self.right(pos)
        # if no leaves exist or already in min heap order
        if smallest != pos:
            # Recurse!
            self.swap(pos, smallest)
            self.__heapify_down(smallest)

    # insert calls heapify up
    def insert(self, vertex):
        self.heap.append(vertex)
        self.nodes_to_indicies[vertex] = len(self.heap) - 1
        self.__heapify_up()  # start at the end of the array

    # Just the root by the heap condition
    def get_min(self):
        return self.heap[0]

    # delete_min removes the smallest node and calls heapify down
    def delete_min(self):
        if not self.is_empty():
            min_element = self.heap[0]
            self.nodes_to_indicies.pop(min_element)
            self.nodes_to_indicies[self.heap[-1]] = 0 # update dict to place last item at root
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

        # update dictionary
        self.nodes_to_indicies[self.heap[pos1]] = pos1
        self.nodes_to_indicies[self.heap[pos2]] = pos2


    # decreases the priority of a key (log n time)
    def decrease_key(self, key, new_val):
        if key in self.nodes_to_indicies:
            pos = self.nodes_to_indicies[key]
            self.heap[pos].d_val = new_val
            self.__heapify_up(pos)

    def print_nodes_to_indicies(self):
        for key in self.nodes_to_indicies:
            print(key)
            print(str(self.nodes_to_indicies[key]))


# return dictionary of v:D(v) key value pairs
def dijkstrize(G, start):
    vertices = G.get_vertices()
    processed = {}
    for vertex in vertices:
        processed[vertex] = float('inf')
    processed[start] = 0
    
    # dict storing vertex name as key and vertex object as value
    vertex_dict = {}
    for vertex in vertices:
        if vertex == start:
            vertex_dict[vertex] = Vertex(vertex, 0)
        else:
            vertex_dict[vertex] = Vertex(vertex)

    pq = ModifiableBinaryHeap()
    pq.initialize(list(vertex_dict.values())) # initialize all vertices with d-values as priorities (linear time)

    while not pq.is_empty():
        current = pq.get_min()
        pq.delete_min()
        processed[current.node] = current.d_val

        for edge in G.get_edges(current.node):
            n1, n2 = edge.vertices
            if n1 != current.node:
                neighbor = n1
            else:
                neighbor = n2
            if processed[current.node] + edge.weight < processed[neighbor]:
                processed[neighbor] = processed[current.node] + edge.weight
                pq.decrease_key(vertex_dict[neighbor], processed[neighbor])


    return processed



