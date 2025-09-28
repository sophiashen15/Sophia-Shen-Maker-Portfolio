import java.util.*;

/*
 * In this implementation of IntSet, all items are stored in an unordered array.
 * 
 * The effiency of each method is as follows:
 *      add is O(n)  (to make sure it isn't a duplicate)
 *      contains is O(n)
 *      remove is O(n)  (to find the index of the element)
 *      size is O(1)
 */
public class UnorderedArrayIntSet implements IntSet {
    private int[] data;
    private int size;
    
    /**
     * Construct an empty set.
     */
    public UnorderedArrayIntSet() {
        size = 0;
        data = new int[10];
    }

    /**
     * Adds an element to the set, ensuring no duplicate elements are added.
     * 
     * @param element - the item to add to the set
     * @return  - true if element was added, false if it already existed.
     */ 
    public boolean add(int element) {
        if (contains(element)) {  // Don't add if it already exists
            return false;
        }

        // Double size of underlying array if needed.
        if (size == data.length) {
            int[] copy = data;
            data = new int[size * 2];

            // Copy data back into original array
            for (int i = 0; i < size; i++) {
                data[i] = copy[i];
            }
        }
        
        data[size] = element;  // Insert new element
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
        return (findIndex(element) != -1);
    }

    /**
     * Removes element from set if it exists in the set already
     * 
     * @param element - Item to remove from the set
     * @return  - true if element was removed, false if it did not exist in the set
     */ 
    public boolean remove(int element) {
        // See if the element is in the set.
        int indexOfElement = findIndex(element);
        
        // Return false if element not in the set.
        if (indexOfElement == -1) {
            return false;
        }
        
        // Otherwise replace this element with last element and return true.
        data[indexOfElement] = data[size - 1];
        size--;
        return true;
    }

    /**
     * @return  - the number of elements currently in the set
     * 
     * This is NOT the same as the length of the underlying array structure
     */ 
    public int size() {
        return size;
    }
    
    // Return index of the element, or -1 if not found.
    private int findIndex(int element) {
        for (int i = 0; i < size; i++) {
            if (data[i] == element) {
                return i;       // Found it!
            }
        }
        return -1;  // Not found
    }
}
