# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'szwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, Qt, QtWidgets


class Ui_SZForm(object):
    def setup(self, Form):
        Form.setObjectName("Form")
        Form.resize(907, 410)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 891, 391))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1000)
        self.tableWidget.setHorizontalHeaderLabels(["Номер служебной записки", "Дата служебной записки", "Текст служебной записки"])
        self.tableWidget.resizeColumnsToContents()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Подсказка"))