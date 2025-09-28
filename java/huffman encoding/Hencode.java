import java.util.*;
import java.nio.file.*;
import java.io.FileInputStream;
import java.io.File;  // Import the File class
import java.io.FileWriter;  
import java.io.IOException;  // Import the IOException class to handle errors


// Stub code for beginning of Huffman.
// Complete a few key aspects together, then individually complete the rest.

public class Hencode {

	//Q: How do we create counts of all chars in the file?
	//A:
	private String file;
	private int[] counts;
	private String text;
	private String[] codes;
	private FileWriter myWriter;

	public Hencode(String file){
		this.file = file;
		counts = new int[256]; // keep track of how many times each character is written
		text = "";
		codes = new String[256];

		try {
			myWriter = new FileWriter(file + ".huf");
		} catch(IOException e) {
			System.out.println("An error occurred.");
      		e.printStackTrace();
		}
	}


	/**
	 * 	Precondition: All instance variables have been initialized.
	 * 	Postcondition: File has been compresssed through Huffman encoding and written to an output file:
	 * 		If input filename is: myfile.txt, 
	 * 			compressed file is written to myfile.txt.huf
	 */ 
	public void encode() { 
		fillCountsArray(); // read the file

		// Make the Priqueue
		Priqueue p = buildInitialQueue(); 

		// Create the Huffman tree & get its preorder traversal string
		Hnode h = buildHuffmanTree(p); 
		String treeStr = preorderString(h);

		// Get the corresponding ASCII codes and then bits for each letter
		getCodes(h, ""); // fill the String[] codes with ____
		int[] asciiSeq = getBitSequence(codes);

		// Write to new file and delete the original
		writeToFile(asciiSeq, treeStr);
    }


	public static void main(String[] args) {
		Hencode huff = new Hencode(args[0]);
		huff.encode();
	}

	// Assumes that file is a String instance variable representing the name of the file to compress
	private void fillCountsArray(){

		try{
			
			FileInputStream fileInput = new FileInputStream(file);	
			int letter;

			while ((letter = fileInput.read()) != -1) { // while we have not reached the end of the file
				text += (char)letter;
				counts[letter]++;

			}
			fileInput.close();

		} catch (Exception e){	
			System.out.println("File: " + file + " was not found.");
			e.printStackTrace();
		}
	}

	// Q: How do we build the initial pqueue of hnodes?
	// A: Check for each element in counts. If it isn't 0, make it an Hnode and put it in the Priqueue
	private Priqueue buildInitialQueue(){
		Priqueue p = new Priqueue(new HnodeComparator());

		for (int i = 0; i < counts.length; i++) {
			if (counts[i] != 0){
				Hnode h = new Hnode((char) i, counts[i]);
				p.insert(h);
			}
		}
		// System.out.println(p);
		return p;
	}

	// Prints tree on its side, root on the left.
    // right to left inorder traversal
    private void printTree(Hnode tree, int depth) {
        
        if (tree == null){
            return;
        }
        printTree(tree.getRight(), depth + 1);   // Right side printed on top

        for (int i = 0; i < depth; i++){    // Manage indentations
            System.out.print("   ");
        }   
        System.out.println(tree);      // Current data
        printTree(tree.getLeft(), depth + 1);    // Left side on bottom
    }


	// Build the Huffman tree from the priqueue of hnodes.
	private Hnode buildHuffmanTree(Priqueue q){
		while (q.size() > 1) {
			Hnode l = q.remove();
			Hnode r = q.remove();

			// Combine the 2 nodes and add it to the priqueue
			Hnode h = buildTree(l, r);
			q.insert(h);
			// System.out.println(q);
		}
		return q.remove(); // return the root
	}


	// Helper method for building Huffman tree 
	private Hnode buildTree(Hnode root1, Hnode root2){
		Hnode root = new Hnode('\0', 0); // makes empty Hnode 

		root.setLeft(root1); // left is smallest Hnode 
		root.setRight(root2); // right is second smallest Hnode
		root.setCount(root.getLeft().getCount() + root.getRight().getCount()); // sum of 2 minimum counts
		
		return root;
	}

	// Update codes (String[]) to hold the corresponding binary strings for each ASCII character
	private void getCodes(Hnode h, String str) {
    	if (h.getLeft() == null && h.getRight() == null){ // you get a leaf
    		codes[(int) h.getData()] = str;
    		return;
    	}
    	getCodes(h.getLeft(), str + "0");
    	getCodes(h.getRight(), str + "1");
    }

    // Using bit shifting to get int from binary
	private int getAsciiInt(String s) {
		int total = 0;
		for (int i = 0; i < s.length(); i++) {
			total <<= 1;
			if (s.charAt(i) == '1') {
				total += 1;
			}
        }
        return total;
    }
    
    // If the length of the binary string is not div by 8, add 0s to the end
    private String applyPadding(String s) {
    	if ((s.length() % 8)== 0) {
    		return s;
    	} else {
    		while (s.length() % 8 != 0) {
    			s += "0";
    		}
    		return s;
    	}
    }

    private int[] getBitSequence(String[] codes) {
    	String seq = "";

    	// Get the binary strings for each letter in file in order
    	for (int i = 0; i < text.length(); i++) {
    		seq += codes[(int) (text.charAt(i))];
    	}

    	// add 0s if the length is not div by 8
    	seq = applyPadding(seq);

    	// create an int[] of int corresponding to ascii charas
    	int[] ascii = new int[(seq.length() / 8)];
    	int index = 0;

    	for (int j = 0; j < seq.length(); j += 8) {
    		String sub = seq.substring(j, j+8); // get groups of 8 binary bits
    		ascii[index] = getAsciiInt(sub); // convert to int 
    		index++;
    	}
    	return ascii;
    }

    
    // Internal node if it has at least one child. 
    // Preorder is root left right
    private String preorderString(Hnode h) {
    	if (h == null) {
    		return "";
    	}

    	// If you are at a leaf
    	if (h.getLeft() == null && h.getRight() == null) {
    		return "L" + h.getData();
    	} 

    	// If you are at a "root" then go left then right
    	return "I" + preorderString(h.getLeft()) + preorderString(h.getRight());
    }
    
    private void writeToFile(int[] ascii, String tree) {
    	try {
      		// 1) the length of the file
      		myWriter.write("" + text.length()); 

      		// 2) the tree preorder traversal
      		myWriter.write(tree);

      		// 3) the bit sequence
        	for (int x : ascii) {
				myWriter.write((char)x); // write the ascii char corresponding to each int
			}
			
      		myWriter.close();
      		System.out.println("Successfully wrote to the new file: " + file + ".huf");
      		
      		Files.delete(Paths.get(file));
      		System.out.println("Successfully deleted original file: " + file);
    	} catch (IOException e) {
      		System.out.println("An error occurred.");
      		e.printStackTrace();
    	}
    	
    }

}
