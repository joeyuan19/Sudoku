
package InteractiveButtons;

import java.awt.*;

public class Slider {

	protected int x, y, w, h, slideW, slideH, slideMax;
	protected int slideMin;
	protected int slideLength, gap, c;
	protected boolean sliderClicked, clicked;
	protected int slideX, slideY;

	protected Color inactive = new Color(200,200,200);
	protected Color inactive2 = new Color(150,150,150);
	protected Color active = new Color(100,100,100);
	protected Font font;
	protected String label = "";
	protected boolean hasLabel = false;
	protected int adjX = 0, adjY = 0;

	public Slider(int x, int y, int w, int h) {
		this.x = x;
		this.y = y;
		this.w = w;
		this.h = h;
		this.gap = w/40;
		this.slideW = w/10 - gap/5;
		this.slideH = h/2 - gap;
		this.slideMax = x + w - (slideW/2 + gap);
		this.slideMin = x + (slideW/2 + gap);
		this.slideLength = slideMax - slideMin;
		this.slideX = x + gap + 4*slideLength/9;
		this.slideY = y + gap + slideH;
		this.sliderClicked = false;
		this.font = new Font("Verdana", Font.PLAIN, h/2);
	}
	public int getx(){
		return x;
	}
	public int gety(){
		return y;
	}
	public int getw(){
		return w;
	}
	public int geth(){
		return h;
	}
	public void draw(Graphics g) {
		if (sliderClicked) {
			clicked = true;
		}
		else {
			clicked = false;
		}
		Color c = (clicked ? active : inactive2);
		
		g.setColor(inactive);
		g.fillRect(x,y,w,h);
		g.setColor(Color.black);
		g.drawRect(x,y,w,h);
		
		g.drawLine(slideMin, slideY + slideH/2, slideMax, slideY + slideH/2);
		
		g.setColor(c);
		g.fillRect((int)slideX, slideY, slideW, slideH);
		g.setColor(Color.black);
		g.drawRect((int)slideX, slideY, slideW, slideH);
		
		if (hasLabel) {
			g.setFont(font);
			g.drawString(label, x + gap + adjX, y + h/2 - gap/2 + adjY);
		}
	}
	public void label(String label, int adjX, int adjY) {
		this.label = label;
		this.adjX = adjX;
		this.adjY = adjY;
		this.hasLabel = true;
	}
	public double behavior(int mouseX, int activeX, int activeY, boolean clickedUp, boolean clickedDown, boolean wasMouseDown, boolean mouseDown) {
		if (activeX >= slideMin - slideW/2 && activeX <= slideMax + slideW/2 && activeY >= slideY && activeY <= slideY + slideH && clickedDown) {
			sliderClicked = true;
		}
		else if (clickedUp) {
			sliderClicked = false;
		}
		if (sliderClicked && mouseDown && wasMouseDown) {
			int _mouseX = (mouseX < slideMin ? slideMin : mouseX > slideMax ? slideMax : mouseX);
			this.slideX = _mouseX - slideW/2;
		}
		
		return ((double) ((slideX + slideW/2)-slideMin) )/((double) slideLength);
	}
}
