import java.util.*;
import java.nio.file.*;
import java.io.FileWriter;
import java.io.FileNotFoundException;

/**
 * A class that tests our RandomWriter Methods!
 */

public class RandomWriterTester {
	public static void main(String[] args) {
		// int k = 25; // seed length
		// int length = 750;
		// String source = "alice.txt"; // alice.txt, janeausten.txt, hamlet.txt, or mobydick.txt
		// String result = "result.txt";
		int k = Integer.parseInt(args[0]); // seed length
		int length = Integer.parseInt(args[1]);
		String source = args[2]; // alice.txt, janeausten.txt, hamlet.txt, or mobydick.txt
		String result = args[3];

		RandomWriter writer = new RandomWriter(k, length, source, result);


		// --------------------------------------------------------------------
    	// Random Writer Tasks!
    	// --------------------------------------------------------------------
		
		writer.checkValidity(k, length, source, result);
		char[] data = writer.openSource(source);
		DLinkedListv2<Character> seed = writer.chooseSeed(k, data);
		DLinkedListv2<Character> currentSeed = seed; // size k

		// Result is the string to write into result.txt at the end! First add the seed to result string
		String resultString = "";
		for (int j = 0; j < seed.size(); j++) {
			resultString += seed.get(j);
		}

		// Adds the subsequent characters to resultString
		for (int i = 0; i < (length-k); i++) {
			DLinkedListv2<Character> nextChars = writer.findOccurences(currentSeed, data);
			Character nextChar = writer.getNextChar(nextChars);
			resultString += nextChar;

			// Update current seed
			if (nextChar != null) {
				currentSeed.remove(0);
				currentSeed.insert(nextChar, currentSeed.size()); // add the new character to end of currentSeed
			}
		}

		// Write resultString into result.txt
		try {
			// File name is built with date/time to differentiate different runs
			FileWriter outFile = new FileWriter(result);
			outFile.write(resultString);
			outFile.close();
		} catch (Exception e) {				// Something went wrong with the file writing
			System.out.println("Error!");
			e.printStackTrace();
		}
	}
}
