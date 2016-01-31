from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, QRect
from gui_ui import Ui_MainWindow
from cell import Cell


class Gui(QMainWindow, Ui_MainWindow):

    def __init__(self, app):
        QObject.__init__(self)
        super(Gui, self).__init__()
        self.app = app
        self.setupUi(self)

        self.cell_matrix = [[None for y in range(9)]
                            for x in range(9)]

        for f_x in range(3):
            for f_y in range(3):
                frame = QtWidgets.QFrame(self.gridLayoutWidget)
                widget = QtWidgets.QWidget(frame)
                #widget.setGeometry(QRect(160, 170, 160, 80))
                gridLayout = QtWidgets.QGridLayout(widget)
                gridLayout.setContentsMargins(0, 0, 0, 0)
                for x in range(3):
                    for y in range(3):
                        cell = Cell(self)
                        self.cell_matrix[(f_x*3)+x][(f_y*3)+y] = cell
                        gridLayout.addWidget(cell, y, x)
                self.grid.addWidget(frame, f_y, f_x)


#        for x in range(9):
#            for y in range(9):
#                cell = Cell(self)
#                self.cell_matrix[x][y] = cell
#                self.grid.addWidget(cell, y, x)

        self.show()

    def setCallBack(self, callback):
        self.goButton.clicked.connect(callback)

    def start(self):
        self.app.exec_()

    def set(self, x, y, value):
        self.cell_matrix[x][y].label.setText(str(value))
