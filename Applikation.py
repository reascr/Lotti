#!/usr/bin/env python3
# coding: utf-8

import sys
# from PyQt5.QtWidgets import QApplication, QtWidget
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QtWidget

app = QApplication(sys.argv)  # auch leere Liste in Ordnung

# Fenster
w = QtWidget()

w.show()

# PythonProgramm hört auf zu laufen, wenn Fenster zu ist
sys.exit(app.exec_())


