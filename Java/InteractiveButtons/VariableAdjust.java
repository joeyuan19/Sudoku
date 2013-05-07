
package InteractiveButtons;

import java.awt.*;
import java.text.*;

public class VariableAdjust extends Slider {
	private int x, y, w, h;
	private Font font;
	private NumberFormat format = new DecimalFormat("##.000#");


	public VariableAdjust(int x, int y, int w, int h) {
		super(x,y,w,h);
	}
	{
	this.x = getx();
	this.y = gety();
	this.w = getw();
	this.h = geth();
	Font font = new Font("Verdana", Font.BOLD, h/2 - 5);
	this.font = font;
	}
	public void resetSlider() {
		this.slideX = slideMin - slideW/2;
	}
	public void label(Graphics g, String var, double m, String units, int adj) {
		g.setColor(Color.black);
		g.setFont(font);
		String s = format.format(m); 
		
		g.drawString( var + ": " + s, x + 5, y + h/2 - 5);
		g.drawString(units, x + w - adj, y + h/2 - 5);
	}
	
}
