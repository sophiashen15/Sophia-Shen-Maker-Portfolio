import java.util.*;  

public class DArray {
	private double[] array;
	private int size;
	private int capacity;

	/**
     * Constructs an empty DArray
     * 
     */	
	public DArray() {
		size = 0;
		capacity = 4;
		array = new double[capacity];
	}


    /**
     * Returns the size of the DArray
     * 
     * @return size of the DArray
     */
	public int size() {
		return size;
	}


	 /**
     * Adds an element at index in the DArray
     * 
     */
	public void add(int index, double element) {
		size += 1;

		if (size > capacity) { // Check if the capacity needs to be adjusted
			capacity *= 2;
			double[] newArray = new double[capacity]; // New array with x2 capacity

			for (int i = 0; i <= size - 1; i++) {
				if (i < index) {
					newArray[i] = array[i];
				} else if (i > index) {
					newArray[i] = array[i - 1];
				} else if (i == index) {
					newArray[i] = element;
				}
			}
			array = newArray;

		} else {
			// Changing our array without creating a new array! 
			for (int i = capacity - 1; i >= 0; i--) {
				if (index < i) {
					array[i] = array[i - 1];
				} else if (index == i) {
					array[i] = element;
				} 
			}
		}
	}


	/**
     * Returns the element at index in the DArray
     * 
     */
	public double get(int index) {
		return array[index];
	}


	/**
     * Set an index as an element in the DArray
     * 
     */
	public void set(int index, double element) {
		array[index] = element;
	}


	/**
     * Removes an element at index in the DArray
     * 
     */
	public void remove(int index) {
		size -= 1;

		// Changing our array without creating a new array! 
		for (int i = 0; i <= size; i++) {
			if (index <= i) {
				array[i] = array[i + 1];
			} 
		}
	}

}
