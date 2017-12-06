import gi
import sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Copy2MainGUI(object):
    global i
    def __init__(self):
        self.gladefile = 'okno.glade'
        self.glade = Gtk.Builder()
        self.glade.add_from_file(self.gladefile)
        self.glade.connect_signals(self)
        self.window = self.glade.get_object('dialog1')
        #self.window.connect('destroy', lambda f: Gtk.main_quit())
        self.window.show_all()
        self.progress_total = self.glade.get_object('image1')

    def btn_click_tygr(self, button):
        self.glade.get_object('image1').clear()
        self.glade.get_object('image1').set_from_file('tygr.png')
        print "Obrazek zmenen na tygra."

    def btn_click_zebra(self, button):
        self.glade.get_object('image1').clear()
        self.glade.get_object('image1').set_from_file('zebra.png')
        print "Obrazek zmenen na zebru."

    def btn_click_slon(self, button):
        self.glade.get_object('image1').clear()
        self.glade.get_object('image1').set_from_file('slon.png')
        print "Obrazek zmenen na slona."

    def btn_click_off(self, button):
        Gtk.main_quit()
        return True

    def btn_click_new(self, button):
        self.gladefile = 'nove_okno.glade'
        self.glade = Gtk.Builder()
        self.glade.add_from_file(self.gladefile)
        self.glade.connect_signals(self)
        self.window2 = self.glade.get_object('newWindow')
        # self.window.connect('destroy', lambda f: Gtk.main_quit())
        self.window2.show_all()

   # def btn_click_msg(self, button):
   #     return True


    #def btn1_click_update(self, button):
     #   """
     #   Potvrzeni vytvoreni vybranych akci ze serveru.
     #   """
     #   #self.statusicon.set_property('visible', False)
     #   print 'cancel;'
     #   print self.progress_total


    #def on_btn_minus_clicked(self,button):
    #   print "minus"

    #def on_btn_plus_clicked(self,button):
    #        print "plus"

pass



if __name__ == '__main__':
    app = Copy2MainGUI()
    Gtk.main()
