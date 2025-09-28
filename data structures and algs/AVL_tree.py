# Implementation of AVL Tree (self-balancing binary search trees) data structure in Python
import math
from random import randint, Random, randrange
import sys
import random
sentinel = object()


class AVLNode:
    def __init__(self, value, left=None, right=None, depth=0):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None
        self.depth = depth
     
    def __str__(self):
        return str(self.value)


class AVLTree:
    def __init__(self):
        self.root = None

    # Finds the node with given value
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
            x = max(self.get_depth(node.left), self.get_depth(node.right))
            return (1 + x)

    # Inserts a node into the AVLTree and balances as necessary
    def insert(self, value, node=sentinel, parent=None, is_left=None):
        if node == sentinel:
            node = self.root
        if node is None:
            new_node = AVLNode(value)
            new_node.parent = parent
            if new_node.parent:
                setattr(new_node.parent, "left" if is_left else "right",
                        new_node)
            else:
                self.root = new_node
            self.balance_and_set_depth(new_node)
            return

        tree_list = self.traverse_2()
        if value in tree_list:
            # cannot add value that already exists in tree
            return

        if value < node.value:
            self.insert(value, node.left, node, True)
        if value > node.value:
            self.insert(value, node.right, node, False)

    # Prints out the values of an AVLtree's nodes in numerical order
    def traverse_1(self, node=sentinel):
        if node == sentinel:
            node = self.root

        if node is not None:
            self.traverse_1(node.left)
            print(node.value)
            self.traverse_1(node.right)

    # Stores the values of an AVLTree in numerical order in a list
    def traverse_2(self):
        ordered_list = []
        self.traverse_2_search(ordered_list, self.root)
        return ordered_list

    # Helper function for traverse_2
    def traverse_2_search(self, ordered_list, node=sentinel):
        if node == sentinel:
            node = self.root

        if node is not None:
            self.traverse_2_search(ordered_list, node.left)
            ordered_list.append(node.value)
            self.traverse_2_search(ordered_list, node.right)

    # Returns the node whose value is the smallest value on the tree
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

    # Helper function for delete
    def get_node_type(self, child):
        if child.parent is not None:
            return "left" if child.parent.left == child else "right"
        else:
            return None

    # Deletes a given node from the AVLTree and balances as necessary
    # (b_and_sd is a boolean that is necessary for when node has 2 child)
    def delete(self, node, b_and_sd=True):
        if node.parent:
            node_type = self.get_node_type(node)

        # case 1: node has no children
        if node.left is None and node.right is None:
            if node.parent:
                setattr(node.parent, node_type, None)
                if b_and_sd:
                    self.balance_and_set_depth(node.parent)
            else:
                self.root = None
            return

        # case 2: node has exactly one child
        if node.left is None or node.right is None:
            child_node = node.left if node.left is not None else node.right
            child_node.parent = node.parent
            if node.parent:
                setattr(node.parent, node_type, child_node)
                if b_and_sd:
                    self.balance_and_set_depth(child_node.parent)
            else:
                self.root = child_node
            return

        # case 3: node has two children
        suc_node = node.right
        while suc_node.left:
            suc_node = suc_node.left

        suc_node_parent = suc_node.parent
        self.delete(suc_node, False) # when recursing on suc, do NOT want to call b_and_sd
        suc_node.left = node.left
        suc_node.left.parent = suc_node
        suc_node.right = node.right
        # if suc_node was node.right, then after deleting suc_node, node only has a left child! 
        # make sure node.right exists before setting its parent.
        if suc_node.right:
            suc_node.right.parent = suc_node
        suc_node.parent = node.parent # this is for calling balance and set depth!
        if node.parent:
            setattr(node.parent, node_type, suc_node)
        else:
            self.root = suc_node

        # Checking for the special case where suc_node_parent is the deleted node
        if suc_node_parent == node:
            self.balance_and_set_depth(suc_node)
        else:
            self.balance_and_set_depth(suc_node_parent)


    # Checks if a tree satisfies the binary search tree condition
    def is_bst(self, root=sentinel, min_v=float('-inf'), max_v=float('inf')):
        if root == sentinel:
            root = self.root

        if root is None:
            return True
        if root.value < max_v and root.value > min_v:
            return self.is_bst(root.left, min_v, root.value) and \
                self.is_bst(root.right, root.value, max_v)
        else:
            return False

    # Checks if the depths of any pair of sibling subtree differ no more than 1
    def is_balanced(self, root=sentinel):
        if root == sentinel:
            root = self.root
        if root is None:
            return True

        left_depth = getattr(root.left, "depth", -1)
        right_depth = getattr(root.right, "depth", -1)

        if abs(left_depth - right_depth) > 1:
            return False
        return self.is_balanced(root.left) and self.is_balanced(root.right)

    # Rotates the tree depending on arugment "direction"
    def rotate(self, root, direction):
        parent_pointer = root.parent
        left_depth = getattr(root.left, "depth", -1)
        right_depth = getattr(root.right, "depth", -1)

        # Right rotation
        if direction == "right":
            new_root = root.left
            root.left = new_root.right
            if root.left:
                root.left.parent = root
            new_root.right = root

        # Left rotation
        elif direction == "left":
            new_root = root.right
            root.right = new_root.left
            if root.right:
                root.right.parent = root
            new_root.left = root

        # Update parent pointers
        new_root.parent = parent_pointer
        root.parent = new_root

        if new_root.parent is not None:
            if new_root.parent.value > new_root.value:
                new_root.parent.left = new_root
            elif new_root.parent.value < new_root.value:
                new_root.parent.right = new_root
        else:
            self.root = new_root  # Update self.root if necessary

        # Update the root depth and new_root depth
        root.depth = max(getattr(root.left, "depth", -1), getattr(root.right, "depth", -1)) + 1
        new_root.depth = max(getattr(new_root.left, "depth", -1), getattr(new_root.right, "depth", -1)) + 1

        assert self.is_bst()
        return new_root
  
    # Balances and sets depths such that no two subtrees have a depth difference > 1
    def balance_and_set_depth(self, root):
        if root is None:
            return None

        left_depth = getattr(root.left, "depth", -1)
        right_depth = getattr(root.right, "depth", -1)
 
        # Recompute the depth of root
        root.depth = max(left_depth, right_depth) + 1

        # Right rotation
        if (left_depth - right_depth) > 1:
            if root.left and getattr(root.left.right, "depth", -1) > getattr(root.left.left, "depth", -1):
                root.left = self.rotate(root.left, "left")
            return self.rotate(root, "right")

        # Left rotation
        if (right_depth - left_depth) > 1:
            if root.right and getattr(root.right.left, "depth", -1) > getattr(root.right.right, "depth", -1):
                root.right = self.rotate(root.right, "right")
            return self.rotate(root, "left")

        # Recursively go up the ancestral path to update depths
        if root.parent is not None:
            # Update parent after rotation
            if root.parent.left == root:
                root.parent.left = root
            else:
                root.parent.right = root
            return self.balance_and_set_depth(root.parent)

    def __str__(self):
        if self.root is None:
            return "Tree is empty."

        result = ""
        stack = [(self.root, "", True)]
        while stack:
            node, prefix, is_left = stack.pop()
            if node is not None:
                result += prefix + ("|-- " if is_left else "+-- ") + str(node.value) + f" (Depth: {node.depth}\n"
                stack.append((node.right, prefix + ("|   " if is_left else "    "), False))
                stack.append((node.left, prefix + ("|   " if is_left else "    "), True))

        return result
