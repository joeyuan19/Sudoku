/*
Java class to implement a double buffered applet
You have my permission to use freely, as long
as you keep the attribution. - Ken Perlin
*/

import java.awt.*;
import java.awt.event.*;

public abstract class BufferedApplet extends java.applet.Applet implements Runnable, KeyListener, MouseListener, MouseMotionListener
{
   class Event {}
   Event event = new Event();
   public boolean keyDown(Event e, int key) { return false;}
   public boolean keyUp(Event e, int key) { return false;}
   public boolean mouseDown(Event e, int x, int y) { return false;}
   public boolean mouseDrag(Event e, int x, int y) { return false;}
   public boolean mouseUp(Event e, int x, int y) { return false;}
   public boolean mouseMove(Event e, int x, int y) { return false;}
   //public Rectangle bounds() { return r; }

   public boolean[] keyDown = new boolean[256], wasKeyDown = new boolean[256];
   public int mouseX, wasMouseX;
   public int mouseY, wasMouseY;
   public boolean mouseDown, wasMouseDown;

   public void keyPressed(KeyEvent e) { setKey(e.getKeyCode(), e.getKeyChar(), true); keyDown(event, e.getKeyChar()); }
   public void keyReleased(KeyEvent e) { setKey(e.getKeyCode(), e.getKeyChar(), false); keyUp(event, e.getKeyChar()); }
   public void keyTyped(KeyEvent e) { } 

   public void mouseClicked(MouseEvent e) { }
   public void mouseEntered(MouseEvent e) { }
   public void mouseExited(MouseEvent e) { }
   public void mousePressed(MouseEvent e) { setMouse(e.getX(), e.getY(), true); mouseDown(event, e.getX(), e.getY()); }
   public void mouseReleased(MouseEvent e) { setMouse(e.getX(), e.getY(), false); mouseUp(event, e.getX(), e.getY()); }

   public void mouseDragged(MouseEvent e) { setMouse(e.getX(), e.getY(), true); mouseDrag(event, e.getX(), e.getY()); }
   public void mouseMoved(MouseEvent e) { setMouse(e.getX(), e.getY(), false); mouseMove(event, e.getX(), e.getY()); }

   void setKey(int key, int ch, boolean down) {
      if (ch > 255)
         ch = key;
      keyDown[ch] = down;

      damage = true;
   }

   void setMouse(int x, int y, boolean down) {
      mouseX = x;
      mouseY = y;
      mouseDown = down;

      damage = true;
   }

   public boolean damage = true; // Flag advising app. program to rerender
   public boolean animating = false;
   public abstract void render(Graphics g); // App. defines render method

   Image bufferImage = null;                // Image for the double buffer
   private Graphics bufferGraphics = null;  // Canvas for double buffer
   private Thread t;                        // Background thread for rendering
   private Rectangle r = new Rectangle();   // Dimensions of buffer image

   // Extend the start,stop,run methods to implement double buffering.

   public void start() { if (t == null) { t = new Thread(this); t.start(); } }
   //public void stop()  { if (t != null) { t.stop(); t = null; } }
   public void stop()  { t = null; }
   public void run() {
      addKeyListener(this);
      addMouseListener(this);
      addMouseMotionListener(this);
      try {
         while (true) { repaint(); t.sleep(30); } // Repaint each 30 msecs
      }
      catch(InterruptedException e){}; // Catch interruptions of sleep().
   }

   // Update(Graphics) is called by repaint() - the system adds canvas.
   // Extend update method to create a double buffer whenever necessary.

   public void update(Graphics g) {
      if (r.width != getWidth() || r.height != getHeight()) {
         bufferImage    = createImage(getWidth(), getHeight());
         bufferGraphics = bufferImage.getGraphics(); // Applet size change.
	 r.width  = getWidth();
	 r.height = getHeight();
         damage = true;                              // Tell application.
      }
      if (damage) {
         render(bufferGraphics); // Ask application to render to buffer,

	 for (int key = 0 ; key < 256 ; key++)
            wasKeyDown[key] = keyDown[key];
         wasMouseX = mouseX;
         wasMouseY = mouseY;
         wasMouseDown = mouseDown;
      }
      damage = animating;
      paint(g);                  // paste buffered image onto the applet.
   }

   // Separate paint method for application to extend if needed.

   public void paint(Graphics g) {
      if (bufferImage != null)
         g.drawImage(bufferImage,0,0,this); // Paste result of render().
   }
}
