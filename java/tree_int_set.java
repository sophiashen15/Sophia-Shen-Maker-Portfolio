import java.util.*;
import java.lang.Math.*;
/*
 * In this implementation of IntSet, all items are stored in a integer binary search tree.
 * 
 * The effiency of each method is as follows:
 *      add is O(log(n))  
 *      contains is O(log(n)) 
 *      remove is O(log(n))  (to find the index of the element)
 *      size is O(1)
 */
public class TreeIntSet implements IntSet {
    private int size;
    private IntBinarySearchTree tree;

    /**
     * Construct an empty set.
     */
    public TreeIntSet() {
        size = 0;
        tree = new IntBinarySearchTree();
    }

    /**
     * Adds an element to the set, ensuring no duplicate elements are added.
     * 
     * @param element - the item to add to the set
     * @return  - true if element was added, false if it already existed.
     */ 
    public boolean add(int element) {
        if(contains(element)) {
            return false;
        }
        tree.insert(element);
        size++;
        return true;
    }

    /**
     * Returns the index of the element, -1 if the element does not exist in the set
     * 
     * @param element - item to look for
     * @return  - index of element or -1 if it does not exist
     */ 
    public boolean contains(int element) {
        return (tree.find(element));
    }

    /**
     * Removes element from set if it exists in the set already
     * 
     * @param element - Item to remove from the set
     * @return  - true if element was removed, false if it did not exist in the set
     */ 
    public boolean remove(int element) {
        // Return false if element not in the set.
        if (!(contains(element))) {
            return false;
        }
        else {
            tree.delete(element);
            size--;
            return true;
        }
    }

    /**
     * @return  - the number of elements currently in the set
     * 
     * This is NOT the same as the length of the underlying array structure
     */ 
    public int size() {
        return size;
    }
}  
