
public class Print{
	public Print(int[][] x){
	} 
	public static void main(String args[]){
		int[][] var;
		int[][][] p = {{{0},{2},{3},{4},{5},{6},{7},{8},{9}},
					   {{1},{0},{3},{4},{5},{6},{7},{8},{9}},
					   {{1},{2},{3},{4},{5},{6},{7},{8},{9}},
					   {{1},{2},{0},{4},{5},{6},{7},{8},{9}},
					   {{1},{2},{3},{0},{5},{6},{7},{8},{9}},
					   {{1},{2},{3},{4},{5},{6},{7},{8},{9}},
					   {{1},{2},{3},{4},{5},{6},{7},{8},{9}},
					   {{1},{2},{3},{4},{5},{6},{7},{8},{9}},
					   {{1},{2},{3},{4},{5},{6},{7},{8},{9}}};
		int[] x = {1,2,3,4,5,6,7,8,9};
		for (int i = 0; i < p.length; i++){
			for(int j = 0; j < p[0].length; j++){
				if (p[i][j][0] == 0){
					for (int k = 0; k < x.length; k++){
						p[i][j] = x;
					}
				}
			}
		}
		System.out.println(PrintPuzzle(p));
	}
	public static String PrintPuzzle(int[][][] puzzle){
		String linebreak = "+ - - - + - - - + - - - +";
		String s = "";
		String d = "";
		for (int i = 0; i < puzzle.length; i++){
			s += (i == 0 ?  linebreak +"\n" : (i%3 == 0 ? "|\n" + linebreak +"\n" : "|\n"));
			for(int j = 0; j < puzzle[0].length; j++){
				s+= (j%3 != 0 ? "" : "| ");
				if (puzzle[i][j].length == 1){
					s+= puzzle[i][j][0] + " ";
				}
				else {
					d = "{";
					for (int k = 0; k < puzzle[i][j].length; k++){
						d += puzzle[i][j][k] +  (k != puzzle[i][j].length - 1 ? ", " : "} ");
					}
					s+= d;
				}
			}
		}
		s += "|\n" + linebreak;
		return s;
	}
}
