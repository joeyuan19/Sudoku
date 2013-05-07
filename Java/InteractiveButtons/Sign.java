
package InteractiveButtons;

import java.awt.*;

public class Sign {
	protected int x, y, w, h;
	protected String s;
	
	protected Color inactive = new Color(200,200,200);
	
	
	public Sign(String s, int x, int y, int w, int h) {
		this.x = x;
		this.y = y;
		this.w = w;
		this.h = h;
		this.s = s;
	}
	public void draw(Graphics g, Font font, int adjX, int adjY) {
		g.setFont(font);
		g.setColor(inactive);
		g.fillRect(x, y, w, h);
		
		g.setColor(Color.black);
		g.drawRect(x, y, w, h);

		g.drawString(s, x + adjX, y + h - adjY);
	}
}
