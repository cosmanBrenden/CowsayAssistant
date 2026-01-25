


import sys
import os


    
def loop():
    current = None
    while 1:
        e = d.next_event()
        
        
        window.draw_text(gc, 25,25,"AAAAAAAAAAAAAAA")
        window.display.flush()
            
        if e.type == X.DestroyNotify:
            sys.exit(0)


loop()