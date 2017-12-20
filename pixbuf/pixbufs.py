#!/usr/bin/python

# ZetCode PyGTK tutorial
#
# This code example draws a circle
# using the cairo library
#
# author: jan bodnar
# website: zetcode.com
# last edited: February 2009


import gtk
import math


class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Simple drawing")
        #self.resize(230, 150)
        self.set_position(gtk.WIN_POS_CENTER)

        self.connect("destroy", gtk.main_quit)
        darea = gtk.DrawingArea()
        darea.connect("expose-event", self.expose)
        #pixbuf = gtk.gdk.pixbuf_new_from_file('images/background.jpg')
        #darea.draw_pixbuf(darea, pixbuf)

        self.connect("expose-event", self.draw_pixbuf)
        self.add(darea)
        self.show_all()

    def draw_pixbuf(self, event):
        path = 'images/background.jpg'
        pixbuf = gtk.gdk.pixbuf_new_from_file(path)
        self.window.draw_pixbuf(self.style.bg_gc[gtk.STATE_NORMAL], pixbuf, 0, 0, 0, 0)

    def expose(self, widget, event):
        cr = widget.window.cairo_create()

        cr.set_line_width(9)
        cr.set_source_rgb(0.7, 0.2, 0.0)

        w = self.allocation.width
        h = self.allocation.height

        cr.translate(w / 2, h / 2)
        cr.arc(0, 0, 50, 0, 2 * math.pi)
        cr.stroke_preserve()

        cr.set_source_rgb(0.3, 0.4, 0.6)
        cr.fill()


PyApp()
gtk.main()



'''
#!/usr/bin/env python
import gtk
import math


def draw_pixbuf(widget, event):
    path = 'images/background.jpg'
    pixbuf = gtk.gdk.pixbuf_new_from_file(path)
    widget.window.draw_pixbuf(widget.style.bg_gc[gtk.STATE_NORMAL], pixbuf, 0, 0, 0, 0)

def expose(self, widget, event):
    cr = widget.window.cairo_create()

    cr.set_line_width(9)
    cr.set_source_rgb(0.7, 0.2, 0.0)

    w = self.allocation.width
    h = self.allocation.height

    cr.translate(w / 2, h / 2)
    cr.arc(0, 0, 50, 0, 2 * math.pi)
    cr.stroke_preserve()

    cr.set_source_rgb(0.3, 0.4, 0.6)
    cr.fill()


window = gtk.Window()
darea = gtk.DrawingArea()
window.set_title('Drawing Test')
#window.set_size_request(640, 480)
window.connect('destroy', gtk.main_quit)
hbbox = gtk.HButtonBox()
window.add(hbbox)
hbbox.connect('expose-event', draw_pixbuf)
window.add(darea)
window.show_all()




gtk.main()
'''