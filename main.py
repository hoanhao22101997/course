
from hear import *
from test import*
from PyQt5 import QtCore, QtGui, QtWidgets
from testui import Ui_MainWindow
import sys
import webbrowser
class main_handdle(Ui_MainWindow):
    def __init__(self):
            self.setupUi(MainWindow)
you = hear
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = main_handdle()
    MainWindow.show()
    sys.exit(app.exec_())
        