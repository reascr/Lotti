# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playingaround.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.py


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QMessageBox
import os 
import pandas as pd
import time

DEFAULT_BUTTON_STYLE = "background-color: rgb(193, 164, 234); color: white; border-style: outset; border-width: 2px;  border-radius: 10px; border-color: beige; padding: 10px"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(679, 786)
        # prevent MainWindow from resizing
        MainWindow.setFixedSize(679, 720)
        MainWindow.setStyleSheet("background-color : rgb(173, 180, 175)")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(140, 110, 321, 111))
        # align button horizontally
        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setStyleSheet(DEFAULT_BUTTON_STYLE)
        self.b1.setObjectName("b1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 330, 561, 381))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Logo.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 679, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Schülermeeting Geseke Monatsabrechnungen"))
        MainWindow.setStatusTip(_translate("MainWindow", "Aktueller Monat"))
        self.b1.setText(_translate("MainWindow", " Monatsabrechnung erstellen"))
        self.b1.clicked.connect(self.clicked) 
    
    # Kopie von tryingobject.py
    def clicked(self):
        self.b1.setStyleSheet("background-color: rgb(100, 100, 230); color: grey; border-style: inset; border-width: 2px;  border-radius: 10px; border-color: beige; padding: 10px")
        # neue Klasse für FileSelector
        fileinput = QFileDialog.getOpenFileName(None, "ÜBERSCHRIFT", './', filter="Tabellen (*.xlsx)")
        print("b4")
        print(fileinput)
        if fileinput == ('',''):
            msg = QMessageBox()
            msg.setWindowTitle("Schülermeeting Geseke Abrechnungen")
            msg.setText("Bitte Datei auswählen!")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
            self.b1.setStyleSheet(DEFAULT_BUTTON_STYLE)
            return
        print("after")
        root = os.path.dirname(fileinput[0])
        # TO DO: Checken ob Datei echt ist!!!
        df = pd.read_excel(fileinput[0], header=1)
        Schüler = [x.strip() for x in df["Schüler"].unique()]
        Lehrer = [x.strip() for x in df["Lehrer"].unique()]
        Schüler_Min_Betrag = 19.50/60
        Lehrer_Min_Betrag = 10/60 
    # Schüler in neuen DataFrame
        Minuten_ges = list()
        Betrag_ges = list()

        Minuten_ges_l = list()
        Betrag_ges_l = list()

        # Minuten gesamt
        for s in Schüler:
            Min_ges = sum(df["Dauer_min"].where(df["Schüler"] == s.strip()).dropna())
            Minuten_ges.append(Min_ges)
            Bet_ges = Min_ges * Schüler_Min_Betrag
            Betrag_ges.append(Bet_ges)


        # neuer Dataframe
        Schüler_df = pd.DataFrame(Schüler, columns=["Schüler"])
        Schüler_df["Minuten_ges"] = Minuten_ges
        Schüler_df["Betrag_ges"] = Betrag_ges

        Schüler_df = Schüler_df.set_index("Schüler")


        # Lehrer in neuen DataFrame
        for l in Lehrer:
            Min_ges = sum(df["Dauer_min"].where(df["Lehrer"] == l.strip()).dropna())
            Minuten_ges_l.append(Min_ges)
            Bet_ges = Min_ges * Schüler_Min_Betrag
            Betrag_ges_l.append(Bet_ges)


        # neuer Dataframe
        Lehrer_df = pd.DataFrame(Lehrer, columns=["Lehrer"])
        Lehrer_df["Minuten_ges"] = Minuten_ges_l
        Lehrer_df["Betrag_ges"] = Betrag_ges_l
        Lehrer_df =Lehrer_df.set_index("Lehrer")

        # Schüler_df und Lehrer_df in csv_Datei, automatische Erstellung in Zielordner
        Schüler_df.to_excel(root+"/Schüler.xlsx", header=1)
        Lehrer_df.to_excel(root+"/Lehrer.xlsx", header=1)

        time.sleep(2) 
        self.b1.setStyleSheet(DEFAULT_BUTTON_STYLE)

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
