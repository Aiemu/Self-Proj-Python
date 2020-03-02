# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

import random


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(480, 400))
        Form.setMaximumSize(QtCore.QSize(480, 400))
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setAutoFillBackground(True)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 480, 360))
        self.label.setText("")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(50, 365, 391, 32))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.btn_clicked)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("MainPage", "MainPage"))
        self.radioButton.setText(_translate("Form", "Random"))
        self.pushButton.setText(_translate("Form", "Next"))

    count = 0

    def btn_clicked(self):
        if self.radioButton.isChecked():
            self.count = random.randint(1, 92)
        else:
            if self.count == 92:
                self.count = 1
            else:
                self.count += 1

        path = 'img/img' + str(self.count) + '.JPG'

        # Notice the location
        QtWidgets.QApplication.processEvents() 

        pixRead = QPixmap(path)
        pixShow = pixRead.scaled(480, 360, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)

        self.label.setPixmap(pixShow)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

