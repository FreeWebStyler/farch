#!/usr/bin/python3
#/usr/bin/env python

import sys
import time
#from background import Background
#from main_window import MainWindow

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

(TARGET_ENTRY_TEXT, TARGET_ENTRY_PIXBUF) = range(2)
(COLUMN_TEXT, COLUMN_PIXBUF) = range(2)

DRAG_ACTIONC = Gdk.DragAction.COPY

class DragDropWindow(Gtk.Window):

    def __init__(self):
        #Gtk.Window.__init__(self, title="Drag and Drop Demo") w = Gtk.Window()
        Gtk.Window.__init__(self, title="Drag and Drop Demo")
        #print(self)
        #w = Gtk.Window()

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        hbox = Gtk.Box(spacing=12)
        vbox.pack_start(hbox, True, True, 0)

        self.iconview = DragSourceIconView()
        self.drop_area = DropArea()

        hbox.pack_start(self.iconview, True, True, 0)
        hbox.pack_start(self.drop_area, True, True, 0)

        button_box = Gtk.Box(spacing=6)
        vbox.pack_start(button_box, True, False, 0)

        image_button = Gtk.RadioButton.new_with_label_from_widget(None,
            "Images")
        image_button.connect("toggled", self.add_image_targets)
        button_box.pack_start(image_button, True, False, 0)

        text_button = Gtk.RadioButton.new_with_label_from_widget(image_button,
            "Text")
        text_button.connect("toggled", self.add_text_targets)
        button_box.pack_start(text_button, True, False, 0)

        #self.add_image_targets()
        #self.add_text_targets()

    def add_image_targets(self, button=None):
        targets = Gtk.TargetList.new([])
        targets.add_image_targets(TARGET_ENTRY_PIXBUF, True)

        self.drop_area.drag_dest_set_target_list(targets)
        self.iconview.drag_source_set_target_list(targets)

    def add_text_targets(self, button=None):
        self.drop_area.drag_dest_set_target_list(None)
        self.iconview.drag_source_set_target_list(None)

        self.drop_area.drag_dest_add_text_targets()
        self.iconview.drag_source_add_text_targets()

class DragSourceIconView(Gtk.IconView):

    def __init__(self):
        Gtk.IconView.__init__(self)
        self.set_text_column(COLUMN_TEXT)
        self.set_pixbuf_column(COLUMN_PIXBUF)

        model = Gtk.ListStore(str, GdkPixbuf.Pixbuf)
        self.set_model(model)
        self.add_item("Item 1", "image-missing")
        self.add_item("Item 2", "help-about")
        self.add_item("Item 3", "edit-copy")

        self.enable_model_drag_source(Gdk.ModifierType.BUTTON1_MASK, [],
            DRAG_ACTIONC)
        self.connect("drag-data-get", self.on_drag_data_get)

    def on_drag_data_get(self, widget, drag_context, data, info, time):
        selected_path = self.get_selected_items()[0]
        selected_iter = self.get_model().get_iter(selected_path)

        print(selected_path)

        if info == TARGET_ENTRY_TEXT:
            text = self.get_model().get_value(selected_iter, COLUMN_TEXT)
            data.set_text(text, -1)
        elif info == TARGET_ENTRY_PIXBUF:
            pixbuf = self.get_model().get_value(selected_iter, COLUMN_PIXBUF)
            data.set_pixbuf(pixbuf)

    def add_item(self, text, icon_name):
        pixbuf = Gtk.IconTheme.get_default().load_icon(icon_name, 16, 0)
        self.get_model().append([text, pixbuf])


