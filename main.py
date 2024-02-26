from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('ui/main.ui', self)
        self.start_button.clicked.connect(self.start)
        self.select_button.clicked.connect(self.continue_with_selected_figure)

    def start(self):
        self.stackedWidget.setCurrentIndex(1)

    def continue_with_selected_figure(self):
        selected_radio = self.figure_choice.checkedButton()
        if selected_radio:
            current_page = self.figure_choice.checkedButton().text().lower()
            self.stackedWidget.setCurrentWidget(
                getattr(self, f'{current_page}_page', self.figure_select_page)
            )


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
