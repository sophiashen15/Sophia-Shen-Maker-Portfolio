import java.util.*;

public class HnodeComparator implements Comparator<Hnode>{
	
	public int compare(Hnode a, Hnode b) {
		if (a.getCount() > b.getCount()) {
			return 1;
		} else if (a.getCount() < b.getCount()) {
			return -1;
		} else {
			return 0;
		}
	}
}