class DropArea(Gtk.Label):

    def __init__(self):
        Gtk.Label.__init__(self)
        self.set_label("Drop something on me!")
        #print(Gtk.DestDefaults.ALL)
        #print(Gtk.DestDefaults)
        #self.drag_dest_set(Gtk.DestDefaults.ALL, [], DRAG_ACTION)
        #self.drag_dest_set(Gtk.DestDefaults.DROP, [], DRAG_ACTION)
        #self.drag_dest_set(0, [], DRAG_ACTION)
        #self.drag_dest_set(0, [], 0)
        self.drag_dest_set(0, [], DRAG_ACTIONC)

        #self.connect("drag-data-received", self.on_drag_data_received)
        #self.connect('drag-motion', motion_cb)
        #self.connect('drag-drop', drop_cb)
        self.connect('drag-motion', self.on_drag_move)
        self.connect('drag-drop', self.on_drag_dropped)
        #self.connect('drag_data_received', self.drag_data_received)
        self.connect('drag-data-received', self.drag_data_received)

    #def on_drag_data_receivedd(self, widget, drag_context, x,y, data):
    #def on_drag_data_receivedd(*args):
    #    print(args)

    #def on_drag_data_receivedr(wid, context, x, y, time, data):
    def drag_data_received6(self, dao, context, x, y, time):
        #l.set_text('\n'.join([str(t) for t in context.list_targets()]))
        #context.finish(True, False, time)
        print('>>>>>>>>>>>>>>>|||||||||||===============||||||||||||<<<<<<<<<<<<<<<<<<<<')
        print(context.list_targets())
        print(self)
        print(dao)
        print(context)
        print(x)
        print(y)
        print(time)
        return True

    def drag_data_received(self, widget, context, x,y, data,info, time):
        #l.set_text('\n'.join([str(t) for t in context.list_targets()]))
        #context.finish(True, False, time)
        print('>>>>>>>>>>>>>>>|||||||||||===============||||||||||||<<<<<<<<<<<<<<<<<<<<')

        if info == TARGET_ENTRY_TEXT:
            text = data.get_text()
            print("Received text: %s" % text)
                    
        print(context.list_targets())
        print(self)
        print(widget)
        print(context)
        print(x)
        print(y)
        print(data)
        print(info)
        print(time)
        print(type(data))
        print(type(data.get_text()))
        print(data.get_text())
        return True

    def on_drag_dropped(self, dao, context, x, y, time):
        #l.set_text('\n'.join([str(t) for t in context.list_targets()]))
        #context.finish(True, False, time)
        print('|||||||||||||||||||||||')
        print(self.drag_get_data(context, context.list_targets()[1], time))
        return True
        print(type(self))
        print(type(dao))
        print(type(context))
        print(context.list_targets())
        #target_type = (Atom) context.list_targets().nth_data (Target.INT32);
        #print(Gtk.gtk_drag_get_data(self, context, Gdk.Atom, time))
        print(context.list_targets()[0])
        print(context.list_targets()[1])
        #print(type(context.list_targets()))
        #print(type(context.list_targets()[1]))
        #print(context.list_targets()[0].get_uris())
        #print(context.list_targets()[1].get_uris())
        #print(dao.drag_get_data(context, context.list_targets()[0], time))
        #res = dao.drag_get_data(context, context.list_targets()[0], time)
        #print(type(res))
        #print(res)
        print('!!!!!===========||||||||||||')
        print(dao.drag_get_data(context, context.list_targets()[0], time))
        #print(self.drag_get_data(context, context.list_targets()[0], time))
        print(dao.drag_get_data(context, context.list_targets()[-1], time))
        #print(self.drag_get_data(context, context.list_targets()[-1], time))
        print('===========||||||||||||')
        print(self)
        print(dao)
        print(context)
        print(x)
        print(y)
        print(time)
        context.finish(True, False, time)

        print(dao.drag_get_data(context, context.list_targets()[-1], time))
        print(self.drag_get_data(context, context.list_targets()[-1], time))
        return True

    def on_drag_move(self, dao, context, x, y, time):
        
        #l.set_text('\n'.join([str(t) for t in context.list_targets()]))
        #context.finish(True, False, time)
        '''print('=====')
        print(self)
        print(dao)
        print(context)
        print(x)
        print(y)
        print(time)'''
        #Gdk.drag_status(context, Gdk.DragAction.COPY, time)
        Gdk.drag_status(context, DRAG_ACTIONC, time)
        #Gdk.drag_status(context, Gdk.DragAction.COPY, 333333)
        #dao.drag_status(gtk.gdk.ACTION_COPY, time)
        #self.drag_status()
        return True

    def on_drag_data_receivedd1(**kwargs):
        for key, value in kwargs.items():
            print("The value of {} is {}".format(key, value))
        #print(diction)

    def on_drag_data_received0(self, widget, drag_context, x,y, data,info, time):
        print("Received1111111111111")
        if info == TARGET_ENTRY_TEXT:
            text = data.get_text()
            print("Received text: %s" % text)

        elif info == TARGET_ENTRY_PIXBUF:
            pixbuf = data.get_pixbuf()
            width = pixbuf.get_width()
            height = pixbuf.get_height()

            print("Received pixbuf with width %spx and height %spx" % (width,
                height))

def main():
    win = DragDropWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
    #window = Gtk.Window()
    #LANG=en_EN.UTF-8
    #lsblk --output KNAME,SIZE,HOTPLUG
    #sudo mount -o users,uid=1000,gid=1000 /dev/sdc1 /mnt/usb