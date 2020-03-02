from mainPage import Ui_Form 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap

import sys
import random



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())