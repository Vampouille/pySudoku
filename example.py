#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication
import sys
from gui import Gui

gui = Gui(QApplication(sys.argv))


def go():
    gui.set(0, 0, 1)
    gui.set(0, 1, 2)
    gui.set(0, 2, 7)
    gui.set(0, 3, None)
    gui.set(0, 4, 9)


gui.setCallBack(go)
gui.start()
