# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KalkulatorBMI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(222, 272)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Txt_tb = QtWidgets.QLineEdit(self.centralwidget)
        self.Txt_tb.setGeometry(QtCore.QRect(120, 60, 70, 20))
        self.Txt_tb.setObjectName("Txt_tb")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 91, 16))
        self.label_3.setObjectName("label_3")
        self.Txt_bb = QtWidgets.QLineEdit(self.centralwidget)
        self.Txt_bb.setGeometry(QtCore.QRect(120, 90, 70, 20))
        self.Txt_bb.setObjectName("Txt_bb")
        self.pb_hitung = QtWidgets.QPushButton(self.centralwidget)
        self.pb_hitung.setGeometry(QtCore.QRect(80, 130, 75, 23))
        self.pb_hitung.setObjectName("pb_hitung")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 170, 61, 51))
        self.label_4.setObjectName("label_4")
        self.label_hasil = QtWidgets.QLabel(self.centralwidget)
        self.label_hasil.setGeometry(QtCore.QRect(76, 173, 131, 21))
        self.label_hasil.setText("")
        self.label_hasil.setObjectName("label_hasil")
        self.label_hasil2 = QtWidgets.QLabel(self.centralwidget)
        self.label_hasil2.setGeometry(QtCore.QRect(90, 205, 121, 31))
        self.label_hasil2.setText("")
        self.label_hasil2.setObjectName("label_hasil2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 222, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Kalkulator BMI"))
        self.label_2.setText(_translate("MainWindow", "Tinggi Badan(cm)"))
        self.label_3.setText(_translate("MainWindow", "Berat Badan(kg)"))
        self.pb_hitung.setText(_translate("MainWindow", "HITUNG"))
        self.label_4.setText(_translate("MainWindow", "BMI ANDA:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
