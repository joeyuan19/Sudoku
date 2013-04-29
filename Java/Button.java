
import java.awt.*;

public class Button {
	int x, y, w, h;
	
	Color inactive = new Color(200,200,200);
	Color active = new Color(100,100,100);
	
	public Button (int x, int y,int w, int h) {
		this.x = x;
		this.y = y;
		this.w = w;
		this.h = h;
	} 
	
	
	public void draw(Graphics g, boolean mouseDown, int activeX, int activeY, boolean keyDown) {
		boolean clicked;
		
		if ( (activeX >= x && activeX <= x + w && activeY >= y && activeY <= y + h && mouseDown) || keyDown) {
			clicked = true;
		}
		else {
			clicked = false;
		}
		
		Color c = (clicked ? active : inactive);
		
		g.setColor(c);
		g.fillRect(x, y, w, h);
		
		g.setColor(Color.black);
		g.drawRect(x, y, w, h);
	}
	public void label(Graphics g, String s, Font font, int adjX, int adjY){
		g.setFont(font);
		g.setColor(Color.black);
		g.drawString(s, x + 5 + adjX, y + h - adjY);
	}
	public boolean behavior(int MouseX, int MouseY, int activeX, int activeY, boolean clickedUp, boolean keyUp) {
		boolean ActiveButton, hover;
		if (MouseX >= x && MouseX <= x + w && MouseY >= y && MouseY <= y + h) {
			hover = true;
		}
		else {
			hover = false;
		}
		if (activeX >= x && activeX <= x + w && activeY >= y && activeY <= y + h) {
			ActiveButton = true;
		}
		else {
			ActiveButton = false;
		}
		if ((hover && ActiveButton && clickedUp) || keyUp) {
			return true;
		}
		else {
			return false;
		}
	}
}
