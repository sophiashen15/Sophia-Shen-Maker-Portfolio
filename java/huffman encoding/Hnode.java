public class Hnode{
	private char data; // Not private - so we can directly access the ivars elsewhere in Hencode
	private int count;
	private Hnode left, right;

	public Hnode(char d, int c){
		data = d;
		count = c;
		right = null;
		left = null;
	}

	public String toString(){
		return "|" + data + ":" + count + "|";
	}

	// Accessors
	public char getData(){
		return data;
	}

	public int getCount(){
		return count;
	}

	public Hnode getLeft(){
		return left;
	}

	public Hnode getRight(){
		return right;
	}

	// Setters
	public void setCount(int c){
		count = c;
	}
	
	public void setLeft(Hnode h){
		left = h;
	}

	public void setRight(Hnode h){
		right = h;
	}
}
