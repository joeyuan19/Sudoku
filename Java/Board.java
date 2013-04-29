
import java.awt.*;

public class Board {
	int x, y, w, h;
	
	Font font = new Font("Verdana", Font.BOLD, 20);
	Puzzle p;
	
	public Board(int x, int y, int w, int h, Puzzle p){
		this.p = p;
		this.x = x;
		this.y = y;
		this.w = w;
		this.h = h;
	}
	int[] X = {x, x+w, x+w,   x, x, x+3, (x+w) - 3, (x+w) - 3,    x  - 3, x - 3, x};
	int[] Y = {y,   y, y+h, y+h, y, y+3,    y  - 3, (y+h) - 3, (y+h) - 3, y - 3, y};
	
	
	public void update(Puzzle p) {
		this.p = p;
	}
	
	public void draw(Graphics g){
		g.setColor(Color.white);
		g.fillRect(x, y, w, h);
		
		g.setColor(Color.black);
		g.setFont(font);
		// Border
		g.drawRect(x-3,y-3,w+6,h+6);
		g.drawRect(x-2,y-2,w+4,h+4);
		g.drawRect(x,y,w,h);
		g.drawRect(x+1,y+1,w-2,h-2);
		g.drawRect(x+2,y+2,w-4,h-4);
		
		for (int i = 0; i < 9; i++){
			for (int j = 0; j < 9; j++){
				if (p.getEntry(i,j) != 0){
					g.drawString(p.getEntry(i,j) + "", x + i*(w/9) + 20, y + 35 + j*(h/9));
				}
				else {
					g.drawString("", x + i*(w/9) + 20, y + 35 + j*(h/9));
				}
			}
			
			if (i >= 1){
				if (i%3 == 0){
					// Creates Boxes
					g.fillRect((x + i*w/9) - 1, y + 2, 3, h - 4);
					g.fillRect(x + 2, (y + i*w/9) - 1, w - 4, 3);
				}
				else {
					// "Thin" Lines
					g.drawLine(x + i*w/9, y + 2, x + i*w/9, y + h - 2);
					g.drawLine(x + 2, y + i*w/9, x + w - 2, y + i*w/9);
				}
			}
		}                                                                                                                                                                                                    
	}
}
