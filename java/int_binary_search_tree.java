import java.util.*;
import static java.lang.Math.*;

/**
 * A binary search tree of integers.
 *
 * In addition to usual methods like insert and hasValue, this class 
 * also includes some strange methods that wouldn't normally go in a
 * search tree. These are included because they are good practice
 * exercises.
 *
 * @author Sophia Shen
 */
public class IntBinarySearchTree{
    // --------------------------------------------------------------------
    // Private classes
    // --------------------------------------------------------------------

    /** 
     * Data-only class to store Nodes. 
     * Only accessible within IntBinarySearchTree.
     */
    private static class Node {
        public int data;
        public Node left;
        public Node right;
        
        public Node(int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }

    
    // --------------------------------------------------------------------
    // Private state variables
    // --------------------------------------------------------------------
    private Node root;

    // --------------------------------------------------------------------
    // Public methods
    // --------------------------------------------------------------------
    /**
     * Construct an empty search tree.
     */
    public IntBinarySearchTree() {
        root = null;
    }

    /**
     * Construct a search tree from a given array of values.
     * 
     * @param  inputArray  array of values to be used to construct the tree
     */
    public IntBinarySearchTree(int[] inputArray) {
        for (int i = 0; i < inputArray.length; i++) {
            insert(inputArray[i]);
        }    
    }

    /**
     * Sets up this tree to be a sample binary search tree. This is just for
     * testing purposes.
     */
    public void setToSampleTree1() {
        root = new Node(52);
        root.left = new Node(29);
        root.left.left = new Node(10);
        root.left.right = new Node(37);
        root.left.left.right = new Node(17);
        root.right = new Node(75);
        root.right.left = new Node(62);
        root.right.right = new Node(92);
        root.right.left.left = new Node(58);
        root.right.left.right = new Node(68);
    }
    
    /**
     * Sets up this tree to be a sample binary search tree. This is just for
     * testing purposes.
     */
    public void setToSampleTree2() {
        root = new Node(5);
        root.left = new Node(1);
        root.left.right = new Node(4);
        root.left.right.left = new Node(3);
        root.left.right.left.left = new Node(2);
    }
    
    /**
     * Sets up this tree to be a sample binary search tree. This is just for
     * testing purposes.
     */
    public void setToSampleTree3() {
        // make your own sample tree with 12 Nodes
        // it should be almost balanced, but not quite
        // draw it out on paper first!

    }
    
    /**
     * Return the values as a string.
     * 
     * The format is as follows: "12 (4 16 (13 _))"
     * Left to right, inorder traversal:
     *  Start with the root, each pair of children is enclosed in parentheses
     *  Any empty spaces are represented with an underscore.
     * 
     * sampleTree2 from above is represented by "5 (1 (_ 4 (3 (2 _) _)) _)"
     * @return  String  
     */
    @Override
    public String toString() {
        return toStringRecursion(root);
    }

    /**
     * Prints the tree on its side, root on the left.
     */ 
    public void print() {
        printTree(root, 0);
    }

    /**
     * Return if data exists in tree.
     */
    public boolean find(int data) {
        return findData(root, data);
    }

    /**
     * Inserts a value into tree.
     * Values in left subtree < root, right >= root
     */
    public void insert(int data) {
        insertData(root, data);
    }

    /**
     * Deletes data from tree. 
     * Returns if deletion was possible. 
     */
    public boolean delete(int data) {
        if (find(data) == false) {
            return false;
        }
        deleteData(root, data);
        return true;
    }

    /**
     * Returns the sum of nodes of the tree.
     */
    public int sum() {
        return sumTree(root);
    }

    /**
     * Returns the number of nodes in a tree. 
     */
    public int countNodes() {
        return numNodes(root);
    }

    /**
     * Returns the number of branches in a tree. 
     */
    public int countBranches() {
        return numBranches(root);
    }


    /**
     * Returns the number of leaves in a tree. 
     */
    public int countLeaves() {
        return numLeaves(root);
    }

    /**
     * Returns the height of a tree. 
     */
    public int height() {
        return findHeight(root);
    }    

    /**
     * Return true if this tree is full; false otherwise.
     * A tree is full if each level has the maximum number of nodes or 0 nodes.
     */
    public boolean isFull() {
        return checkIfFull(root, 1, height());
    }

    /**
     * Return true if this tree is balanced; false otherwise.
     * At every node, the heights of the subtrees differ by no more than 1.
     */
    public boolean isBalanced() {
        return checkIfBalanced(root);
    }

    // --------------------------------------------------------------------
    // Private methods
    // --------------------------------------------------------------------

    // Hint: All recursive solutions rely on a call to a private method!

