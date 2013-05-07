
import java.awt.*;

import InteractiveButtons.Button;
import InteractiveButtons.*;

public class Board {
	int x, y, w, h;
	int i, j;
	int activeFieldX = -1, activeFieldY = -1;
	Font font = new Font("Verdana", Font.BOLD, 20);
	String msg = "", errmsg = "";
	Puzzle p;
	EntryField[][] fields = new EntryField[9][9];
	Color background = new Color(0,150,150);
	Button solveButton;
	Button clearButton;
	Button generateButton;
	Slider diffSlider;
	double diff;

	public Board(int x, int y, int w, int h, Puzzle p){
		this.p = p;
		this.x = x;
		this.y = y;
		this.w = w;
		this.h = h;
		this.solveButton = new Button(x + w + 20, y,110,30);
		solveButton.label("Solve", font, 20, 6);
		this.clearButton = new Button(x + w + 20, y + 40,110,30);
		clearButton.label("Clear", font, 20, 6);
		this.generateButton = new Button(x + w + 20, y + 80,110,30);
		generateButton.label("Generate", font, 0, 6);
		this.diffSlider = new Slider(x + w + 20, y + 120, 110, 30);
		diffSlider.label("Difficulty", 20, 0);
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				fields[i][j] = new EntryField(x + 5 + j*50, y + 5 + i*50, 40, 40, p.getEntry(i,j));
			}	
		}
	}
	public void updateFields() {
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				fields[i][j].changeData( p.getEntry(i,j) );
			}
		}
	}
	public void clearFields() {
		p.clearPuzzle();
		updateFields();
	}
	public void draw(Graphics g){
		g.setColor(background);
		g.fillRect(x, y, w, h);

		g.setColor(Color.black);
		// Border
		g.drawRect(x-3,y-3,w+6,h+6);
		g.drawRect(x-2,y-2,w+4,h+4);
		g.drawRect(x,y,w,h);
		g.drawRect(x+1,y+1,w-2,h-2);
		g.drawRect(x+2,y+2,w-4,h-4);

		for (i = -1; i < 2; i++) {
			g.drawLine(x + w/3 + i, y, x + w/3 + i, y + h);
			g.drawLine(x + 2*w/3 + i, y, x + 2*w/3 + i, y + h);
			g.drawLine(x, y + h/3 + i, x + w, y + h/3 + i);
			g.drawLine(x, y + 2*h/3 + i, x + w, y + 2*h/3 + i);
		}

		updateFields();
		g.setFont(font);
		for (i = 0; i < 9; i++){
			for (j = 0; j < 9; j++){
				fields[i][j].draw(g);
			}
		}                     
		solveButton.draw(g);
		clearButton.draw(g);
		//generateButton.draw(g);
		//diffSlider.draw(g);


		g.setColor(Color.white);
		g.fillRect(x + w + 20, y + (2*h)/3, 90, 120);
		g.setColor(Color.black);
		g.drawRect(x + w + 20, y + (2*h)/3, 90, 120);
		g.drawRect(x + w + 19, y + (2*h)/3 - 1, 92, 122);
		g.drawRect(x + w + 17, y + (2*h)/3 - 3, 96, 126);
		g.drawLine(x + w + 20, y + (2*h)/3 + 30, x + w + 110, y + (2*h)/3 + 30);
		g.drawLine(x + w + 20, y + (2*h)/3 + 60, x + w + 110, y + (2*h)/3 + 60);
		g.drawLine(x + w + 20, y + (2*h)/3 + 90, x + w + 110, y + (2*h)/3 + 90);
		g.drawLine(x + w + 50, y + (2*h)/3, x + w + 50, y + (2*h)/3 + 90);
		g.drawLine(x + w + 80, y + (2*h)/3, x + w + 80, y + (2*h)/3 + 90);

		g.setFont(font);
		for (i = 0; i < 3; i++) {
			for (j = 0; j < 3; j++) {
				g.drawString("" + ( (j+1) + 3*i ), x + w + 20 + j*30 + 8, y + (2*h)/3 + (i+1)*30 - 7);
			}
		}

		g.drawString("empty", x + w + 31, y + (2*h)/3 + 112);
		g.drawString(msg, x + w + 25, y + 220);
		g.drawString(errmsg, x + w + 25, y + 240);
	}
	public void behavior(int mouseX, int mouseY, int activeX, int activeY, boolean mouseDown, boolean wasMouseDown, boolean clickedUp, boolean clickedDown, boolean sDown, boolean sUp, boolean cDown, boolean cUp) {
		if (solveButton.behavior(mouseX, mouseY, activeX, activeY, mouseDown, clickedUp, sDown, sUp) ) {
			msg = p.solve();
			errmsg = p.getErrorMsg();
		}
		if (clearButton.behavior(mouseX, mouseY, activeX, activeY, mouseDown, clickedUp, cDown, cUp) ) {
			clearFields();
		}
		/*
		diff = diffSlider.behavior(mouseX, activeX, activeY, clickedUp, clickedDown, wasMouseDown, mouseDown);
		
		if (generateButton.behavior(mouseX, mouseY, activeX, activeY, mouseDown, clickedUp, cDown, cUp) ) {
			p.generatePuzzle( );
		}
		*/
		
		if (clickedDown) {
			for (i = 0; i < 9; i++) {
				for (j = 0; j < 9; j++) {
					if ( fields[i][j].isOver(activeX, activeY) ) {
						fields[i][j].highlight();
						activeFieldX = i;
						activeFieldY = j;
					}
				}
			}
		}
		if (activeFieldX != -1 && activeFieldY != -1) {
			fields[activeFieldX][activeFieldY].highlight();
			for (i = 0; i < 9; i++) {
				for (j = 0; j < 9; j++) {
					if ( activeFieldX != i || activeFieldY != j ) {
						fields[i][j].unhighlight();
					}
				}
			}

			for (i = 0; i < 3; i++) {
				for (j = 0; j < 3; j++) {
					// ( , ,  - 7
					if ( activeX >= x + w + 20 + j*30 && activeX <= x + w + 20 + (j+1)*30 && activeY >= y + (2*h)/3 + i*30  && activeY <= y + (2*h)/3 + (i+1)*30 ) {
						p.setEntry((j+1) + 3*i, activeFieldX, activeFieldY);
						fields[activeFieldX][activeFieldY].unhighlight();
						activeFieldX = -1;
						activeFieldY = -1;
					}
				}
			}
			if (activeX >= x + w + 20 && activeX <= x + w + 110 && activeY >= y + (2*h)/3 + 90  && activeY <= y + (2*h)/3 + 120 ) {
				p.setEntry(0, activeFieldX, activeFieldY);
				fields[activeFieldX][activeFieldY].unhighlight();
				activeFieldX = -1;
				activeFieldY = -1;
			}
		}

	}
}
