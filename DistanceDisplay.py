# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DistanceDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(306, 364)
        Dialog.setMouseTracking(False)
        Dialog.setSizeGripEnabled(False)
        self.table = QtWidgets.QTableWidget(Dialog)
        self.table.setGeometry(QtCore.QRect(60, 100, 131, 251))
        self.table.setAutoFillBackground(False)
        self.table.setAlternatingRowColors(True)
        self.table.setRowCount(60)
        self.table.setColumnCount(1)
        self.table.setObjectName("table")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.table.setHorizontalHeaderItem(0, item)
        self.DistanceLabel = QtWidgets.QLabel(Dialog)
        self.DistanceLabel.setGeometry(QtCore.QRect(40, 20, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.DistanceLabel.setFont(font)
        self.DistanceLabel.setTextFormat(QtCore.Qt.RichText)
        self.DistanceLabel.setObjectName("DistanceLabel")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(230, 330, 56, 17))
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.DistanceDisplay = QtWidgets.QTextEdit(Dialog)
        self.DistanceDisplay.setGeometry(QtCore.QRect(60, 50, 131, 41))
        self.DistanceDisplay.setObjectName("DistanceDisplay")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Trial One"))
        self.DistanceLabel.setText(_translate("Dialog", "Current Distance (Inches)"))
        self.pushButton.setText(_translate("Dialog", "Cancel"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
