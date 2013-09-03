

# apt-get install python-xlib
import ewmh # http://sourceforge.net/projects/pyewmh
# docs at http://pyewmh.sourceforge.net/

from ewmh import EWMH
ewmh = EWMH()

# get the active window
win = ewmh.getActiveWindow()
print win
print win.__dict__
print win.get_wm_name()
print win.get_geometry()
#print ewmh.getReadableProperties()

print "Work area:", ewmh.getWorkArea()
x, y, w, h =  ewmh.getWorkArea()[0:4]
w = w/2 -1
# height = ewmh.getWorkArea()[3] -1
h =  h-y-10 # some fudging going here. Adjust to suit
ewmh.setMoveResizeWindow(win, 0, x, y, w, h)

ewmh.display.flush()
