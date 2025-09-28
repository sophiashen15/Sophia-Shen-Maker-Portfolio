import java.util.*;
import java.lang.Math.*;
/*
 * In this implementation of IntSet, all items are stored in a mod table.
 * 
 * The effiency of each method is as follows:
 *      add is O(1)  
 *      contains is O(1) 
 *      remove is O(1)
 *      size is O(1)
 */
public class ModTableIntSet implements IntSet {
    private int size;
    private TreeIntSet[] array;
    private int modulus;

    /**
     * Construct an empty set.
     */
    public ModTableIntSet(int modulus) {
        size = 0;
        array = new TreeIntSet[modulus];

        for (int i = 0; i < modulus; i++) {
            TreeIntSet treeSet = new TreeIntSet();
            array[i] = treeSet;
        }

        this.modulus = modulus;
    }

    /**
     * Adds an element to the set, ensuring no duplicate elements are added.
     * 
     * @param element - the item to add to the set
     * @return  - true if element was added, false if it already existed.
     */ 
    public boolean add(int element) {
        TreeIntSet tree = getTree(element);
        if(tree.contains(element)) {
            return false;
        }
        tree.add(element);
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
        TreeIntSet tree = getTree(element);
        return (tree.contains(element));
    }

    /**
     * Removes element from set if it exists in the set already
     * 
     * @param element - Item to remove from the set
     * @return  - true if element was removed, false if it did not exist in the set
     */ 
    public boolean remove(int element) {
        TreeIntSet tree = getTree(element);
        if (!(tree.contains(element))) {
            return false;
        }
        else {
            tree.remove(element);
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

    private TreeIntSet getTree(int element) {
        if (element%modulus >= 0) {
            return array[element%modulus];
        }
        else {
            return array[modulus + (element%modulus)];
        }
    }
}
