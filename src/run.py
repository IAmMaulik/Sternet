import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from main import MainWindow

# RUNNING THE CODE 🔥
app = QApplication(sys.argv)
QApplication.setApplicationName("Sternet Browser")
window = MainWindow()
app.exec_()