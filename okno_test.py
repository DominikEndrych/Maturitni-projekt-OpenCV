from __future__ import unicode_literals

import os
import glob
import sys
from time import sleep
import ConfigParser
import datetime
import xml.sax
import urllib2
import logging
from collections import defaultdict
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def show_error_dialog(parent, message, title=None):
    dlg = Gtk.MessageDialog(parent, Gtk.DIALOG_MODAL, Gtk.MESSAGE_ERROR, Gtk.BUTTONS_CLOSE, message)
    if title is not None:
        dlg.set_title('Chyba pri zapisu souboru')
    dlg.run()
    dlg.destroy()


# Predne zkontroluji, zda program bezi na podporovane plaforme (windows, linux)
if not sys.platform.startswith('win') and not sys.platform.startswith('linux'):
    show_error_dialog(None, u'Vas operacni system neni bohuzel podporovan.')
    exit(1)




class Copy2MainGUI(object):
    global i
    def __init__(self):
        self.gladefile = 'okno.glade'
        self.glade = Gtk.Builder()
        self.glade.add_from_file(self.gladefile)
        self.glade.connect_signals(self)
        self.window = self.glade.get_object('win_sync')
        #self.window.connect('destroy', lambda f: Gtk.main_quit())
if __name__ == '__main__':
    app = Copy2MainGUI()
    Gtk.main()
