import java.util.*;
import java.nio.file.*;
import java.io.FileWriter;
import java.io.FileNotFoundException;

/**
 * A Random Writer!
 * 
 * @author Sophia Shen
 */

public class RandomWriter {
    // --------------------------------------------------------------------
    // Random Writer Constructor
    // --------------------------------------------------------------------

    // Private State Variables
    private int k;
    private int length; 
    private String source;
    private String output;

    public RandomWriter(int k, int length, String source, String output) {
        this.k = k;
        this.length = length; 
        this.source = source;
        this.output = output;
    }


    // --------------------------------------------------------------------
    // Random Writer Public Methods
    // --------------------------------------------------------------------

    /**
     * Checks validity of the arguments. 
     * 
     * Returns system.err message if arguments aren't valid. 
     */
    public void checkValidity(int k, int length, String source, String result) {
    	// Check if k and length are non-negative
        if (k < 0 || length < 0) {
    		System.err.println("k and length must be non-negative!");;
    		System.exit(-1);
    	} 

        String data = "";
        String data2 = "";
        int sourceLength = 0;

        // Check if source can be opened for reading
        try {
            data = new String(Files.readAllBytes(Paths.get(source)));
            data.toCharArray();
            sourceLength = data.length();
        } catch (Exception e){
            System.out.println("Cannot read source!");
            e.printStackTrace();
        }

        // Check if result can be opened for writing
        // try {
        //     data2 = new String(Files.readAllBytes(Paths.get(result)));
        // } catch (Exception e){
        //     System.out.println("Cannot read result!");
        //     e.printStackTrace();
        // }

        // Make sure length of source > k
        if (sourceLength < k) {
            System.err.println("Source must contain more than k characters!");;
            System.exit(-1);
        }
    }


    /** 
	 * Opens the source and makes it a DLinkedList of as characters. 
	 * 
	 * @param source the file the data comes from
     * @return DLinkedList of data as characters
	 */ 
	public char[] openSource(String source){
		// Read in all chars from the file into a string. 
		// This requires catching any exceptions - won't compile otherwise
        String data = "";
	 	try {
	 		data = new String(Files.readAllBytes(Paths.get(source)));

	 	} catch (Exception e){
	 		e.printStackTrace();
	 	}

        char[] chars = data.toCharArray();
	 	return chars;
	}


    /**
     * Randomly generates the seed as a DLinkedList with length k
     * 
     * @param k the length of seed
     * @param data char array of data to generate seed from
     * @return DLinkedList of seed characters
     */
    public DLinkedListv2 chooseSeed(int k, char[] data) {
        String seedString = ""; // String version of seed
        Random rand = new Random(); // instance of Random class
        int indexStart = rand.nextInt(data.length); // random index to get seed

        // Add the subsequent character of string to seedString based off of indexStart
        for (int j = 0; j < k; j++) {
            seedString += data[indexStart+j];
        }
        
        // Convert seedString into a DLinkedList
        DLinkedListv2<Character> seedLL = new DLinkedListv2<>();
        for (int i = 0; i < seedString.length(); i++) {
            seedLL.insert(seedString.charAt(i), i);
        }

        return seedLL;
    }


    /**
     * Creates a DLinkedList of all the possible next characters after the seed!
     * 
     * @param seed - DLinkedList of characters for seed
     * @param data - char array of data to find next characters from
     * @return DLinkedList of all possible next characters
     */
	public DLinkedListv2 findOccurences(DLinkedListv2<Character> seed, char[] data) {
		DLinkedListv2<Character> nextCharacters = new DLinkedListv2<>();

		// Find each occurrence of seed in source using nested for loops
        for (int i = 0; i < data.length; i++) {
			if (data[i] == seed.get(0)) {
                boolean match = true;

                // Check that every succeeding character matches with seed
				for (int j = 0; j < seed.size(); j++) {
                    if ((i+j) > (data.length-1)) { // index is out of bounds
                        match = false;
                    } else if (seed.get(j) != null) {
                        if (data[i+j] != seed.get(j)) { 
                            match = false;
                        }
                    }
				}
                
                // If all the characters in the seed match with this occurence, add the next character to our DLinkedList
                if (match == true) {
                    Character nextChar = data[i+seed.size()];
                    nextCharacters.insert(nextChar, nextCharacters.size());
                }
			}
		}
        return nextCharacters;
	}


    /**
     * Chooses a character at random from the DLinkedList that holds the possible next characters
     * 
     * @param nextChars - DLinkedList of possible next characters
     * @return randomly chosen next character
     */
    public Character getNextChar(DLinkedListv2<Character> nextChars) {
        Random rand = new Random(); // instance of Random class
        int index = 0;

        // Generate a random index in between 0 and size - 1. So size is the upperbound
        if (nextChars.size() > 1) {
            index = rand.nextInt((nextChars.size()-1));
        } 
        Character nextChar = nextChars.get(index);
        return nextChar;
    }
}
