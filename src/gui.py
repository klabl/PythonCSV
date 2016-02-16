# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Mon Jan 18 21:54:57 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1012, 710)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tb = QtGui.QTextBrowser(Form)
        self.tb.setObjectName("tb")
        self.gridLayout.addWidget(self.tb, 0, 0, 1, 1)
        self.el = QtGui.QPushButton(Form)
        self.el.setObjectName("el")
        self.gridLayout.addWidget(self.el, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.el.setText(QtGui.QApplication.translate("Form", "Einlesen", None, QtGui.QApplication.UnicodeUTF8))

