#!/usr/bin/python3
#/usr/bin/env python

import sys
import time
from background import Background

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

(TARGET_ENTRY_TEXT, TARGET_ENTRY_PIXBUF) = range(2)
(COLUMN_TEXT, COLUMN_PIXBUF) = range(2)

DRAG_ACTIONC = Gdk.DragAction.COPY

class DragDropWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Fast Archiver")
        self.set_position(Gtk.WindowPosition.CENTER)
        #self.set_size_request(300, 250)

        #label = Gtk.Label('')
        #vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=100)
        #vbox.pack_start(label, True, True, 0)

        hbox = Gtk.Box(spacing=10)
        #vbox.pack_start(hbox, True, True, 0)
        self.drop_areaTar = DropArea('TAR')        
        self.drop_areaZip = DropArea('ZIP')
        hbox.pack_start(self.drop_areaTar, True, True, 0)        #self.add_text_targets()
        hbox.pack_start(self.drop_areaZip, True, True, 0)        #self.add_text_targets()
        
        #llabel = Gtk.Label('')
        #vvbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=100)
        #vbox.pack_end(llabel, True, True, 0)

        #self.add(vvbox)

        self.add(hbox)
        self.add_text_targets()

    def on_drag_data_get(self, widget, drag_context, data, info, time):
        selected_path = self.get_selected_items()[0]
        selected_iter = self.get_model().get_iter(selected_path)
        print(selected_path)

    def add_text_targets(self, button=None):        #self.drop_areaTar.drag_dest_set_target_list(None)
        self.drop_areaTar.drag_dest_add_text_targets()
        self.drop_areaZip.drag_dest_add_text_targets()

class DropArea(Gtk.Label):

    def __init__(self, ltext):
        Gtk.Label.__init__(self)
        self.set_label(ltext)
        self.drag_dest_set(0, [], DRAG_ACTIONC)
        self.drag_dest_set(Gtk.DestDefaults.ALL, [], DRAG_ACTIONC)
        #self.connect('drag-motion', self.on_drag_move)
        #self.connect('drag-drop', self.on_drag_dropped)
        self.connect('drag-data-received', self.drag_data_received)
        self.set_size_request(150, 100)

    def drag_data_received(self, widget, drag_context, x,y, data,info, time):
        if info == TARGET_ENTRY_TEXT:
            text = data.get_text()
            print("Received text: %s" % text)

        elif info == TARGET_ENTRY_PIXBUF:
            pixbuf = data.get_pixbuf()
            width = pixbuf.get_width()
            height = pixbuf.get_height()

            print("Received pixbuf with width %spx and height %spx" % (width,
                height))

    def drag_data_received00(self, widget, context, x,y, data,info, time):
        #l.set_text('\n'.join([str(t) for t in context.list_targets()]))
        #context.finish(True, False, time)
        print('>>>>>>>>>>>>>>>|||||||||||===============||||||||||||<<<<<<<<<<<<<<<<<<<<')

        if info == 0:
            text = data.get_text()
            print("Received text: %s" % text)
            Background.pk(path)
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