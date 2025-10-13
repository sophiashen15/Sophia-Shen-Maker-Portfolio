# Java Data Structures and Algorithms

A collection of data structures and projects implemented in Java.

## Core Data Structures

**Linked Lists**
- `int_linked_list.java` - Integer-specific singly linked list
- `doubly_linked_list.java` - doubly linked list with two directions of traversal

**Array-Based Structures**
- `dynamic_array.java` - Resizable array with size management
- `ordered_array_int_set.java` - Sorted array-based integer set
- `unordered_array_int_set.java` - Unsorted array-based integer set

**Tree Structures**
- `int_binary_search_tree.java` - Integer binary search tree with recursive operations
- `tree_int_set.java` - Tree-based integer set implementation

**Hash-Based Structures**
- `mod_table_int_set.java` - Hash table using modular arithmetic
- `int_set.java` - Abstract integer set interface

## Sub-Projects

**huffman encoding/**
Data Compression Algorithm
- Builds optimal Huffman trees from character frequency analysis
- Implements encoding and decoding for text compression
- Demonstrates greedy algorithm principles and tree construction

**random writer/**
Markov Chain Text Generation
- Implements k-order Markov chain analysis (levels 0-10) on source texts
- Analyzes character sequence probabilities to generate stylistically similar output
- Selects next characters based on k-character seeds and frequency analysis
- Only custom doubly linked list implementation (no built-in Java collections)
- Uses probabilistic modeling and natural language processing fundamentals
