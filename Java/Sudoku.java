
import java.awt.*;

public class Sudoku extends BufferedApplet{
	private static final long serialVersionUID = 1L;
	
	public Sudoku(){
	}
	
	int[][] puzzle = 
			{{2, 0, 0, 0, 0, 0, 0, 0, 5},
		   	 {0, 1, 0, 0, 2, 0, 8, 3, 0},
		   	 {4, 8, 9, 3, 6, 5, 0, 2, 0},
		   	 {6, 0, 8, 7, 0, 0, 0, 0, 9},
		   	 {0, 4, 0, 0, 0, 0, 0, 1, 0},
		   	 {5, 0, 0, 0, 0, 2, 6, 0, 3},
		   	 {0, 5, 0, 2, 3, 4, 9, 6, 1},
		   	 {0, 9, 2, 0, 5, 0, 0, 7, 0},
		   	 {3, 0, 0, 0, 0, 0, 0, 0, 8}};
	int[][][] variables = setVariables(puzzle); 
	int[][] x = Box(puzzle);
	int w, h;
	int i;
	{i = 0;}
	Color background = new Color(0,175,0);

	Button box = new Button(500,50,50,50);
	
	Puzzle p = new Puzzle(puzzle); 
	
	Board board = new Board(10,10,450,450, p);
	
	boolean clickedUp, clickedDown, bUp, bDown;
	int activeX, activeY;
	
	public void render(Graphics g){
		w = getWidth();
		h = getHeight();
		
		clickedDown = ! wasMouseDown && mouseDown;
		clickedUp =  wasMouseDown && ! mouseDown;
		
		bDown = ! wasKeyDown['b'] && keyDown['b'];
		bUp =  wasKeyDown['b'] && ! keyDown['b'];
		
		if (clickedDown) {
			activeX = mouseX;
			activeY = mouseY;
		}
		
		g.setColor(background);
		g.fillRect(0, 0, w, h);
		
		board.draw(g);
		board.update(p);
		box.draw(g, mouseDown, activeX, activeY, bDown);
		if (i == 1000){
			System.out.println("should be boxing");
			puzzle = box(puzzle);
		}
		if (keyDown['s'] && ! wasKeyDown['s']){
			Solve(puzzle);
		}
		System.out.println(i++);
		animating = true;
	}
}
