from KalkulatorJAN import*

def signals(self):
    self.push_hitung.clicked.connect(self.hitungan)

def hitungan(self):
    try:
        usia = int(self.line_umur.text())
        kelamin = self.combo_kelamin.currentText()

        if (kelamin == "PRIA"):
            result = 210 - (usia * 0.7)
        elif(kelamin == "WANITA"):
            result = 200 - (usia * 0.7)
        self.label_hasil.setText(str(result))
    except:
        self.label_hasil.setText(str('Error!!!'))

Ui_FormJAN.signals = signals
Ui_FormJAN.hitungan = hitungan

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormJAN = QtWidgets.QWidget()
    ui = Ui_FormJAN()
    ui.setupUi(FormJAN)
    ui.signals()
    FormJAN.show()
    sys.exit(app.exec_())