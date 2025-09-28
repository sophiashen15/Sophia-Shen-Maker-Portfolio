from weighted_graph import *

class BinaryHeap:
    # attributes:
    #    heap (an array)

    def __init__(self, heap=None):
        if heap == None:
            self.heap = []
        else:
            self.heap = heap

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

class UnionFind:
    def __init__(self, objects):
        self.parents = {obj:obj for obj in objects} # parents[i] represents the ith parent
        self.sizes = {obj:1 for obj in objects} # represents num elements in tree

    # Goes up tree to find root
    def find_root(self, obj):
        while self.parents[obj] != obj:
            obj = self.parents[obj]
        return obj

    # Checks if obj_1 and obj_2 are in the same tree
    def in_same_group(self, obj_1, obj_2):
        return (self.find_root(obj_1) == self.find_root(obj_2))

    # merges 2 objects into 1 tree
    def merge(self, obj_1, obj_2):
        r1 = self.find_root(obj_1)
        r2 = self.find_root(obj_2)
        # check which one has more elements
        if r1 != r2:
            # print(f"Merging {obj_1} (root: {r1}, size: {self.sizes[r1]}) and {obj_2} (root: {r2}, size: {self.sizes[r2]})")
            if self.sizes[r1] > self.sizes[r2]:
                self.parents[r2] = r1
                self.sizes[r1] += self.sizes[r2]
                # print(f"{obj_2} is now pointing to {obj_1} (new size of {obj_1}'s tree is {self.sizes[r1]})")
            elif self.sizes[r2] > self.sizes[r1]:
                self.parents[r1] = r2
                self.sizes[r2] += self.sizes[r1]
                # print(f"{obj_1} is now pointing to {obj_2} (new size of {obj_2}'s tree is {self.sizes[r2]})")

            else:
                self.parents[r1] = r2
                self.sizes[r2] += self.sizes[r1]
                # print(f"{obj_1} is now pointing to {obj_2} (new size of {obj_2}'s tree is {self.sizes[r2]})")


def MST_Kruskal(G):
	edges = G.get_all_edges()
	nodes = G.get_vertices()
	uf_nodes = UnionFind(list(nodes))
	visited_edges = set()
	visited_nodes = set()
	weight_sum = 0

	# create pq with all edges
	pq = BinaryHeap()
	pq.initialize(list(edges))

	# check that all nodes are there and it is connected!
	while visited_nodes != nodes or len(visited_edges) < (len(nodes)-1):
		edge = pq.get_min()
		pq.delete_min()
		n1, n2 = edge.vertices
		visited_nodes.add(n1)
		visited_nodes.add(n2)

		# check that n1, n2 are not in a cycle
		if not uf_nodes.in_same_group(n1, n2):
			uf_nodes.merge(n1, n2)
			visited_edges.add(edge)
			weight_sum += edge.weight

	return (visited_edges, weight_sum)


# Tests
data1 = [('A', 'B', 8), ("A", "C", 3), ("B", "D", 3), ("B", "C", 7),
         ("D", "C", 4), ("C", "E", 2), ("D", "E", 2)]
G1 = WeightedGraph(data1)

# print(MST_Kruskal(G1))

example = [('A', 'B', 5), ('B', 'E', 2), ('E', 'C', 3), ('C', 'D', 1), ('D', 'A', 1.5), ('A', 'C', 1), ('D', 'B', 6)]
G2 = WeightedGraph(example)
# print(MST_Kruskal(G2))

