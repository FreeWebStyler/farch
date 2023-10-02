#!/usr/bin/python3
#/usr/bin/env python

import chardet
import codecs
import os.path # is file
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
        icon_fp = os.path.dirname(os.path.realpath(__file__)) + '/res/farch32.png'
        self.set_icon_from_file(icon_fp)
        #self.set_size_request(300, 250)

        #label = Gtk.Label('')
        #vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=100)
        #vbox.pack_start(label, True, True, 0)

        hbox = Gtk.Box(spacing=10)
        #vbox.pack_start(hbox, True, True, 0)
        self.drop_areaTar = DropArea('TAR')
        self.drop_areaTgz = DropArea('TGZ')
        self.drop_areaZip = DropArea('ZIP')
        hbox.pack_start(self.drop_areaTar, True, True, 0)        #self.add_text_targets()
        hbox.pack_start(self.drop_areaTgz, True, True, 0)        #self.add_text_targets()
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
        self.drop_areaTgz.drag_dest_add_text_targets()
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

    def drag_data_received(self, widget, drag_context, x,y, data, info, time):
        # print(widget)
        #print(widget.get_name())
        if info == TARGET_ENTRY_TEXT:
            #print(data.get_data())
            #fp = data.get_text()
            fpb = data.get_data()
            encoding = chardet.detect(fpb)["encoding"] #print(encoding)
            fp = codecs.decode(bytes(fpb), encoding) #print(fp) sys.exit()
            fp = fp.replace('file://', '')

            if widget.get_label() == 'ZIP':
                pfp = fp +'.zip'
                '''if os.path.isfile(fp):
                    pfp = fp +'.zip'
                else:
                    pfp = fp'''
                Background.pkzip(fp, pfp)

            if widget.get_label() == 'TAR':
                pfp = fp +'.tar'
                '''if os.path.isfile(fp):
                    pfp = fp +'.zip'
                else:
                    pfp = fp'''
                Background.pktar(fp, pfp)

            if widget.get_label() == 'TGZ':
                pfp = fp +'.tgz'
                Background.pktgz(fp, pfp)

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
    win.set_keep_above(True)
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()