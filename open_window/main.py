import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
    def btn_click_off(self, *args):
        Gtk.main_quit(*args)

    def btn_click_msg(self, button):
        print("Hello World!")

builder = Gtk.Builder()
builder.add_from_file("okno.glade")
builder.connect_signals(Handler())

window = builder.get_object("dialog1")
window.show_all()

Gtk.main()

