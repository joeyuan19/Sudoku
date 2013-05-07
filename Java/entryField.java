
import java.awt.*;

public class EntryField {
	int x, y, w, h, data;
	int adjX = 12, adjY = -12;
	boolean highlight;

	public EntryField(int x, int y, int w, int h, int data) {
		this.x = x;
		this.y = y;
		this.w = w;
		this.h = h;
		this.data = data;
	}
	public void draw(Graphics g) {
		g.setColor(Color.white);
		g.fillRect(x, y, w, h);
		g.setColor(highlight ? Color.red : Color.black);
		g.drawRect(x, y, w, h);
		g.setColor(Color.black);
		g.drawString((data == 0 ? "" : "" + data), x + adjX, y + h + adjY);
	}
	public void highlight() {
		highlight = true;
	}
	public void unhighlight() {
		highlight = false;
	}
	public boolean isOver(int x, int y) {
		return (this.x <= x && this.x + w >= x && this.y <= y && this.y + h >= y);
	}
	public void changeData(int data) {
		this.data = data;
	}
	public int getData() {
		return data;
	}
}
