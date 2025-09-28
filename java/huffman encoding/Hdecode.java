import java.util.*;
import java.nio.file.*;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;


public class Hdecode {
	String filename; 
	FileReader fileInput;
	int letter;

	public Hdecode(String filename){
		this.filename = filename;
		try {
			fileInput = new FileReader(filename);
			letter = fileInput.read();
			decode();
			fileInput.close();
		} catch (IOException e) {
			System.out.println("An error occurred.");
      		e.printStackTrace();
		}
		
	}
 
	public void decode() throws IOException {
		// Get length
		int length = 0;
		while ((char) letter != 'I') {
			length  = (10 * length) + ((char) letter - '0');
			read();
		}

		// Build the Huffman tree
		Hnode root = buildTree();
		
		// Get the binary bits
		String bits = getBits();

		// Decode the binary bits based on Huffman tree
		String txt = getCharacters(bits, root, length);

		// Write to new file
		try {
      		FileWriter myWriter = new FileWriter(filename.substring(0, filename.length() - 4));
      		myWriter.write(txt);
      		myWriter.close();
      		System.out.println("Successfully wrote to " + filename.substring(0, filename.length() - 4));
    	} catch (IOException e) {
      		System.out.println("An error occurred.");
      		e.printStackTrace();
    	}

    	// Delete the original file
    	Files.delete(Paths.get(filename));
	}

	public static void main(String[] args) {
		Hdecode huff = new Hdecode(args[0]);
	}

	// build the Huff tree based on the preorder traversal in file
	private Hnode buildTree() throws IOException{
		if (letter == 'L') {
			Hnode h = new Hnode((char) read());
			read();
			return h;
		}
		read();
		return new Hnode(buildTree(), buildTree());
	}
	
	// get the binary bits associated to the ascii characters in the file
	private String getBits() throws IOException {
		String bits = ""; 

		while (letter != -1) {
			// System.out.println(letter);
			bits += binarify(((int) letter));
			read();
		}

		return bits;
	}

	private String binarify(int n) { 
		String binary = "";

		while (n > 0) {
			binary = (n % 2) + binary;
			n /= 2;
		}

		while (binary.length() < 8) {
			binary = "0" + binary;
		}
		return binary;
	}

	private String getCharacters(String bits, Hnode root, int length) {
		int i = 0;
		String text = "";
		Hnode current = root;

		while (i < bits.length() && text.length() < length) {
			if (current.left == null && current.right == null) {
				text += current.data;
				current = root;
			} else {
				if (bits.charAt(i) == '0') {
					current = current.left;
				} else {
					current = current.right;
				}
				i++;
			}
		}
		return text;
	}
	
	// Prints tree on its side, root on the left.
    // right to left inorder traversal
    private void printTree(Hnode tree, int depth) {
        if (tree == null){
            return;
        }
        printTree(tree.right, depth + 1);   // Right side printed on top

        for (int i = 0; i < depth; i++){    // Manage indentations
            System.out.print("   ");
        }
        System.out.println(tree);      // Current data
        printTree(tree.left, depth + 1);    // Left side on bottom
    }

    // reads the next letter from the file
    private int read() throws IOException {
		return letter = fileInput.read();
	}

	/**
	 * INTERNAL DATA STRUCTURES:
	 * 	- Hnode: represents a node in a Huffman Tree
	 */ 

	//Q: How is a node for a huffman tree different from a regular binary tree?
	//A: We have one piece of data - a character
	private class Hnode {
		char data; // Not private - so we can directly access the ivars elsewhere in Hencode
		Hnode left, right;

		public Hnode(Hnode l, Hnode r) {
			left = l;
			right = r;
		}
		public Hnode(char d) {
			data = d;
			right = null;
			left = null;
		}

		public String toString() {
			return "|" + data + "|";
		}
	}
}
