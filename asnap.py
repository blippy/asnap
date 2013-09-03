# http://stackoverflow.com/questions/8041389/showing-mouseposition-with-python

# mask - tells you which mouse buttons are pressed:
#    1<<4 = 16 - nothing pressed
#    (1<<8) + (1<<4) = 272 - LMB (left mouse button down)
#    (1<<9) + (1<<4) = 528 - MMB (middle mouse button)
#    (1<<10) + (1<<4) = 1040 - RMB (right mouse button down)
#    Combinations are logically-anded. E.g.:
#       (1<<8) + (1<<10) + (1<<4) is LMB and RMB simultaneously

# wmctrl -e g,x,y,w,h

import os
import sys
import Tkinter as tk
import Xlib.display as display # sudo aptitude install python-xlib
import Xlib
import time

doing = False # currently performing an action

class Indent:
    def __init__(self, w, h):
        self.w = w
        self.h = w
        self.top_indent = 0
        self.bottom_indent = 0
        self.left_indent = 0
        self.right_indent = 0
        self.gap_indent = 5
    
# def mousepos(screenroot=display.Display().screen().root):
def mousepos(screenroot, indent):
    """
    rw - root width
    rh - root height
    """

    global doing
    pointer = screenroot.query_pointer()
    data = pointer._data
    lmb = (data['mask'] & 1<<8) > 0 # left mouse button down
    #print "lmb=", lmb
    #print screenroot.display.__dict__
    #print screenroot.width_in_pixels()
    right = data["root_x"] == indent.w -1
    corner = (data["root_x"] == 0 or right) and  data["root_y"] == 0 
    hit = corner and lmb
    #print "hit=", hit
    if hit  and not doing:
        # print doing,
        doing = True

        # common values - assume aerosnap left
        x = indent.left_indent
        y = indent.top_indent
        midx = (indent.left_indent + indent.w - indent.right_indent)/2
        w = midx - indent.gap_indent - indent.left_indent
        h = rh -indent.top_indent- indent.bottom_indent
        if right: # aersosnap right
            x = midx + indent.gap_indent

        cmd = "wmctrl -r :ACTIVE: -e 0,{0},{1},{2},{3}".format(x, y, w, h)
        os.system(cmd)
        cmd = "wmctrl -r :ACTIVE: -b add,maximized_vert"
        # os.system(cmd)
        print ".",
        sys.stdout.flush()
        # time.sleep(1)
    if doing and not lmb:
        doing = False
    # return data["root_x"], data["root_y"]

#def update():
#    strl.set("mouse at {0}".format(mousepos()))
#    root.after(100, update)

#root = tk.Tk()
#strl = tk.StringVar()
#lab = tk.Label(root,textvariable=strl)
#lab.pack()
#root.after(100, update) # every 0.1 seconds
#root.title("Mouseposition")
#root.mainloop()


def main():
    screen = Xlib.display.Display().screen()
    root   = screen.root
    rw = screen.width_in_pixels
    rh = screen.height_in_pixels
    indent = Indent(rw, rh)
    indent.bottom_indent = 50
    #abort(0)
    while True:
        mousepos(root, indent)
        time.sleep(0.1)

if __name__ == "__main__":
    main()
