# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KalkulatorBmr.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KalkulatorBmr(object):
    def setupUi(self, KalkulatorBmr):
        KalkulatorBmr.setObjectName("KalkulatorBmr")
        KalkulatorBmr.resize(279, 341)
        self.kalkulator_bmr = QtWidgets.QWidget(KalkulatorBmr)
        self.kalkulator_bmr.setObjectName("kalkulator_bmr")
        self.label = QtWidgets.QLabel(self.kalkulator_bmr)
        self.label.setGeometry(QtCore.QRect(10, 10, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.kalkulator_bmr)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 101, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.kalkulator_bmr)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 111, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.kalkulator_bmr)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 111, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.kalkulator_bmr)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 111, 16))
        self.label_5.setObjectName("label_5")
        self.Txt_umur = QtWidgets.QLineEdit(self.kalkulator_bmr)
        self.Txt_umur.setGeometry(QtCore.QRect(140, 70, 113, 20))
        self.Txt_umur.setObjectName("Txt_umur")
        self.cmb_kelamin = QtWidgets.QComboBox(self.kalkulator_bmr)
        self.cmb_kelamin.setGeometry(QtCore.QRect(140, 110, 69, 22))
        self.cmb_kelamin.setObjectName("cmb_kelamin")
        self.cmb_kelamin.addItem("")
        self.cmb_kelamin.addItem("")
        self.Txt_tb = QtWidgets.QLineEdit(self.kalkulator_bmr)
        self.Txt_tb.setGeometry(QtCore.QRect(140, 150, 113, 20))
        self.Txt_tb.setObjectName("Txt_tb")
        self.Txt_bb = QtWidgets.QLineEdit(self.kalkulator_bmr)
        self.Txt_bb.setGeometry(QtCore.QRect(140, 190, 113, 20))
        self.Txt_bb.setObjectName("Txt_bb")
        self.PB_hitung = QtWidgets.QPushButton(self.kalkulator_bmr)
        self.PB_hitung.setGeometry(QtCore.QRect(140, 230, 75, 23))
        self.PB_hitung.setObjectName("PB_hitung")
        self.label_hasil = QtWidgets.QLabel(self.kalkulator_bmr)
        self.label_hasil.setGeometry(QtCore.QRect(100, 300, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_hasil.setFont(font)
        self.label_hasil.setText("")
        self.label_hasil.setObjectName("label_hasil")
        self.label_7 = QtWidgets.QLabel(self.kalkulator_bmr)
        self.label_7.setGeometry(QtCore.QRect(20, 280, 231, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.kalkulator_bmr)
        self.label_8.setGeometry(QtCore.QRect(20, 300, 81, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.kalkulator_bmr)
        self.label_9.setGeometry(QtCore.QRect(140, 300, 31, 20))
        self.label_9.setObjectName("label_9")
        KalkulatorBmr.setCentralWidget(self.kalkulator_bmr)

        self.retranslateUi(KalkulatorBmr)
        QtCore.QMetaObject.connectSlotsByName(KalkulatorBmr)

    def retranslateUi(self, KalkulatorBmr):
        _translate = QtCore.QCoreApplication.translate
        KalkulatorBmr.setWindowTitle(_translate("KalkulatorBmr", "Kalkulator Bmr"))
        self.label.setText(_translate("KalkulatorBmr", "KALKULATOR BMR"))
        self.label_2.setText(_translate("KalkulatorBmr", "Umur"))
        self.label_3.setText(_translate("KalkulatorBmr", "Kelamin"))
        self.label_4.setText(_translate("KalkulatorBmr", "Tinggi Badan (cm)"))
        self.label_5.setText(_translate("KalkulatorBmr", "Berat Badan (kg)"))
        self.cmb_kelamin.setItemText(0, _translate("KalkulatorBmr", "PRIA"))
        self.cmb_kelamin.setItemText(1, _translate("KalkulatorBmr", "WANITA"))
        self.PB_hitung.setText(_translate("KalkulatorBmr", "HITUNG"))
        self.label_7.setText(_translate("KalkulatorBmr", "Kebutuhan Kalori Kamu minimal dalam"))
        self.label_8.setText(_translate("KalkulatorBmr", "sehari adalah "))
        self.label_9.setText(_translate("KalkulatorBmr", "  Kal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KalkulatorBmr = QtWidgets.QMainWindow()
    ui = Ui_KalkulatorBmr()
    ui.setupUi(KalkulatorBmr)
    KalkulatorBmr.show()
    sys.exit(app.exec_())
