
package InteractiveButtons;

import java.awt.*;

public class Button {
	protected int x, y, w, h;
	
	protected Color inactive = new Color(200,200,200);
	protected Color active = new Color(100,100,100);
	
	boolean activeButton = false, clicked = false;
	boolean hover;
	
	String label;
	Font font;
	int adjX, adjY;
	
	public Button (int x, int y,int w, int h) {
		this.x = x;
		this.y = y;
		this.w = w;
		this.h = h;
	} 
	
	
	public void draw(Graphics g) {
		Color c = (clicked ? active : inactive);
		
		g.setColor(c);
		g.fillRect(x, y, w, h);
		
		g.setColor(Color.black);
		g.drawRect(x, y, w, h);
		
		g.setFont(font);
		g.setColor(Color.black);
		g.drawString(label, x + 5 + adjX, y + h - adjY);
	}
	public void label(String s, Font font, int adjX, int adjY){
		this.font = font;
		this.label = s;
		this.adjX = adjX;
		this.adjY = adjY;
	}
	public boolean behavior(int mouseX, int mouseY, int activeX, int activeY, boolean mouseDown, boolean clickedUp, boolean keyDown, boolean keyUp) {
		if ( (activeX >= x && activeX <= x + w && activeY >= y && activeY <= y + h && mouseDown) || keyDown) {
			
			clicked = true;
		}
		else {
			clicked = false;
		}
		if ( activeX >= x && activeX <= x + w && activeY >= y && activeY <= y + h ) {
			activeButton = true;
		}
		else {
			activeButton = false;
		}
		if (mouseX >= x && mouseX <= x + w && mouseY >= y && mouseY <= y + h) {
			hover = true;
		}
		else {
			
			hover = false;
		}
		if ((hover && activeButton && clickedUp) || keyUp) {
			return true;
		}
		else {
			return false;
		}
	}
}
