#!/usr/bin/env python
import gtk


def draw_pixbuf(widget, event):
    path = 'images/background.jpg'
    pixbuf = gtk.gdk.pixbuf_new_from_file(path)
    widget.window.draw_pixbuf(widget.style.bg_gc[gtk.STATE_NORMAL], pixbuf, 0, 0, 0, 0)


window = gtk.Window()
window.set_title('Drawing Test')
#window.set_size_request(640, 480)
window.connect('destroy', gtk.main_quit)
hbbox = gtk.HButtonBox()
window.add(hbbox)
hbbox.connect('expose-event', draw_pixbuf)
window.show_all()

gtk.main()