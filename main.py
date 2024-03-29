from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import MyMath.formulas as mf
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('ui/main.ui', self)
        self.set_ui_welcome()
        self.set_ui_main()
        self.set_ui_circle()
        self.set_ui_triangle()
        self.set_ui_rectangle()
        self.set_ui_trapezoid()

    def set_ui_welcome(self):
        self.start_button.clicked.connect(self.to_start)

    def set_ui_main(self):
        self.select_button.clicked.connect(self.continue_with_selected_figure)

    def set_ui_circle(self):
        self.radius_input.valueChanged.connect(lambda value: self.handle_circle_input(value))
        self.home_button.clicked.connect(self.to_home)
        self.next_button_circle.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

    def set_ui_triangle(self):
        self.AB_input.valueChanged.connect(self.update_triangle_output)
        self.BC_input.valueChanged.connect(self.update_triangle_output)
        self.AC_input.valueChanged.connect(self.update_triangle_output)
        self.next_button_triangle_page.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.home_button_triangle_page.clicked.connect(self.to_home)

    def set_ui_rectangle(self):
        self.AB_input_rectangle.valueChanged.connect(self.update_rectangle_output)
        self.BC_input_rectangle.valueChanged.connect(self.update_rectangle_output)
        self.home_button_rectangle.clicked.connect(self.to_home)
        self.next_button_rectangle.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))

    def set_ui_trapezoid(self):
        self.AB_input_trapezoid.valueChanged.connect(self.update_trapezoid_output)
        self.BC_input_trapezoid.valueChanged.connect(self.update_trapezoid_output)
        self.CD_input_trapezoid.valueChanged.connect(self.update_trapezoid_output)
        self.AD_input_trapezoid.valueChanged.connect(self.update_trapezoid_output)
        self.home_button_trapezoid.clicked.connect(self.to_home)

    def handle_circle_input(self, value):
        area = mf.circle_area(value)
        length = mf.circle_circumference(value)
        self.circle_area_output.setText(f'{area:.2f}')
        self.circle_length_output.setText(f'{length:.2f}')

    def update_triangle_output(self):
        a, b, c = self.AB_input.value(), self.BC_input.value(), self.AC_input.value()
        area = mf.triangle_area(a, b, c)
        perimeter = mf.triangle_perimeter(a, b, c)
        if type(area) is complex or area == 0:
            self.triangle_area_output.setText(f'Not a valid triangle.')
            self.triangle_perimeter_output.setText(f'Not a valid triangle.')
        else:
            self.triangle_area_output.setText(f'{area:.2f}')
            self.triangle_perimeter_output.setText(f'{perimeter:.2f}')

    def update_rectangle_output(self):
        a, b = self.AB_input_rectangle.value(), self.BC_input_rectangle.value()
        area = mf.rectangle_area(a, b)
        perimeter = mf.rectangle_perimeter(a, b)
        if area > 0:
            self.area_output_rectangle.setText(f'{area:.2f}')
            self.perimeter_output_rectangle.setText(f'{perimeter:.2f}')
        else:
            self.area_output_rectangle.setText(f'Not a valid rectangle.')
            self.perimeter_output_rectangle.setText(f'Not a valid rectangle.')

    def update_trapezoid_output(self):
        a, b, c, d = (self.AB_input_trapezoid.value(), self.BC_input_trapezoid.value(), self.CD_input_trapezoid.value(),
                      self.AD_input_trapezoid.value())
        if a > 0 and b > 0 and c > 0 and d > 0:
            area = mf.trapezoid_area(a, b, c)
            perimeter = mf.trapezoid_perimeter(a, b, c, d)
            self.area_output_trapezoid.setText(f'{area:.2f}')
            self.perimeter_output_trapezoid.setText(f'{perimeter:.2f}')
        else:
            self.area_output_trapezoid.setText(f'Not a valid trapezoid.')
            self.perimeter_output_trapezoid.setText(f'Not a valid trapezoid.')

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


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
