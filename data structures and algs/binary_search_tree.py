# A binary search tree class, as well as the nodes that make up the tree

sentinel = object()


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent, self.left, self.right = None, None, None

    # Overwrite this method (and.or put a __str__ in BinarySearchTree) if
    # you want.
    def __str__(self):
        return str(self.value) + (" left" if self.left else "") + \
            (" right" if self.right else "") + \
            (" parent" if self.parent else "")


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def find(self, value, node=sentinel):
        if node == sentinel:
            node = self.root
        if node is None:
            return None
        if node.value == value:
            return node
        if value < node.value:
            return self.find(value, node.left)
        if value > node.value:
            return self.find(value, node.right)

    # Returns depth. A tree with single node -> 0. A tree with no nodes -> -1.
    def get_depth(self, node=sentinel):
        if node == sentinel:
            node = self.root
        if node is None:  # tree with no nodes
            return -1
        if node.left is None and node.right is None:  # tree with single node
            return 0
        if node.left is None and node.right:  # tree with only left branch
            return (1 + self.get_depth(node.right))
        if node.right is None and node.left:  # tree with only right branch
            return (1 + self.get_depth(node.left))
        if node.left and node.right:  # tree with both branches
            return (1 + max(self.get_depth(node.left), self.get_depth(node.right)))

    # Creates node whose value is num and places it in the BST at correct spot
    # Recursive algorithm where root is the location in tree
    def insert(self, num):
        # If the tree is empty create a root node with the given value
        if self.root is None:
            self.root = TreeNode(num)
        else:
            # Call the recursive insert method
            self.insert_recursive(num, self.root)

    def insert_recursive(self, num, root):
        if num < root.value:
            if root.left is None:
                new_node = TreeNode(num)  # create new node, set as left child
                new_node.parent = root
                root.left = new_node
            else:
                # Recursively insert into the left subtree
                self.insert_recursive(num, root.left)
        elif num > root.value:
            if root.right is None:
                new_node = TreeNode(num)  # create new node, set as right child
                new_node.parent = root
                root.right = new_node
            else:
                # Recursively insert into the left subtree
                self.insert_recursive(num, root.right)

    # Prints out the values of a binary tree's nodes in numerical order
    def traverse_1(self, node=sentinel):
        if node == sentinel:
            node = self.root

        if node is not None:
            self.traverse_1(node.left)
            print(node.value)
            self.traverse_1(node.right)

    def traverse_2(self):
        ordered_list = []
        self.traverse_2_search(ordered_list, self.root)
        return ordered_list

    def traverse_2_search(self, ordered_list, node=sentinel):
        if node == sentinel:
            node = self.root

        if node is not None:
            self.traverse_2_search(ordered_list, node.left)
            ordered_list.append(node.value)
            self.traverse_2_search(ordered_list, node.right)

    # Returns the ndoe whose value is the smallest value on the tree
    def find_smallest(self, node):
        if node:
            current = node
            while current.left:
                current = current.left
            return current
        else:
            return None

    # Finds the node whose value is the next largest value after node
    def successor(self, node):
        successor = None
        # If the node has a right subtree
        if node.right:
            return self.find_smallest(node.right)

        # If no right subtree, check if it is in the left subtree of parent
        current = self.root
        while current:
            if node.value < current.value:
                successor = current
                current = current.left
            if node.value > current.value:
                current = current.right
            else:
                break
        return successor

    def delete(self, node_to_del, root=sentinel):
        if root == sentinel:
            root = self.root
        # Check tree is not empty
        if root is None:
            return None

        # node to delete has no children
        if node_to_del.left is None and node_to_del.right is None:
            if node_to_del.parent is None:
                self.root = None
                return None
            if node_to_del == node_to_del.parent.left:
                node_to_del.parent.left = None
            else:
                node_to_del.parent.right = None

        # node to delete has one child
        elif node_to_del.left is None or node_to_del.right is None:
            if node_to_del.left:
                child = node_to_del.left
            else:
                child = node_to_del.right
            if node_to_del.parent is None:
                child.parent = None
                self.root = child  # since ntd has no parent, it was root
                return child
            if node_to_del == node_to_del.parent.left:
                node_to_del.parent.left = child
            else:
                node_to_del.parent.right = child
            child.parent = node_to_del.parent

        # node to delete has two children
        else:
            successor = self.successor(node_to_del)
            node_to_del.value = successor.value
            self.delete(successor)

    def __str__(self):
        lines = []
        self._build_tree_string(self.root, 0, lines)
        return "\n".join(reversed(lines))

    def _build_tree_string(self, node, level, lines):
        if node is not None:
            self._build_tree_string(node.left, level + 1, lines)
            lines.append("  " * level + str(node.value))
            self._build_tree_string(node.right, level + 1, lines)
