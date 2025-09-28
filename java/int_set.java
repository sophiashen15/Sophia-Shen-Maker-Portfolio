import java.util.*;

/**
 * An IntSet is a set of integers.
 * 
 * When implementing an IntSet, any constructors provided must create a set that
 * contains no duplicate elements.
 */
public interface IntSet extends Iterable<Integer> {
    
    /**
     * Adds the specified element to this set if it is not already present.
     * 
     * If this set already contains the element, the call leaves the set unchanged and
     * returns false. In combination with the restriction on constructors, this ensures
     * that sets never contain duplicate elements.
     * 
     * @param  element  number to be added to this set, if not already present
     * 
     * @return  true if this set did not already contain the specified element
     */
    boolean add(int element);

    /**
     * Returns true if this set contains the specified element.
     * 
     * @param  element  number whose presence in this set is to be tested
     * 
     * @return  true if this set contains the specified element
     */
    boolean contains(int element);

    /**
     * Removes the specified element from this set if it is present.
     * 
     * @param  element  number to be removed from this set, if present
     * 
     * @return  true if this set contained the specified element
     */
    boolean remove(int element);

    /**
     * Returns the number of elements in this set.
     * 
     * @return  the number of elements in this set
     */
    int size();


    /**
     * Adds all elements of otherSet to this set if not already present.
     * 
     */
    default void union(IntSet otherSet) {
        for (Integer item : otherSet) {
            if (! contains(item)) {
                add(item);
            }
        }
    }

    /**
     * Remove all elements of this set that are not in otherSet.
     * 
     */
    default void intersection(IntSet otherSet) {
        int[] unwanted = new int[this.size()]; // items we don't want in our set
        int index = 0;

        // Add all the unwanted items into the arraylist
        for (Integer item : this) {
            if (! otherSet.contains(item)) {
                unwanted[index] = item;
                index++;
            }
        }

        for (int i = 0; i < unwanted.length; i++) {
            this.remove(unwanted[i]);
        }
    }

    /**
     * Returns true if this set contains all elements of otherSet.
     * 
     */
    default boolean subset(IntSet otherSet) {
        for (Integer item : otherSet) {
            if (! contains(item)) {
                return false;
            }
        }
        return true;
    }

    /**
     * Compares the specified object with this set for equality. 
     * 
     */
    default boolean equals(IntSet otherSet) {
        Iterator<Integer> iter = this.iterator();
        Iterator<Integer> otherIter = otherSet.iterator();

        // Test if our set is a subset of otherSet
        while (iter.hasNext()) {
            if (! otherSet.contains(iter.next())) {
                return false;
            }
        }

        // Test if otherSet is a subset of our set
        while (otherIter.hasNext()) {
            if (! this.contains(otherIter.next())) {
                return false;
            }
        }

        return true;
    }
}
