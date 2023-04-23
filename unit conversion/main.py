import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.convert_box.currentIndexChanged.connect(self.convert_type)
        self.ui.calculate_btn.clicked.connect(self.calculate)
        self.ui.reset_btn.clicked.connect(self.reset)

    def convert_type(self):
        if self.ui.convert_box.currentText() == "Mass":
            self.ui.from_box.clear()
            self.ui.from_box.addItems(["Grams", "Kilograms", "Ton", "Pound"])
            self.ui.to_box.clear()
            self.ui.to_box.addItems(["Grams", "Kilograms", "Ton", "Pound"])

        elif self.ui.convert_box.currentText() == "Length":
            self.ui.from_box.clear()
            self.ui.from_box.addItems(
                ["Millimeter", "Centimeter", "Meter", "Kilometer", "Inch"])
            self.ui.to_box.clear()
            self.ui.to_box.addItems(
                ["Millimeter", "Centimeter", "Meter", "Kilometer", "Inch"])

        elif self.ui.convert_box.currentText() == "Temperature":
            self.ui.from_box.clear()
            self.ui.from_box.addItems(["Celsius", "Fahrenheit", "Kelvin"])
            self.ui.to_box.clear()
            self.ui.to_box.addItems(["Celsius", "Fahrenheit", "Kelvin"])

        elif self.ui.convert_box.currentText() == "Digital volume":
            self.ui.from_box.clear()
            self.ui.from_box.addItems(
                ["bit", "byte", "Kilobytes", "megabyte", "Gigabytes", "Terabytes"])
            self.ui.to_box.clear()
            self.ui.to_box.addItems(
                ["bit", "byte", "Kilobytes", "Megabyte", "Gigabytes", "Terabytes"])

    def calculate(self):
        if self.ui.convert_box.currentText() == "Mass":
            if self.ui.from_box.currentText() == "Grams":
                if self.ui.to_box.currentText() == "Grams":
                    self.numericalـvalue = float(self.ui.input_box.text())

                elif self.ui.to_box.currentText() == "Kilograms":
                    self.numericalـvalue = (
                        float(self.ui.input_box.text()) / 1000)

                elif self.ui.to_box.currentText() == "Ton":
                    self.numericalـvalue = (
                        float(self.ui.input_box.text()) / 1000000)

                elif self.ui.to_box.currentText() == "Pound":
                    self.numericalـvalue = (
                        float(self.ui.input_box.text()) / 453)

                self.ui.output_box.setText(str(self.numericalـvalue))

            elif self.ui.from_box.currentText() == "Kilograms":
                if self.ui.to_box.currentText() == "Grams":
                    self.numericalـvalue = (
                        float(self.ui.input_box.text()) * 1000)

                elif self.ui.to_box.currentText() == "Kilograms":
                    self.numericalـvalue = float(self.ui.input_box.text())

                elif self.ui.to_box.currentText() == "Ton":
                    self.numericalـvalue = (
                        float(self.ui.input_box.text()) / 1000)

                elif self.ui.to_box.currentText() == "Pound":
                    self.numericalـvalue = (
                        (float(self.ui.input_box.text()) * 1000) / 453)

                self.ui.output_box.setText(str(self.numericalـvalue))

            elif self.ui.from_box.currentText() == "Ton":
                if self.ui.to_box.currentText() == "Grams":
                    self.numericalـvalue = (
                        float(self.ui.input_box.text()) * 1000000)

                elif self.ui.to_box.currentText() == "Kilograms":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1000

                elif self.ui.to_box.currentText() == "Ton":
                    self.numericalـvalue = float(self.ui.input_box.text())

                elif self.ui.to_box.currentText() == "Pound":
                    self.numericalـvalue = (
                        (float(self.ui.input_box.text()) * 1000000) / 453)

                self.ui.output_box.setText(str(self.numericalـvalue))

            elif self.ui.from_box.currentText() == "Pound":
                if self.ui.to_box.currentText() == "Grams":
                    self.numericalـvalue = (
                        float(self.ui.input_box.text()) * 453)

                elif self.ui.to_box.currentText() == "Kilograms":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 453 / 1000

                elif self.ui.to_box.currentText() == "Ton":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 453 / 1000000

                elif self.ui.to_box.currentText() == "Pound":
                    self.numericalـvalue = float(self.ui.input_box.text())

                self.ui.output_box.setText(str(self.numericalـvalue))

        elif self.ui.convert_box.currentText() == "Length":
            if self.ui.from_box.currentText() == "Millimeter":
                if self.ui.to_box.currentText() == "Millimeter":
                    self.numericalـvalue = float(self.ui.input_box.text())

                elif self.ui.to_box.currentText() == "Centimeter":
                    self.numericalـvalue = float(self.ui.input_box.text()) / 10

                elif self.ui.to_box.currentText() == "Meter":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) / 1000

                elif self.ui.to_box.currentText() == "Kilometer":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) / 1000000

                elif self.ui.to_box.currentText() == "Inch":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) / ...

                self.ui.output_box.setText(str(self.numericalـvalue))

    def reset(self):
        self.ui.input_box.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()
