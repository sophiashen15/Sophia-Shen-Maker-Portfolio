import java.util.*;


/**
 * A singly-linked list of integers.
 *
 * @author Sophia Shen
 */
public class IntLinkedList {
    // --------------------------------------------------------------------
    // Private classes
    // --------------------------------------------------------------------

    // Data-only class to store Nodes. Only accessible within IntLinkedList.
    private class Node {
        public int value;
        public Node next;
        public Node(int value, Node next) {
            this.value = value;
            this.next = next;
        }
    }

    // --------------------------------------------------------------------
    // Private state variables
    // --------------------------------------------------------------------
    private Node head;
    private int size;
    
    // --------------------------------------------------------------------
    // Public methods
    // --------------------------------------------------------------------

    /**
     * Construct an empty list.
     */
    public IntLinkedList() {
        head = null;
        size = 0;
    }

    /**
     * Construct a list from a given array of values. 
     * 
     * @param  inputArray  array of values to be used to construct the list
    */
    public IntLinkedList(int[] inputArray) {
        if (inputArray.length == 0) {
            head = null;
            size = 0;

        } else {
            head = new Node(inputArray[0], null);
            Node current = head;
            size = inputArray.length;

            for (int i = 1; i < inputArray.length; i++) {
                current.next = new Node(inputArray[i], null);;
                current = current.next;
            }
        }
    }

    /**
     * Print the list to the screen.
     * 
     * The format is as follows: "1, 2, 35, 12, "
     */
    public void display() {
        if (head == null) {
            System.out.println("Null");
        }

        else {
            for (Node n = head; n != null; n = n.next) {
                System.out.print(n.value);
                System.out.print(", ");
            }
            System.out.println();
        }
    }

    /**
     * Asks the user for a string containing a list to replace the
     * current list.
     * 
     * The prompt will look like:
     * <pre>
     * Enter a list of numbers, separated by commas:
     * > </pre>
     * The input should include integers separated by commas. Spacing
     * does not matter.
     * 
     * The program will crash if the user messes up. This is only
     * meant for flawless users.
     */
    public void inputList() {
        Scanner reader = new Scanner(System.in);
        System.out.println("Enter a list of numbers, separated by commas:");
        System.out.print("> ");  // print prompt
        String input = reader.nextLine();
        // strip spaces
        input.replaceAll("\\s+", "");
        // split on commas
        String[] numbersAsStrings = input.split(",");
        // convert to integers
        int[] numbers = new int[numbersAsStrings.length];
        for (int i = 0; i < numbersAsStrings.length; i++) {
            numbers[i] = Integer.parseInt(numbersAsStrings[i]);
        }
        
        IntLinkedList newIntLinkedList = new IntLinkedList(numbers);
        // newIntLinkedList.display();
    }

    /**
     * Inserts an item at the specified location.
     * 
     * @param  index  the location to insert the new item within range of linked list. 
     * @param  value  the value of the new item
     * @throws NoSuchElementException - If the index is not found  

     */
    public void insert(int value, int index) {
        if (index <= size) {
            size++;
            if (index == 0) {
                head = new Node(value, head);
            }

            else {
                Node current = head;
                for (int i = 0; i < (index-1); i++) {
                    current = current.next;
                }
                current.next = new Node(value, current.next);
            }   
        }
        else {
            throw new NoSuchElementException(); 
        }
    }

