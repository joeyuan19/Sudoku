public class Puzzle {
	int i, j, k;

	int[][][] vars;
	int[][] puzzle;

	ListNode failsafe;

	String errmsg;

	int updateCount;

	public Puzzle() {
		this.vars = new int[9][9][9];
		this.puzzle = new int[9][9];
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				puzzle[i][j] = 0;
				for (k = 1; k < 10; k++) {
					vars[i][j][k - 1] = k;
				}
			}
		}
		this.failsafe = new ListNode(puzzle, null);
	}

	public Puzzle(int[][] puzzle) {
		this.vars = new int[9][9][9];
		this.puzzle = new int[9][9];
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				this.puzzle[i][j] = puzzle[i][j];
				for (k = 1; k < 10; k++) {
					if (puzzle[i][j] == 0) {
						vars[i][j][k - 1] = k;
					} else {
						vars[i][j][k - 1] = 0;
					}
				}
			}
		}
		this.failsafe = new ListNode(puzzle, null);
	}

	public void clearPuzzle() {
		int i, j, k;
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				this.puzzle[i][j] = 0;
				for (k = 1; k < 10; k++) {
					vars[i][j][k - 1] = k + 1;
				}
			}
		}
		this.failsafe = new ListNode(puzzle, null);
	}

	public void resetPuzzle(int[][] puzzle) {
		int i, j, k;
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				this.puzzle[i][j] = puzzle[i][j];
				for (k = 1; k < 10; k++) {
					if (puzzle[i][j] == 0) {
						vars[i][j][k - 1] = k;
					} else {
						vars[i][j][k - 1] = 0;
					}
				}
			}
		}
		this.failsafe = new ListNode(puzzle, null);
	}

	public int getEntry(int x, int y) {
		return puzzle[x][y];
	}

	public void setEntry(int data, int x, int y) {
		this.puzzle[x][y] = data;
		resetVars();
	}

	public String getErrorMsg() {
		return errmsg;
	}

	public String solve() {
		if (error()) {
			return "Error in entry:";
		}
		int[][][] prevVars = new int[9][9][9];
		int[] minCoords;
		copyArray(vars, prevVars);
		//updateCount = 0;
		long t0 = System.currentTimeMillis();
		while (!isSolved()) {
			copyArray(vars, prevVars);
			update();
			if (!changeMade(prevVars, vars)) {
				bruteforce();
			}
			if (failsafe.getSize() > 1 && (error() || bruteforceError())) {
				for (i = 0; i < 9; i++) {
					for (j = 0; j < 9; j++) {
						puzzle[i][j] = failsafe.data[i][j];
					}
				}
				resetVars();
				failsafe = failsafe.next;
				minCoords = findMinVars();
				for (k = 0; k < 9; k++) {
					if (vars[minCoords[0]][minCoords[1]][k] != 0) {
						vars[minCoords[0]][minCoords[1]][k] = 0;
						break;
					}
				}
			}
		}
		return "Solved in:" + (System.currentTimeMillis() - t0) / 1000.0
				+ " sec";
	}

	public boolean isSolved() {
		int i, j;
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				if (puzzle[i][j] == 0) {
					return false;
				}
			}
		}
		return true;
	}

	public boolean error() {
		errmsg = "";
		int i, j, k;
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				if (puzzle[i][j] != 0) {
					for (k = 0; k < 9; k++) {
						if (k != i && puzzle[i][j] == puzzle[k][j]) {
							errmsg = "Repeated " + puzzle[i][j] + " in column "
									+ (j + 1);
							return true;
						}
						if (k != j && puzzle[i][j] == puzzle[i][k]) {
							errmsg = "Repeated " + puzzle[i][j] + " in row "
									+ (i + 1);
							return true;
						}
					}
				}
			}
		}
		box();
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				if (puzzle[i][j] != 0) {
					for (k = 0; k < 9; k++) {
						if (j != k && puzzle[i][j] == puzzle[i][k]) {
							errmsg = "Repeated " + puzzle[i][j] + " in ";
							switch (i) {
							case 0:
								errmsg += "top left";
								break;
							case 1:
								errmsg += "top center";
								break;
							case 2:
								errmsg += "top right";
								break;
							case 3:
								errmsg += "center left";
								break;
							case 4:
								errmsg += "center";
								break;
							case 5:
								errmsg += "center right";
								break;
							case 6:
								errmsg += "bottom left";
								break;
							case 7:
								errmsg += "bottom center";
								break;
							case 8:
								errmsg += "bottom right";
								break;
							}
							errmsg += " box";
							box();
							return true;
						}
					}
				}
			}
		}
		box();
		return false;
	}

	public boolean bruteforceError() {
		int i, j, k;
		int count;
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				if (puzzle[i][j] == 0) {
					count = 0;
					for (k = 0; k < 9; k++) {
						if (vars[i][j][k] != 0) {
							count++;
						}
					}
					if (count == 0) {
						return true;
					}
				}
			}
		}
		return false;
	}

	public void resetVars() {
		int i, j, k;
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				for (k = 0; k < 9; k++) {
					if (puzzle[i][j] == 0) {
						vars[i][j][k] = k + 1;
					} else {
						vars[i][j][k] = 0;
					}
				}
			}
		}
		updateVars();
	}

	public void copyArray(int[][][] a, int[][][] b) {
		int i, j, k;
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				for (k = 0; k < 9; k++) {
					b[i][j][k] = a[i][j][k];
				}
			}
		}
	}

	public boolean changeMade(int[][][] before, int[][][] after) {
		int i, j, k;
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				for (k = 0; k < 9; k++) {
					if (before[i][j][k] != after[i][j][k]) {
						return true;
					}
				}
			}
		}
		return false;
	}

	public void update() {
		updatePuzzle();
		resetVars();
		updateForSingles();
		resetVars();
	}

	public void updateVars() {
		int temp, itr;
		int i, j;
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				if ((temp = puzzle[i][j]) != 0) {
					for (itr = 0; itr < 9; itr++) {
						vars[i][itr][temp - 1] = 0;
						vars[itr][j][temp - 1] = 0;
					}
				}
			}
		}
		box();
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				if ((temp = puzzle[i][j]) != 0) {
					for (itr = 0; itr < 9; itr++) {
						vars[i][itr][temp - 1] = 0;
					}
				}
			}
		}
		box();
		return;
	}

	public void updatePuzzle() {
		int count;
		int i, j, k;
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				if (puzzle[i][j] == 0) {
					count = 0;
					for (k = 0; k < 9; k++) {
						if (vars[i][j][k] != 0) {
							count++;
						}
						if (count > 1) {
							break;
						}
					}
					if (count == 1) {
						for (k = 0; k < 9; k++) {
							if (vars[i][j][k] != 0) {
								puzzle[i][j] = k + 1;
								vars[i][j][k] = 0;
								break;
							}
						}
					}
				}
			}
		}
	}

	public void updateForSingles() {
		int i, j, k;
		int[] varCount = new int[9];
		for (k = 0; k < 9; k++) {
			varCount[k] = 0;
		}
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				if (puzzle[i][j] == 0) {
					for (k = 0; k < 9; k++) {
						if (vars[i][j][k] != 0) {
							varCount[k]++;
						}
					}
				}
			}
			for (k = 0; k < 9; k++) {
				if (varCount[k] == 1) {
					for (j = 0; j < 9; j++) {
						if (vars[i][j][k] != 0) {
							puzzle[i][j] = k + 1;
							break;
						}
					}
				}
			}
		}
		for (k = 0; k < 9; k++) {
			varCount[k] = 0;
		}
		for (j = 0; j < 9; j++) {
			for (i = 0; i < 9; i++) {
				if (puzzle[i][j] == 0) {
					for (k = 0; k < 9; k++) {
						if (vars[i][j][k] != 0) {
							varCount[k]++;
						}
					}
				}
			}
			for (k = 0; k < 9; k++) {
				if (varCount[k] == 1) {
					for (i = 0; i < 9; i++) {
						if (vars[i][j][k] != 0) {
							puzzle[i][j] = k + 1;
							break;
						}
					}
				}
			}
		}
		for (k = 0; k < 9; k++) {
			varCount[k] = 0;
		}
		box();
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				if (puzzle[i][j] == 0) {
					for (k = 0; k < 9; k++) {
						if (vars[i][j][k] != 0) {
							varCount[k]++;
						}
					}
				}
			}
			for (k = 0; k < 9; k++) {
				if (varCount[k] == 1) {
					for (j = 0; j < 9; j++) {
						if (vars[i][j][k] != 0) {
							puzzle[i][j] = k + 1;
							break;
						}
					}
				}
			}
		}
		box();
	}

	public void box() {
		int[][] boxPuzz = new int[9][9];
		int[][][] boxVars = new int[9][9][9];
		int i, j, k;
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				if (i < 3) {
					if (j < 3) {
						boxPuzz[0][j % 3 + 3 * (i % 3)] = puzzle[i][j];
						for (k = 0; k < 9; k++) {
							boxVars[0][j % 3 + 3 * (i % 3)][k] = vars[i][j][k];
						}
					} else if (3 <= j && j < 6) {
						boxPuzz[1][j % 3 + 3 * (i % 3)] = puzzle[i][j];
						for (k = 0; k < 9; k++) {
							boxVars[1][j % 3 + 3 * (i % 3)][k] = vars[i][j][k];
						}
					} else {
						boxPuzz[2][j % 3 + 3 * (i % 3)] = puzzle[i][j];
						for (k = 0; k < 9; k++) {
							boxVars[2][j % 3 + 3 * (i % 3)][k] = vars[i][j][k];
						}
					}
				} else if (3 <= i && i < 6) {
					if (j < 3) {
						boxPuzz[3][j % 3 + 3 * (i % 3)] = puzzle[i][j];
						for (k = 0; k < 9; k++) {
							boxVars[3][j % 3 + 3 * (i % 3)][k] = vars[i][j][k];
						}
					} else if (3 <= j && j < 6) {
						boxPuzz[4][j % 3 + 3 * (i % 3)] = puzzle[i][j];
						for (k = 0; k < 9; k++) {
							boxVars[4][j % 3 + 3 * (i % 3)][k] = vars[i][j][k];
						}
					} else {
						boxPuzz[5][j % 3 + 3 * (i % 3)] = puzzle[i][j];
						for (k = 0; k < 9; k++) {
							boxVars[5][j % 3 + 3 * (i % 3)][k] = vars[i][j][k];
						}
					}
				} else {
					if (j < 3) {
						boxPuzz[6][j % 3 + 3 * (i % 3)] = puzzle[i][j];
						for (k = 0; k < 9; k++) {
							boxVars[6][j % 3 + 3 * (i % 3)][k] = vars[i][j][k];
						}
					} else if (3 <= j && j < 6) {
						boxPuzz[7][j % 3 + 3 * (i % 3)] = puzzle[i][j];
						for (k = 0; k < 9; k++) {
							boxVars[7][j % 3 + 3 * (i % 3)][k] = vars[i][j][k];
						}
					} else {
						boxPuzz[8][j % 3 + 3 * (i % 3)] = puzzle[i][j];
						for (k = 0; k < 9; k++) {
							boxVars[8][j % 3 + 3 * (i % 3)][k] = vars[i][j][k];
						}
					}
				}
			}
		}
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				puzzle[i][j] = boxPuzz[i][j];
				for (k = 0; k < 9; k++) {
					vars[i][j][k] = boxVars[i][j][k];
				}
			}
		}
		return;
	}

	public int[] findMinVars() {
		int count, minCount = 10, minX = -1, minY = -1;
		int[] coords = new int[2];
		int i, j, k;
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				if (puzzle[i][j] == 0) {
					count = 0;
					for (k = 0; k < 9; k++) {
						if (vars[i][j][k] != 0) {
							count++;
						}
					}
					if (count == 2) {
						coords[0] = i;
						coords[1] = j;
						return coords;
					}
					if (count < minCount) {
						minX = i;
						minY = j;
						minCount = count;
					}
				}
			}
		}
		coords[0] = minX;
		coords[1] = minY;
		return coords;
	}

	public void generatePuzzle() {
		clearPuzzle();
		int count;
		int[] tempVars = new int[9];
		int i, j, k;
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				count = 0;
				for (k = 0; k < 9; k++) {
					if (vars[i][j][k] != 0) {
						tempVars[count] = k + 1;
						count++;
					}
				}
				puzzle[i][j] = tempVars[(int) (count * Math.random())];
				resetVars();
			}
		}
		return;
		/*
		 * i = 0; for (k = 0; k < 60; k++) { i += k%(60/9); j = (int)
		 * (9*Math.random()); while (puzzle[i][j] == 0) {
		 * System.out.println("stuck"); i = (int) (9*Math.random()); j = (int)
		 * (9*Math.random()); } puzzle[i][j] = 0; }
		 */
	}

	public void bruteforce() {
		int[][] puzzleCopy = new int[9][9];
		int i, j, k;
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				puzzleCopy[i][j] = puzzle[i][j];
			}
		}
		failsafe = new ListNode(puzzleCopy, failsafe);
		int[] minCoords = findMinVars();
		for (k = 0; k < 9; k++) {
			if (vars[minCoords[0]][minCoords[1]][k] != 0) {
				// System.out.println(vars[minCoords[0]][minCoords[1]][k]);
				puzzle[minCoords[0]][minCoords[1]] = k + 1;
				while (k < 9) {
					vars[minCoords[0]][minCoords[1]][k] = 0;
					k++;
				}
				break;
			}
			vars[minCoords[0]][minCoords[1]][k] = 0;
		}
	}

	public String toString() {
		String s = "";
		int i, j;
		for (i = 0; i < 9; i++) {
			if (i % 3 == 0) {
				s += "+ - - - + - - - + - - - +\n";
			}
			s += "|";
			for (j = 0; j < 9; j++) {
				s += ((j != 0 && j % 3 == 0) ? " |" : "") + " " + puzzle[i][j];
			}
			s += " |\n";

		}
		return s + "+ - - - + - - - + - - - +\n";
	}

	public String varsToString() {
		String s = "";
		int i, j, k;
		for (i = 0; i < 9; i++) {
			if (i % 3 == 0) {
				s += "+ - - - + - - - + - - - +\n";
			}
			s += "|";
			for (j = 0; j < 9; j++) {
				s += ((j != 0 && j % 3 == 0) ? " |" : "") + " [ ";
				for (k = 0; k < 9; k++) {
					s += (vars[i][j][k] != 0 ? vars[i][j][k] + " " : "");
				}
				s += "]";
			}
			s += " |\n";

		}
		return s + "+ - - - + - - - + - - - +\n";
	}

	public static void main(String args[]) {
		int[][] puzzle = { { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
				{ 0, 0, 0, 0, 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
				{ 0, 0, 0, 0, 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
				{ 0, 0, 0, 0, 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
				{ 0, 0, 0, 0, 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 0, 0, 0, 0, 0 } };
		Puzzle p = new Puzzle(puzzle);
		System.out.println(p + p.varsToString());
		p.solve();
		System.out.println(p + p.varsToString());
	}
}
