from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('ui/main.ui', self)
        self.start_button.clicked.connect(self.start)

    def start(self):
        self.stackedWidget.setCurrentIndex(1)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())

