from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('ui/main.ui', self)
        self.start_button.clicked.connect(self.to_start)
        self.select_button.clicked.connect(self.continue_with_selected_figure)
        self.radius_input.valueChanged.connect(lambda value: self.update_circle_output(value))
        self.home_button.clicked.connect(self.to_home)
        self.next_button_circle.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

    def to_home(self):
        self.stackedWidget.setCurrentIndex(1)

    def to_start(self):
        self.stackedWidget.setCurrentIndex(1)

    def continue_with_selected_figure(self):
        selected_radio = self.figure_choice.checkedButton()
        if selected_radio:
            current_page = self.figure_choice.checkedButton().text().lower()
            self.stackedWidget.setCurrentWidget(
                getattr(self, f'{current_page}_page', self.figure_select_page)
            )

    def update_circle_output(self, value):
        area = 3.14 * value ** 2
        length = 2 * 3.14 * value
        self.circle_area_output.setText(f'{area:.2f}')
        self.circle_length_output.setText(f'{length:.2f}')


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
