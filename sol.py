#!/usr/bin/python3
#/usr/bin/env python

import sys
import time
#from background import Background
#from main_window import MainWindow

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

(TARGET_ENTRY_TEXT, TARGET_ENTRY_PIXBUF) = range(2)
(COLUMN_TEXT, COLUMN_PIXBUF) = range(2)

DRAG_ACTIONC = Gdk.DragAction.COPY

class DragDropWindow(Gtk.Window):

    def __init__(self):
        #Gtk.Window.__init__(self, title="Drag and Drop Demo") w = Gtk.Window()
        Gtk.Window.__init__(self, title="Sol")
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)
        hbox = Gtk.Box(spacing=12)
        vbox.pack_start(hbox, True, True, 0)
        self.drop_area = DropArea()
        hbox.pack_start(self.drop_area, True, True, 0)
        #self.add_text_targets()

    def on_drag_data_get(self, widget, drag_context, data, info, time):
        selected_path = self.get_selected_items()[0]
        selected_iter = self.get_model().get_iter(selected_path)
        print(selected_path)

class DropArea(Gtk.Label):

    def __init__(self):
        Gtk.Label.__init__(self)
        self.set_label("Drop something on me!")
        self.drag_dest_set(0, [], DRAG_ACTIONC)
        self.connect('drag-motion', self.on_drag_move)
        self.connect('drag-drop', self.on_drag_dropped)
        self.connect('drag-data-received', self.drag_data_received)

    def drag_data_received(self, widget, context, x,y, data,info, time):
        #l.set_text('\n'.join([str(t) for t in context.list_targets()]))
        #context.finish(True, False, time)
        print('>>>>>>>>>>>>>>>|||||||||||===============||||||||||||<<<<<<<<<<<<<<<<<<<<')

        if info == TARGET_ENTRY_TEXT:
            text = data.get_text()
            print("Received text: %s" % text)
        return True

    def on_drag_dropped(self, dao, context, x, y, time):
        self.drag_get_data(context, context.list_targets()[1], time)
        return True

    def on_drag_move(self, dao, context, x, y, time):
        Gdk.drag_status(context, DRAG_ACTIONC, time)
        return True

def main():
    win = DragDropWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()