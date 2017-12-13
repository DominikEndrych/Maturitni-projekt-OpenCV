#!/usr/bin/env python
# vim: set fileencoding=utf-8

import sys

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore
from PySide import QtGui



# nový widget bude odvozen od obecného widgetu
class MainWindow(QtGui.QWidget):
    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindow, self).__init__()

        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareGUI(self):
        # velikost není potřeba specifikovat
        self.resize(320, 240)
        self.setWindowTitle("QLabel widget")

        # textové návěští
        # pozor na nutnost použití prefixu "u" v Pythonu 2.x
        text = u"<font color='black'>černá</font><br />" \
               u"<font color='blue'>modrá</font><br />" \
               u"<font color='red'>čevená</font><br />"



        textLabel = QtGui.QLabel(text)
        textLabel.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)

        # tlačítko pro ukončení aplikace
        quitButton = QtGui.QPushButton("Quit")
        helloButton = QtGui.QPushButton("Hello World")

        # vytvoření správce geometrie
        layout = QtGui.QVBoxLayout()

        # umístění widgetů do okna
        layout.addWidget(textLabel)
        layout.addWidget(quitButton)
        layout.addWidget(helloButton)


        # nastavení správce geometrie a vložení všech komponent do okna
        self.setLayout(layout)

        # navázání akce na stisk tlačítka pro ukončení aplikace

        quitButton.clicked.connect(self.quit)
        helloButton.clicked.connect(self.hello)

    def run(self, app):
        # zobrazení okna na obrazovce
        self.show()
        # vstup do smyčky událostí (event loop)
        app.exec_()

    def quit(self):
        print("Closing...")
        self.close()

    def hello(self):
        print("Hello world")


def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow().run(app)


if __name__ == '__main__':
    main()
