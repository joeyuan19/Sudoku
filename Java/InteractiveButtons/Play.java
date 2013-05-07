
package InteractiveButtons;

import java.awt.*;

public class Play extends Button{
	protected int rectw, recth, gap, xMid;
	int[] triX, triY;
	
	
	public Play(int x, int y, int w, int h) {
		super(x,y,w,h);
		this.rectw = 2*w/3;
		this.recth = 2*h/3;
		this.gap = (h - rectw)/2;
		this.xMid = (x + w/2);
		int[] triX = {xMid - rectw/2, xMid + rectw/2, xMid - rectw/2};
		int[] triY = {y + gap, y + h/2, y + h - gap};
		this.triX = triX;
		this.triY = triY;
	}
	public void Icon(Graphics g, boolean play) {
		
		
		if (! play) {
			g.setColor(Color.green);
			g.fillPolygon(triX,triY,3);
			
			g.setColor(Color.black);
			g.drawPolygon(triX,triY,3);
		}
		else {
			g.setColor(Color.yellow);
			g.fillRect(xMid - rectw/2, y + gap, rectw/2 - gap/2, rectw );
			g.fillRect(xMid + gap/2, y + gap, rectw/2 - gap/2, rectw );
			
			g.setColor(Color.black);
			g.drawRect(xMid + gap/2, y + gap, rectw/2 - gap/2, rectw );
			g.drawRect(xMid - rectw/2, y + gap, rectw/2 - gap/2, rectw );
			
		}
	} 
}
