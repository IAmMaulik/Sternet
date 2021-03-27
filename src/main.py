import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # NAVBAR
        navbar = QToolBar()
        self.addToolBar(navbar)

        # back and forward buttons
        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # refresh button
        refresh_btn = QAction("Refresh", self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)

        # home button
        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://google.com"))


# RUNNING THE CODE 🔥
app = QApplication(sys.argv)
QApplication.setApplicationName("Sternet Browser")
window = MainWindow()
app.exec_()