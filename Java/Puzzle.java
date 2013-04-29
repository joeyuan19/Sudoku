
public class Puzzle {
	
	int[][] entries = new int[9][9];
	
	public Puzzle(int[][] initial) {
		this.entries = initial;
	}
	
	
	public int getEntry(int i, int j){
		return entries[i][j];
	}
}
