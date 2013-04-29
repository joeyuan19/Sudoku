
import java.awt.*;

public class PuzzleEntry {
	
	int[] var = new int[9];
	
	{
		for (int i = 1; i <= 9; i++) {
			var[i] = i;
		}
	}
	
	int entry = 0;
	boolean empty = true;
	
	int x, y, w, h;
	
	public PuzzleEntry(int x, int y, int w, int h) {
		this.x = x;
		this.y = y;
		this.w = w;
		this.h = h;
	}
	public void setEntry(int entry){
		this.entry = entry;
	}
	public boolean isEmpty() {
		return empty;
	}
	public void eliminateVariables(int num){
		var[num - 1] = 0;
	}
	public int[] getVar() {
		return var;
	}
	public boolean checkVariable(int num) {
		if (var[num - 1] == 0) {
			return false;
		}
		else {
			return true;
		}
	}
	public void reset() {
		empty = true;
		entry = 0;
		for (int i = 1; i <= 9; i++) {
			var[i] = i;
		}
	}
	public String toString() {
		if (entry != 0)	
			return entry + "";
		else 
			return "";
	}
	public int getValue() {
		return entry;
	}
	public void draw(Graphics g) {
		
	}
}
