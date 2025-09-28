import java.util.*;

public class Priqueue {

    private int size;
    private Hnode[] data;
    private Comparator<Hnode> comp;

    public Priqueue(Comparator<Hnode> comparator) {
   	 comp = comparator;
   	 size = 0;
   	 data = new Hnode[300];
    }

    @Override
    public String toString() {
   	 String s = "";
   	 for(int i = 0; i < size; i++){
   		 s += data[i].toString() + ", ";
   	 }
   	 return s;
    }

    public int size(){
   	 return size;
    }


    /**
     * Insert an item into the min-heap, maintaining min-heap order
     */
    public void insert(Hnode item) {
       data[size] = item;
       reheapUp(size);
       size++;
    }


    /**
     * Remove root from the min-heap, maintaining min-heap order
     */
    public Hnode remove() {
       // Remove root
       Hnode removed = data[0];
       data[0] = data[size-1]; // Place the last item at root
       data[size-1] = null;
       size--;

       // Reheap down from the root
       reheapDown(0);
       return removed;
    }


    // Swap two nodes
    private void swap(int pos1, int pos2) {
   	 Hnode el = data[pos1];
   	 data[pos1] = data[pos2];
   	 data[pos2] = el;
    }


    // Arithmetic to find the correct index for the relative
    private int left(int pos) { 
       return (2*pos + 1);
    }

    private int right(int pos) { 
       return (2*pos + 2);
    }

    private int parent(int pos) { 
       return (pos - (2 - (pos % 2))) / 2;
    }


    // Fix heap order after inserting an element at the bottom of 
    // the min-heap - move it up until it is in order
    private void reheapUp(int pos) {

       // Continue until the new element’s parent is <= to the new element, or the new element reaches the root
   	 while (pos > 0 && comp.compare(data[pos], data[parent(pos)]) == -1) {
          swap(pos, parent(pos));
          pos = parent(pos);
       }
    }


    // Fix heap order after removing root from the min-heap.
    // Continually swaps node at pos with its child if the
    // child is smaller than the node at pos
    private void reheapDown(int pos) {
       int smallest = pos;

       // if the left value is smaller than pos value
       if (left(pos) < size && comp.compare(data[smallest], data[left(pos)]) == 1) {
          smallest = left(pos);
       }

       // if the right value is smaller than the "smallest" value
       if (right(pos) < size && comp.compare(data[smallest], data[right(pos)]) == 1) {
          smallest = right(pos);
       }

       // if no leaves exist or already in min heap order, do nothing
       if (smallest == pos) {
         return;
       }

       // recurse!
       swap(pos, smallest);
       reheapDown(smallest);
    }
}
