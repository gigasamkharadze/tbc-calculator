from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('ui/main.ui', self)
        # home
        self.start_button.clicked.connect(self.to_start)
        self.select_button.clicked.connect(self.continue_with_selected_figure)
        # circle
        self.radius_input.valueChanged.connect(lambda value: self.update_circle_output(value))
        self.home_button.clicked.connect(self.to_home)
        self.next_button_circle.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        # triangle
        self.AB_input.valueChanged.connect(self.update_triangle_output)
        self.BC_input.valueChanged.connect(self.update_triangle_output)
        self.AC_input.valueChanged.connect(self.update_triangle_output)
        self.next_button_triangle_page.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.home_button_triangle_page.clicked.connect(self.to_home)
        # rectangle

    def update_triangle_output(self):
        a, b, c = self.AB_input.value(), self.BC_input.value(), self.AC_input.value()
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        if type(area) is complex or area == 0:
            self.triangle_area_output.setText(f'Not a valid triangle.')
        else:
            self.triangle_area_output.setText(f'{area:.2f}')

    def to_home(self):
        self.stackedWidget.setCurrentIndex(1)

    def to_start(self):
        self.stackedWidget.setCurrentIndex(1)

    def continue_with_selected_figure(self):
        """
        This method is called when the user selects a figure and clicks the continue button.
        The Program chooses the selected ratio button from the button group,
        And if none is selected, The same page is displayed.
        Otherwise, It displays the corresponding page for the selected figure.
        """
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
