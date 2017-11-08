import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk



builder = Gtk.Builder()
builder.add_from_file("okno.glade")

window = builder.get_object("dialog1")
window.show_all()

Gtk.main()

