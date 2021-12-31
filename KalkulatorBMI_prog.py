from KalkulatorBMI import *


def signals(self):
    self.pb_hitung.clicked.connect(self.hitungan)


def hitungan(self):
    try:
        tb = float(self.Txt_tb.text())
        bb = float(self.Txt_bb.text())
        result= bb / (tb/100)**2

        if (result < 18.5):
            cek = "Kategori : Berat Badan Kurang"
        elif(result <= 25):
            cek = "Kategori : Berat Badan Normal"
        elif(result > 25):
            cek = "Kategori : Berat Badan Berlebih" 


        self.label_hasil.setText("{:.2f} ".format(result))
        self.label_hasil2.setText(str(cek))
    
    except:
        self.label_hasil.setText(str('Error!!!'))



Ui_MainWindow.signals = signals
Ui_MainWindow.hitungan = hitungan

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals
    MainWindow.show()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    MainWindow.show()
    sys.exit(app.exec_())
