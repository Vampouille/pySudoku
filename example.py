#!/usr/bin/env python3

from gui import Gui


def go():
    gui.setValue(0, 0, 1)
    gui.setValue(0, 1, 2)
    gui.setValue(0, 2, 7)
    gui.setValue(0, 3, None)
    gui.setValue(0, 4, 9)
    gui.setColor(0, 0, "green")
    gui.setColor(0, 1, "green")
    gui.setColor(0, 2, "green")
    gui.setColor(0, 3, "green")
    gui.setColor(0, 4, "green")

    gui.setValue(1, 0, 1)
    gui.setValue(1, 1, 4)
    gui.setValue(1, 2, 8)
    gui.setValue(1, 3, "")
    gui.setValue(1, 4, 9)


gui = Gui()
gui.setCallBack(go)
gui.start()
