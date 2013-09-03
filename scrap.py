# code that has been scrapped

import wnck
screen = wnck.screen_get_default()
window_list = screen.get_windows()
active_window = screen.get_active_window()

print active_window #.__dict__

import subprocess
# inp = '\n'.join(inlines)
p = subprocess.Popen(['xdotool', 'getactivewindow'] , stdout = subprocess.PIPE)
out, err = p.communicate()
print "computer says:", out

print window_list
