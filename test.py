#!/usr/bin/python
#
# examples/draw.py -- high-level xlib test application.
#
#    Copyright (C) 2000 Peter Liljenberg <petli@ctrl-c.liu.se>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation; either version 2.1
# of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
#    Free Software Foundation, Inc.,
#    59 Temple Place,
#    Suite 330,
#    Boston, MA 02111-1307 USA


import sys
import os
import env
import jarviscli
import colorama

#import colorama
# Change path so we find Xlib
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Xlib import X, display, Xutil

# Application window (only one)
class Window(object):
    def __init__(self, display):
        self.d = display
        self.objects = []

        # Find which screen to open the window on
        self.screen = self.d.screen()

        self.window = self.screen.root.create_window(
            50, 50, 300, 200, 2,
            self.screen.root_depth,
            X.InputOutput,
            X.CopyFromParent,

            # special attribute values
            background_pixel = self.screen.white_pixel,
            event_mask = (X.ExposureMask |
                          X.StructureNotifyMask |
                          X.ButtonPressMask |
                          X.ButtonReleaseMask |
                          X.Button1MotionMask),
            colormap = X.CopyFromParent,
            )

        self.gc = self.window.create_gc(
            foreground = self.screen.black_pixel,
            background = self.screen.white_pixel,
            )

        # Set some WM info

        self.WM_DELETE_WINDOW = self.d.intern_atom('WM_DELETE_WINDOW')
        self.WM_PROTOCOLS = self.d.intern_atom('WM_PROTOCOLS')

        self.window.set_wm_name('Xlib example: draw.py')
        self.window.set_wm_icon_name('draw.py')
        self.window.set_wm_class('draw', 'XlibExample')

        self.window.set_wm_protocols([self.WM_DELETE_WINDOW])
        self.window.set_wm_hints(flags = Xutil.StateHint,
                                 initial_state = Xutil.NormalState)

        self.window.set_wm_normal_hints(flags = (Xutil.PPosition | Xutil.PSize
                                                 | Xutil.PMinSize),
                                        min_width = 20,
                                        min_height = 20)

        # Map the window, making it visible
        self.window.map()

    # enable color on windows
    colorama.init()
    # start Jarvis
    jarvis = Jarvis.Jarvis()
    command = " ".join(sys.argv[1:]).strip()
    jarvis.executor(command)

    #result = subprocess.run(['/home/rbray/jarvis/CowsayAssistant/jarvis'])
    # Main loop, handling events
    
    def loop(self):
        current = None
        while 1:
            e = self.d.next_event()

            

            gc = self.window.create_gc(foreground = self.screen.black_pixel,
            background = self.screen.white_pixel)
            self.window.draw_text(gc,25,25,"a")       
            self.window.display.flush()
        
            
            #self.win.window.draw_text(self.win.gc, 0,0,"penis", onerror=None)

            # Window has been destroyed, quit
            if e.type == X.DestroyNotify:
                sys.exit(0)

            # Some part of the window has been exposed,
            # redraw all the objects.
            if e.type == X.Expose:
                for o in self.objects:
                    o.expose(e)

            if e.type == X.ClientMessage:
                if e.client_type == self.WM_PROTOCOLS:
                    fmt, data = e.data
                    if fmt == 32 and data[0] == self.WM_DELETE_WINDOW:
                        sys.exit(0)


                self.last.draw()


if __name__ == '__main__':
    Window(display.Display()).loop()