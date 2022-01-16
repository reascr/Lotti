import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

def clicked():
    print("clicked")
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500, 500, 500, 500) #xpos, ypos, width, height
    win.setWindowTitle("Abrechnungsprogramm Nachhilfeschule C. Schröter-Eiserich")
    win.setStyleSheet("background-color: pink;")
    #label = QtWidgets.QLabel(win)
    #label.setText("my first label")
    #label.move(50,50)
    b1 = QtWidgets.QPushButton(win)
    b1.setText("Bitte drücken")
    b1.clicked.connect(clicked) #

    win.show()
    sys.exit(app.exec_())

window()