bimport java.util.*;

/**
 * A doubly-linked list of any data type T.
 *
 * @author Sophia Shen
 */
public class DLinkedList<T> {
	// --------------------------------------------------------------------
    // Private classes
    // --------------------------------------------------------------------

    // Data-only class to store Nodes. Only accessible within DLinkedList.
    private class Node {
    	public Node prev;
        public T value;
        public Node next;
        public Node(Node prev, T value, Node next) {
        	this.prev = prev;
            this.value = value;
            this.next = next;
        }
    }

    // --------------------------------------------------------------------
    // Private state variables
    // --------------------------------------------------------------------
    private Node head;
    private Node tail;
    private int size;

    // --------------------------------------------------------------------
    // Public methods
    // --------------------------------------------------------------------

    /**
     * Construct an empty list.
     */
    public DLinkedList() {
        head = new Node(null, null, null);
        tail = new Node(head, null, null);
        head.next = tail;
        size = 0;
    }

     /**
     * Construct a list from a given array of values. 
     * 
     * @param  inputArray  array of values to be used to construct the list
    */
    public DLinkedList(T[] inputArray) {
        head = new Node(null, null, null);
        tail = new Node(head, null, null);
       	head.next = tail;
       	size = inputArray.length;

        Node current = head;
        for (int i = 0; i < inputArray.length; i++){
           	current = new Node(current, inputArray[i], current.next);
           	current.prev.next = current;
            current.next.prev = current;
        }
    }


    /**
     * Returns/prints the list to the screen. 
     * 
     * Format: "1, 2, 35, 12, "
     * 
     * @return printed list 
	*/
    public String toString() {
    	String outputString = "";
    	Node current = head.next;

        for (int i = 0; i < size; i++) {
            outputString += current.value;
            outputString += ", ";
            current = current.next;
        }

        return outputString;
    }


    /**
     * Returns/prints the list reversed. 
     * 
     * Format: "1, 2, 35, 12, "
     * 
     * @return printed reversed list 
	*/
   	public String toReverseOrderString() {
   		String outputString = "";
   		Node current = tail.prev;

   		for (int i = 0; i < size; i++) {
   			outputString += current.value;
   			outputString += ", ";
   			current = current.prev;
   		}
   		
   		return outputString;
   	}

    /**
     * Returns the number of items in the list.
     * 
     * @return  the number of items in the list
     */
    public int size() {
        return size; 
    }

    /**
     * Returns the value of item at index.
     * 
     * @param  index  the location to get the value of and item. 
     * @return  value of item at index. 
     * @throws NoSuchElementException - if the index is not found
     */
    public T get(int index) {
        if (index > size || index < 0) {
            throw new NoSuchElementException();
        }
        else {
            Node current = head.next;
            for (int i = 0; i < index; i++) {
                current = current.next;
            }

            return current.value;
        }
    }


    /**
     * Inserts an item at index with value.
     * 
     * @param  index  the location to insert the new item within range of linked list. 
     * @param  value  the value of the new item
     * @throws NoSuchElementException - if the index is not found  

     */
    public void insert(T value, int index) {
        if (index > size || index < 0) {
            throw new NoSuchElementException();
        }
        else {
            size++;

            if (index == 0) {
                Node newHead = new Node(head, value, head.next);
                head.next.prev = newHead;
                head.next = newHead;
            }

            else {
                Node current = head.next;
                for (int i = 0; i < (index-1); i++) {
                    current = current.next;
                }
                Node newNode = new Node(current, value, current.next);
                current.next.prev = newNode;
                current.next = newNode;
            }
        }
    }


    /**
     * Removes the item at specified index.
     * 
     * @param  index  the location to item to remove within range of linked list
     * @return  the value of the removed item
     * @throws NoSuchElementException - if the index is not found
     */
    public T remove(int index) {
        if (index > size || index < 0) {
            throw new NoSuchElementException();
        }
        else {
            size--;

            if (index == 0) {
                T removedValue = head.next.value;
                head.next = head.next.next;
                head.next.prev = head; // I also used a drawing to figure this out!
                return removedValue;
            }

            else {
                Node current = head.next;
                T removedValue = null;

                for (int i = 0; i < (index-1); i++) {
                    current = current.next;
                }

                removedValue = current.next.value;
                current.next = current.next.next;
                current.next.prev = current; // I used a drawing to figure this out :)
                return removedValue;
            }
        }
    }

    // --------------------------------------------------------------------
    // Linked List Iterator
    // --------------------------------------------------------------------
    
    /**
     * Makes an iterator starting from head.
     */
    public LLIterator iteratorFromHead() {
        return new LLIterator(true);
    }

    /**
     * Makes an iterator starting from tail.
     */
    public LLIterator iteratorFromTail() {
        return new LLIterator(false);
    }

    public class LLIterator {
        private Node next;  // accessed next time next() is called
        private Node prev;  // accessed next time previous() is called
        // the last node to be returned by previous() or next()
        // this is set to null if remove() or insert() is called
        private Node lastAccessed;

        // Private constructor ensures that you can only make an Iterator
        // using the outer class's method.
        private LLIterator(boolean startsAtHead) {
            if (startsAtHead) {
                next = head.next;
                prev = head;
            } else {
                next = tail;
                prev = tail.prev;
            }
            lastAccessed = null;
        }

        // --------------------------------------------------------------------
        // Iterator Public Methods
        // --------------------------------------------------------------------

        /**
         * Returns true if there is an element in front of the iterator.
         */
        public boolean hasPrevious() {
            return (prev != head);
        }

        /**
         * Returns true if there is an element behind the iterator.
         */
        public boolean hasNext() {
            return (next != tail);
        }

        /**
         * Returns the next value and advances the iterator forward.
         * 
         * @return the next value 
         * @throws NoSuchElementException - if there is no next element.
         */     
        public T next() {
            if (next == tail) {
                throw new NoSuchElementException();
            }

            prev = next;
            next = next.next;
            lastAccessed = prev;
            return lastAccessed.value;
        }

        /**
         * Returns the previous value and advance the iterator backward.
         * 
         * @return the previous value 
         * @throws NoSuchElementException - if there is no previous element.
         */
        public T previous() {
            if (prev == head) {
                throw new NoSuchElementException();
            }

            next = prev;
            prev = prev.prev;
            lastAccessed = next;
            return lastAccessed.value;
            
        }

        /**
         * Changes the value last accessed by next() or previous() to newValue. 
         * (Not valid if remove or insert has been called since the last call to next() or previous()). 
         * 
         * @throws IllegalStateException - if there is no last-accessed element to modify.
         */
        public void set(T newValue) {
            if (lastAccessed == null) {
                throw new IllegalStateException();
            }
            lastAccessed.value = newValue;
        }

        /**
         * Removes the last value last accessed by next() or previous() from the list. 
         * (Not valid if remove or insert has been called since the last call to next() or previous()). 
         * 
         * @throws IllegalStateException - if there is no last-accessed element to remove.
         */
        public void remove() {
            if (lastAccessed == null) {
                throw new IllegalStateException();
            }

            lastAccessed.prev.next = lastAccessed.next;
            lastAccessed.next.prev = lastAccessed.prev;
            lastAccessed = null;
        }

        /**
         * Inserts a new element with value newValue in between the previous and next elements. 
         * The iterator now points in between the new element and the next element. 
         * 
         */
        public void insert(T newValue) {
            Node newNode = new Node(prev, newValue, next);
            prev.next = newNode;
            next.prev = newNode;

            // Set the iterator between new and next
            prev = newNode;
        }
    }
}
