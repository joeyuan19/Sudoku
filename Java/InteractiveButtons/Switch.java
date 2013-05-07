
package InteractiveButtons;

import java.awt.*;

public class Switch extends Button{
	protected String s;
	protected Font fontOn = new Font("Verdana", Font.BOLD, 20);
	protected Font fontOff= new Font("Verdana", Font.ITALIC, 20);
	
	public Switch(int x, int y, int w, int h, String s) {
		super(x, y, (w > 39 ? w : 39) , (h/2 > 10 ? h : 22));
		this.s = s; 
	}
	public void Label(Graphics g, boolean gravity) {
		g.setFont(fontOn);
		g.setColor(Color.black);
		g.drawString(s + (s.length() == 0 ? "" : ": "), x + 10, y + h/2 + 10);
		
		g.setFont((gravity ? fontOn : fontOff));
		g.setColor((gravity ? Color.green : Color.red));
		g.drawString((gravity ? "On" : "Off"), (int) (x + w - 38), y + h/2 + 10);
	}
}
