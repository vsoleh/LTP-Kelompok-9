# -*- coding: utf-8 -*-

# FormJAN implementation generated from reading ui file 'KalkulatorJAN.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormJAN(object):
    def setupUi(self, FormJAN):
        FormJAN.setObjectName("FormJAN")
        FormJAN.resize(275, 306)
        self.label = QtWidgets.QLabel(FormJAN)
        self.label.setGeometry(QtCore.QRect(40, 20, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FormJAN)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line_umur = QtWidgets.QLineEdit(FormJAN)
        self.line_umur.setGeometry(QtCore.QRect(150, 80, 91, 22))
        self.line_umur.setObjectName("line_umur")
        self.label_3 = QtWidgets.QLabel(FormJAN)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.combo_kelamin = QtWidgets.QComboBox(FormJAN)
        self.combo_kelamin.setGeometry(QtCore.QRect(150, 120, 91, 22))
        self.combo_kelamin.setObjectName("combo_kelamin")
        self.combo_kelamin.addItem("")
        self.combo_kelamin.addItem("")
        self.label_4 = QtWidgets.QLabel(FormJAN)
        self.label_4.setGeometry(QtCore.QRect(30, 220, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.push_hitung = QtWidgets.QPushButton(FormJAN)
        self.push_hitung.setGeometry(QtCore.QRect(150, 170, 93, 28))
        self.push_hitung.setObjectName("push_hitung")
        self.label_5 = QtWidgets.QLabel(FormJAN)
        self.label_5.setGeometry(QtCore.QRect(30, 250, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(FormJAN)
        self.label_6.setGeometry(QtCore.QRect(120, 250, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_hasil = QtWidgets.QLabel(FormJAN)
        self.label_hasil.setGeometry(QtCore.QRect(80, 250, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_hasil.setFont(font)
        self.label_hasil.setText("")
        self.label_hasil.setObjectName("label_hasil")

        self.retranslateUi(FormJAN)
        QtCore.QMetaObject.connectSlotsByName(FormJAN)

    def retranslateUi(self, FormJAN):
        _translate = QtCore.QCoreApplication.translate
        FormJAN.setWindowTitle(_translate("FormJAN", "FormJAN"))
        self.label.setText(_translate("FormJAN", "Kalkulator Jantung"))
        self.label_2.setText(_translate("FormJAN", "Usia (Tahun)"))
        self.label_3.setText(_translate("FormJAN", "Jenis Kelamin"))
        self.combo_kelamin.setItemText(0, _translate("FormJAN", "PRIA"))
        self.combo_kelamin.setItemText(1, _translate("FormJAN", "WANITA"))
        self.label_4.setText(_translate("FormJAN", "Detak jantung MAKSIMAL kamu"))
        self.push_hitung.setText(_translate("FormJAN", "HITUNG"))
        self.label_5.setText(_translate("FormJAN", "adalah"))
        self.label_6.setText(_translate("FormJAN", " detakan permenit."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormJAN = QtWidgets.QWidget()
    ui = Ui_FormJAN()
    ui.setupUi(FormJAN)
    FormJAN.show()
    sys.exit(app.exec_())