# A\ simple linked list implementation.
# Node n is the last item in the list iff n.next is None.

class Node:
    # attributes:
    #   value (can be anything)
    #   next (another Node)

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    # attributes:
    #   head (a Node)
    #   num_items
    # ****************
    # methods:
    #   insert
    #   find
    #   delete
    #   size

    def __init__(self, inputs=[]):
        self.head = None
        self.num_items = 0
        for value in reversed(inputs):
            self.insert(value)

    def __str__(self):
        output = []
        current_node = self.head
        while current_node:
            output.append(str(current_node.value))
            current_node = current_node.next
        return " -> ".join(output)

    # Creates a Node with the given value and inserts into the
    # front of the list.
    def insert(self, value):
        self.num_items += 1
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Finds the first node with the given value. Returns None if there is
    # no such node.
    def find(self, value):
        current = self.head
        while current and current.value != value:
            current = current.next
        return current

    # Deletes given node. Can be used in conjunction with find.
    def delete(self, node):
        self.num_items -= 1
        if (node == self.head):
            self.head = self.head.next
        else:
            current = self.head
            while current and current.next != node:
                current = current.next
            current.next = current.next.next

    def size(self):
        return self.num_items
