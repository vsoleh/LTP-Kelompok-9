from KalkulatorBmr import *

def signals(self):
    self.PB_hitung.clicked.connect(self.hitungan)

def hitungan(self):
    umur = float(self.Txt_umur.text())
    kelamin = self.cmb_kelamin.currentText()
    tb = float(self.Txt_tb.text())
    bb = float(self.Txt_bb.text())
    #try:
    if (kelamin == "PRIA"):
        result = 66.5+(13.7*bb)+(5.0*tb)-(6.0*umur)   
    else :
        result = 65.5 + (9.6 *bb) + (1.8 *tb) - (4.7 *umur)
    self.label_hasil.setText(str(result))

Ui_KalkulatorBmr.signals = signals
Ui_KalkulatorBmr.hitungan = hitungan

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KalkulatorBmr = QtWidgets.QMainWindow()
    ui = Ui_KalkulatorBmr()
    ui.setupUi(KalkulatorBmr)
    ui.signals()
    KalkulatorBmr.show()
    sys.exit(app.exec_())
 