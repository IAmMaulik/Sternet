import sys
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.showMaximized()


# RUNNING THE CODE 🔥
app = QApplication(sys.argv)
QApplication.setApplicationName("Sternet Browser")
window = MainWindow()
app.exec_()