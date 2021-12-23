from KalkulatorBMI import *


def signals(self):
    self.pushButton.clicked.connect(self.hitungan)

def hitungan(self):
    tb = float(self.Txt_tb.text())
    bb = float(self.Txt_bb.text())
    #hitung:
    result= bb / tb 
    self.statusbar.setText(str(result))

Ui_MainWindow.signals = signals
Ui_MainWindow.hitungan = hitungan

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    MainWindow.show()
    sys.exit(app.exec_())
