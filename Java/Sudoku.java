
import java.awt.*;
import InteractiveButtons.*;
import InteractiveButtons.Button;

public class Sudoku extends BufferedApplet{
	private static final long serialVersionUID = 1L;
	
	public Sudoku(){
	}
	
	int w, h;
	Color background = new Color(0,175,0);
	
	Puzzle p = new Puzzle(); 
	int[][] puzzle = new int[9][9];
	
	Board board = new Board(10,10,450,450, p);
	
	boolean clickedUp, clickedDown, sUp, sDown, cUp, cDown;
	int activeX, activeY;
	
	public void render(Graphics g){
		animating = true;
		
		w = getWidth();
		h = getHeight();
		
		clickedDown = ! wasMouseDown &&   mouseDown;
		clickedUp   =   wasMouseDown && ! mouseDown;
		
		sDown = ! wasKeyDown['s'] &&   keyDown['s'];
		sUp   =   wasKeyDown['s'] && ! keyDown['s'];
		
		cDown = ! wasKeyDown['c'] &&   keyDown['c'];
		cUp   =   wasKeyDown['c'] && ! keyDown['c'];
		
		if (clickedDown) {
			requestFocusInWindow();
			activeX = mouseX;
			activeY = mouseY;
		}
		
		
		g.setColor(background);
		g.fillRect(0, 0, w, h);
		
		board.draw(g);
		board.behavior(mouseX, mouseY, activeX, activeY, mouseDown, wasMouseDown, clickedUp, clickedDown, sDown, sUp, cDown, cUp);
		
		if (clickedUp) {
			activeX = -1;
			activeY = -1;
		}
	}
}