    /**
     * Removes the item at the specified location.
     * 
     * @param  index  the location to item to remove within range of linked list
     * @return  the value of the removed item
     * @throws NoSuchElementException - if the index is not found
     */
    public int remove(int index) {
        if (index > size) {
            throw new NoSuchElementException();
        }
        
        else if (index == 0) {
            size--;
            int removedValue = head.value;
            head = head.next;
            return removedValue;
        } 

        else {
            size--;
            Node current = head;
            int removedValue = 0;

            for (int i = 0; i < (index-1); i++) {
                current = current.next;
            }

            removedValue = current.next.value;
            current.next = current.next.next;
            return removedValue;
        }
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
     * Returns the cumulative sum at each point in the calling list.
     * 
     * Returns a new list containing the cumulative sums. The
     * calling list is not modified.
     * 
     * @return  a new list in which the kth item is the sum of the
     *          first k items of the calling list
     */
    public IntLinkedList cumulativeSum() {
        if (head == null) {
            IntLinkedList newLL = new IntLinkedList();
            return newLL;
        } 

        else {
            Node current = head;
            int sum = current.value;

            int[] inputArray = new int[size]; 
            inputArray[0] = sum; // Store the first sum in array
            int i = 1; // Index of the array to add 

            while (current.next != null) {
                current = current.next;
                sum += current.value; 
                inputArray[i] = sum;
                i += 1;
            }

            IntLinkedList listSum = new IntLinkedList(inputArray); 
            return listSum;
        }
    }

    /**
     * "Deals" an array of lists using elements from this list.
     * 
     * Creates numHands lists of size handSize using the first
     * numHands * handSize items of this list. For example, if
     * numHands is 3 and handSize is 4, then the first item in the
     * returned array of lists will contain <1st item of this list,
     * 4th item, 7th item, 10th item>. The items "dealt" to the
     * returned lists will be removed from the calling list.
     * 
     * @param  numHands  number of new lists to return 
     * @param  handSize  the size of each new list to return with numHands * handSize <= size
     * @return  array of length numHands each containing handSize
     *          items originating from the calling list
     * @throws IllegalArgumentException - If numHands * handSize is > size
     */
    public IntLinkedList[] deal(int numHands, int handSize) {
        Node current = head;
        Node finalCurrent = null;

        if (numHands < 0 || handSize < 0) {
            throw new IllegalArgumentException();
        }
        
        if (size() < numHands * handSize) {
            throw new IllegalArgumentException();
        }
        
        if (numHands == 0) {
            IntLinkedList[] newIntLinkedList = new IntLinkedList[0];
            return newIntLinkedList;
        }


        IntLinkedList[] outputList = new IntLinkedList[numHands];
        if (size() > numHands || size() == handSize) {
            for (int n = 0; n < numHands; n++) {
                IntLinkedList elementN = new IntLinkedList();
                outputList[n] = elementN;
            }
            
            
            for (int i = 0; i < handSize; i++) {
                for(int j = 0; j < numHands; j++) {
                    outputList[j].insert(current.value, i);
                    current = current.next;
                    if (j+1 == numHands && i+1 == handSize) {
                         finalCurrent = current;
                    }
                }
            }
            if (handSize != 0) {
               head = finalCurrent; 
            }
        }
        
        return outputList;
    }
    

    /**
     * Shuffle the given list into the calling list.
     * 
     * The new list will alternate between those of this list and
     * otherList: <first node of this list, first node of otherList, second
     * node of this list, second node of otherList, ... >. If one list runs
     * out of items early, the rest of the items will all come from the
     * other list.
     * 
     * @param  otherList  the list to be shuffled into this one
     */
    public void shuffleWith(IntLinkedList otherList) {
        Node current1 = head;
        Node current2 = otherList.head;

        if (head == null) {
            head = otherList.head;
            otherList.head = null;
        }

        while (current1 != null && current2 != null) {
            Node card1 = null;
            Node card2 = null;

            card1 = current1.next;
            card2 = current2.next;
            current1.next = current2;

            if (card1 != null) {
               current2.next = card1; 
            }
            current2 = card2;
            current1 = card1;
            otherList.head = null;
        }
        if (current2 != null && current1 == null) {
            current1 = current2;
            current2 = null;
        }
    }


    /**
     * Reverses the order of the list.
     */
    public void reverse() {
        Node previous = null;
        Node current = null;
        Node next = head;

        while (next != null) {
            previous = current;
            current = next;
            next = next.next;
            current.next = previous;
        }
        head = current;
    }
    
    // --------------------------------------------------------------------
    // Private methods
    // --------------------------------------------------------------------

    // Hint: You will need at least one to avoid repeating code!

}