    private String toStringRecursion(Node root) {
        
        String contents = "";

        if (root == null) {
            return contents;
        }
        contents += root.data;

        // Conditionals are only here to keep nice spacing 
        // (underscores when a child does not exist)
        if (root.left != null && root.right == null){
            contents += " (" + toStringRecursion(root.left) + " _)";
        } 
        else if (root.left == null && root.right != null){
            contents += " (_ " + toStringRecursion(root.right) + ")";
        }
        else if (root.left != null && root.right != null) {
            contents +=  " (" + toStringRecursion(root.left) + " " + toStringRecursion(root.right) +  ")";
        }
        return contents;
        
    }

    // prints tree on its side, root on the left.
    // right to left inorder traversal
    private void printTree(Node tree, int depth) {
        
        if (tree == null){
            return;
        }
        printTree(tree.right, depth + 1);   // Right side printed on top

        for (int i = 0; i < depth; i++){    // Manage indentations
            System.out.print("   ");
        }   
        System.out.println(tree.data);      // Current data
        printTree(tree.left, depth + 1);    // Left side on bottom
    }

    // returns if data exists in given tree.
    private boolean findData(Node root, int data) {
        if (root == null) {
            return false;
        } else {
            if (data == root.data) {
                return true;
            } else if (data < root.data) {
                return findData(root.left, data);
            } else {
                return findData(root.right, data);
            }
        }
    }

    // inserts data into given tree.
    private void insertData(Node root, int data) {
        if (this.root == null) {
            this.root = new Node(data);
        } 

        else {
            if (data < root.data) {
                if (root.left != null) {
                    insertData(root.left, data);
                } else {
                    root.left = new Node(data);
                }
            }
            else {
                if (root.right != null) {
                    insertData(root.right, data);
                } else {
                    root.right = new Node(data);
                }
            }
        }
    }

    // deletes data from a tree recursively
    private Node deleteData(Node root, int data) {
        if (root == null) {
            return root;
        }

        if (this.root.data == data && this.root.left == null && this.root.right == null) {
            this.root = null;
        }
        else if (this.root.data == data && this.root.left == null) {
            this.root = root.right;
        }
        else if (this.root.data == data && this.root.right == null) {
            this.root = root.left;
        }

        if (data < root.data) {
            root.left = deleteData(root.left, data);
        }
        else if (data > root.data) {
            root.right = deleteData(root.right, data);
        } 

        else {
            if (root.left == null) {
                return root.right;
            } 
            else if (root.right == null) {
                return root.left;
            }

            root.data = findSmallest(root.right); // find left most node in right subtree
            root.right = deleteData(root.right, root.data); // delete left most node in right subtree
        }
        return root;
    }



    // helper for deleteData: finds parent of given current Node in tree. 
    private Node findParent(Node node, int data) {
        if (node.right == null && node.left == null) {
            if (node.data == data) {
                return node;
            }
            return null;
        }

        else {
            if (data < node.data) { // go on left subtree
                return findParent(node.left, data); 
            } else { // go on right subtree 
                return findParent(node.right, data);
            }
        }
    }

    // helper for deleteData
    private int findSmallest(Node root) {
        int min = root.data;
        while (root.left != null) {
            min = root.left.data;
            root = root.left;
        }
        return min;
    }

    // sum of values in given tree
    private int sumTree(Node root) {
        if (root == null) {
            return 0;
        }
        int sum = root.data;
        sum += (sumTree(root.right) + sumTree(root.left));
        return sum;
    }

    // count the number of nodes in given tree
    private int numNodes(Node root) {
        if (root == null) {
            return 0;
        }
        int nodes = 1;
        nodes += (numNodes(root.right) + numNodes(root.left));
        return nodes;
    }

    // count the number of branches in given tree
    private int numBranches(Node root) {
        if (root == null) {
            return 0;
        }
        return numNodes(root.right) + numNodes(root.left);
    }
    
    // count the number of nodes in given tree
    private int numLeaves(Node root) {
        if (root == null) {
            return 0;
        } else {
            if (root.left == null && root.right == null) {
                return 1;
            }
            int leaves = 0;
            leaves += (numLeaves(root.right) + numLeaves(root.left));
            return leaves;
        }
    }

    // find the height of a given tree
    private int findHeight(Node root) {
        if (root == null) {
            return 0;
        }
        return 1 + Math.max(findHeight(root.right), findHeight(root.left));
    }

    // check if a tree is full
    private boolean checkIfFull(Node root, int level, int height) {
        if (root == null) {
            return true;
        }
        if (root.left == null || root.right == null) {
            if (level == height) {
                return true;
            } else {
                return false;
            }
        }
        return (checkIfFull(root.left, level+1, height) && checkIfFull(root.right, level+1, height));
    }

    // check if a tree is balanced (sadly not time-efficient!)
    private boolean checkIfBalanced(Node root) {
        if (root.left == null && root.right == null) {
            return true;
        }
        else if (Math.abs(findHeight(root.left) - findHeight(root.right)) <= 1) {
            return (checkIfBalanced(root.left) && checkIfBalanced(root.right));
        } 
        return false;
    }

}
