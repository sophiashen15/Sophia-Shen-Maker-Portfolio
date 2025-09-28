# An implementation of binomial heaps

class Node:
    # attributes
    #    - value (int)
    #    - children (list of nodes)

    def __init__(self, value, children=None):
        self.value = value
        if children:
            self.children = children
        else:
            self.children = []

    def __str__(self):
        string = str(self.value) + ", "
        for child in self.children:
            if child:
                string += str(child) + ", "
        return string


class BinomialHeap:
    # attributes
    #    - heap (list where index-k element = root of B_k binomial tree)

    def __init__(self, heap=[]):
        self.heap = heap

    # To get the min node, compare the roots of trees, return smallest value
    def get_min(self):
        if self.heap == []:
            return None
        min_value = float('inf')
        for tree in self.heap:
            if tree and tree.value < min_value:
                min_value = tree.value  # tree is the root of a tree
        return min_value

    # Removes the minimum of a one-element list and merges its children
    def delete_min(self):
        if self.heap == []:
            return None
        min_value = float('inf')
        min_index = float('inf')
        min_node = None
        for i in range(len(self.heap)):
            if self.heap[i] and self.heap[i].value < min_value:
                min_value = self.heap[i].value  # tree is the root of a tree
                min_node = self.heap[i]
                min_index = i
        self.heap.pop(min_index)
        self.merge(BinomialHeap(min_node.children))

    def insert(self, num):
        b = BinomialHeap([Node(num)])  # create new binomial heap of size 1
        self.merge(b)

    # Takes heaps of size n and m, creates heap of size n+m
    def merge(self, bin_heap_2):

        # Determine the minimum length of the two heaps
        min_length = min(len(self.heap), len(bin_heap_2.heap))

        i = 0
        carry = None

        while i < min_length:
            if not self.heap[i] and not bin_heap_2.heap[i] and carry:
                self.heap[i] = carry
            elif bin_heap_2.heap[i] and not self.heap[i] and not carry:
                self.heap[i] = bin_heap_2.heap[i]
            elif bin_heap_2.heap[i] and self.heap[i] and not carry:
                carry = self.__combine(bin_heap_2.heap[i], self.heap[i])
                self.heap[i] = None
            elif not bin_heap_2.heap[i] and self.heap[i] and carry:
                carry = self.__combine(self.heap[i], carry)
                self.heap[i] = None
            elif bin_heap_2.heap[i] and not self.heap[i] and carry:
                carry = self.__combine(bin_heap_2.heap[i], carry)

            i += 1

        # Handle any remaining elements in the longer list
        while i < len(self.heap):
            if self.heap[i]:
                carry = self.__combine(carry, self.heap[i])
                self.heap[i] = None
            else:
                self.heap[i] = carry
                carry = None
            i += 1

        # Append any remaining carry to the longer list
        if carry:
            self.heap.append(carry)

        """
        if self.heap == []:
            self.heap = bin_heap_2.heap

        # always set self.heap as the longer list
        if len(self.heap) < len(bin_heap_2.heap):
            placeholder = self.heap
            self.heap = bin_heap_2.heap
            bin_heap_2.heap = placeholder

        i = 0
        carry = None

        while i < len(bin_heap_2.heap) or carry is not None:

            # if there is one tree present
            if not self.heap[i] and not bin_heap_2.heap[i] and carry:
                self.heap[i] = carry
            elif bin_heap_2.heap[i] and not self.heap[i] and not carry:
                self.heap[i] = bin_heap_2.heap[i]

            # if there are two trees present
            elif bin_heap_2.heap[i] and self.heap[i] and not carry:
                carry = self.__combine(bin_heap_2.heap[i], self.heap[i])
                self.heap[i] = None
            elif not bin_heap_2.heap[i] and self.heap[i] and carry:
                carry = self.__combine(self.heap[i], carry)
                self.heap[i] = None
            elif bin_heap_2.heap[i] and not self.heap[i] and carry:
                carry = self.__combine(bin_heap_2.heap[i], carry)

            # if there are three trees present
            elif bin_heap_2.heap[i] and self.heap[i] and carry:
                # keep the self.heap[i] as the same
                carry = self.__combine(carry, bin_heap_2.heap[i])
            i += 1

        # after going through bin_heap_2, if there is extra carry
        while i < len(self.heap) and carry:
            if self.heap[i]:
                carry = self.__combine(carry, self.heap[i])
                self.heap[i] = None
            else:
                self.heap[i] = carry
                carry = None
                break
            i += 1

        # self.heap is completed, if there is a last carry
        if carry:
            self.heap.append(carry)
        """

    # Takes two binomial trees of height k, returns binomial tree of height k+1
    def __combine(self, tree1, tree2):
        if (tree1.value <= tree2.value):
            tree1.children.append(tree2)
            return tree1
        else:
            tree2.children.append(tree1)
            return tree2

    def is_empty(self):
        return (len(self.heap) == 0)

    def __str__(self):
        string = ""
        for tree in self.heap:
            string += str(tree) + "\n"
        return string


# Takes list of nums, puts them in a binomeal heap, removes in increasing order
def binomial_heapsort(nums):
    new_list = []
    b = BinomialHeap()
    for num in nums:
        b.insert(num)
    while not b.is_empty():
        new_list.append(b.get_min())
        b.delete_min()
    return new_list


b = BinomialHeap()
for i in [2, 3]:
    b.insert(i)
print(b.heap)

c = BinomialHeap()
for i in [12, 13, 14, 15, 61, 1, 2, 3, 5, 4, 6]:
    c.insert(i)

c.merge(b)
print(c)
