from KalkulatorBMI import *

def signals(self):
    self.PB_hitung.clicked.connect(self.hitungan)

def hitungan(self):
    tb = float(self.Txt_tb.text())
    bb = float(self.Txt_bb.text())
    #hitung:
    hasil= bb / tb 
    self.label_hasil.setText(str(result))

Ui_KalkulatorBMI.signals = signals
Ui_KalkulatorBMI.hitungan = hitungan

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_KalkulatorBMI()
    ui.setupUi(KalkulatorBMI)
    ui.signals
    KalkulatorBMI.show()
    sys.exit(app.exec_())
