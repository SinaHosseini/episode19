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
                        self.ui.input_box.text()) * 0.04

                self.ui.output_box.setText(str(self.numericalـvalue))

            elif self.ui.from_box.currentText() == "Centimeter":
                if self.ui.to_box.currentText() == "Millimeter":
                    self.numericalـvalue = float(self.ui.input_box.text()) * 10

                elif self.ui.to_box.currentText() == "Centimeter":
                    self.numericalـvalue = float(self.ui.input_box.text())

                elif self.ui.to_box.currentText() == "Meter":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) / 100

                elif self.ui.to_box.currentText() == "Kilometer":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) / 100000

                elif self.ui.to_box.currentText() == "Inch":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 0.4

                self.ui.output_box.setText(str(self.numericalـvalue))

            elif self.ui.from_box.currentText() == "Meter":
                if self.ui.to_box.currentText() == "Millimeter":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1000

                elif self.ui.to_box.currentText() == "Centimeter":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 100

                elif self.ui.to_box.currentText() == "Meter":
                    self.numericalـvalue = float(
                        self.ui.input_box.text())

                elif self.ui.to_box.currentText() == "Kilometer":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) / 1000

                elif self.ui.to_box.currentText() == "Inch":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 39

                self.ui.output_box.setText(str(self.numericalـvalue))

            elif self.ui.from_box.currentText() == "Kilometer":
                if self.ui.to_box.currentText() == "Millimeter":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1000000

                elif self.ui.to_box.currentText() == "Centimeter":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 100000

                elif self.ui.to_box.currentText() == "Meter":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1000

                elif self.ui.to_box.currentText() == "Kilometer":
                    self.numericalـvalue = float(
                        self.ui.input_box.text())

                elif self.ui.to_box.currentText() == "Inch":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 39370

                self.ui.output_box.setText(str(self.numericalـvalue))

            elif self.ui.from_box.currentText() == "Inch":
                if self.ui.to_box.currentText() == "Millimeter":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 25

                elif self.ui.to_box.currentText() == "Centimeter":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 2.54

                elif self.ui.to_box.currentText() == "Meter":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 0.03

                elif self.ui.to_box.currentText() == "Kilometer":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 0.00003

                elif self.ui.to_box.currentText() == "Inch":
                    self.numericalـvalue = float(
                        self.ui.input_box.text())

                self.ui.output_box.setText(str(self.numericalـvalue))

        elif self.ui.convert_box.currentText() == "Temperature":
            if self.ui.from_box.currentText() == "Celsius":
                if self.ui.to_box.currentText() == "Celsius":
                    self.numericalـvalue = float(self.ui.input_box.text())

                elif self.ui.to_box.currentText() == "Fahrenheit":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1.8 + 32

                elif self.ui.to_box.currentText() == "Kelvin":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) + 274.15

                self.ui.output_box.setText(str(self.numericalـvalue))

            elif self.ui.to_box.currentText() == "Fahrenheit":
                if self.ui.to_box.currentText() == "Celsius":
                    self.numericalـvalue = float(self.ui.input_box.text())
                    self.numericalـvalue = (self.numericalـvalue - 32) / 2

                elif self.ui.to_box.currentText() == "Fahrenheit":
                    self.numericalـvalue = float(self.ui.input_box.text())

                elif self.ui.to_box.currentText() == "Kelvin":
                    self.numericalـvalue = float(self.ui.input_box.text())
                    self.numericalـvalue = (self.numericalـvalue + 459.67) / 2

                self.ui.output_box.setText(str(self.numericalـvalue))

            elif self.ui.to_box.currentText() == "Kelvin":
                if self.ui.to_box.currentText() == "Celsius":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) - 273.15

                elif self.ui.to_box.currentText() == "Fahrenheit":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1.8 + 459.67

                elif self.ui.to_box.currentText() == "Kelvin":
                    self.numericalـvalue = float(
                        self.ui.input_box.text())

                self.ui.output_box.setText(str(self.numericalـvalue))

        elif self.ui.convert_box.currentText() == "Digital volume":
            if self.ui.from_box.currentText() == "bit":
                if self.ui.to_box.currentText() == "bit":
                    self.numericalـvalue = float(self.ui.input_box.text())

                elif self.ui.to_box.currentText() == "byte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 0.125

                elif self.ui.to_box.currentText() == "Kilobyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 0.001

                elif self.ui.to_box.currentText() == "Megabyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1.25e-7

                elif self.ui.to_box.currentText() == "Gigabyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1.25e-10

                elif self.ui.to_box.currentText() == "Terabyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1.25e-13

                self.ui.output_box.setText(str(self.numericalـvalue))

            elif self.ui.from_box.currentText() == "byte":
                if self.ui.to_box.currentText() == "bit":
                    self.numericalـvalue = float(self.ui.input_box.text()) * 8

                elif self.ui.to_box.currentText() == "byte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text())

                elif self.ui.to_box.currentText() == "Kilobyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 0.001

                elif self.ui.to_box.currentText() == "Megabyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 0.000001

                elif self.ui.to_box.currentText() == "Gigabyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1e-9

                elif self.ui.to_box.currentText() == "Terabyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1e-12

                self.ui.output_box.setText(str(self.numericalـvalue))

            elif self.ui.from_box.currentText() == "Kilobyte":
                if self.ui.to_box.currentText() == "bit":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 8000

                elif self.ui.to_box.currentText() == "byte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1000

                elif self.ui.to_box.currentText() == "Kilobyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text())

                elif self.ui.to_box.currentText() == "Megabyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 0.001

                elif self.ui.to_box.currentText() == "Gigabyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 0.000001

                elif self.ui.to_box.currentText() == "Terabyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1e-9

                self.ui.output_box.setText(str(self.numericalـvalue))

            elif self.ui.from_box.currentText() == "Megabyte":
                if self.ui.to_box.currentText() == "bit":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 8000000

                elif self.ui.to_box.currentText() == "byte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1000000

                elif self.ui.to_box.currentText() == "Kilobyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1000

                elif self.ui.to_box.currentText() == "Megabyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text())

                elif self.ui.to_box.currentText() == "Gigabyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 0.001

                elif self.ui.to_box.currentText() == "Terabyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 0.000001

                self.ui.output_box.setText(str(self.numericalـvalue))

            elif self.ui.from_box.currentText() == "Gigabyte":
                if self.ui.to_box.currentText() == "bit":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 8000000000

                elif self.ui.to_box.currentText() == "byte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1000000000

                elif self.ui.to_box.currentText() == "Kilobyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1000000

                elif self.ui.to_box.currentText() == "Megabyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1000

                elif self.ui.to_box.currentText() == "Gigabyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text())

                elif self.ui.to_box.currentText() == "Terabyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 0.001

                self.ui.output_box.setText(str(self.numericalـvalue))

            elif self.ui.from_box.currentText() == "Terabyte":
                if self.ui.to_box.currentText() == "bit":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 8000000000000

                elif self.ui.to_box.currentText() == "byte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1000000000000

                elif self.ui.to_box.currentText() == "Kilobyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1000000000

                elif self.ui.to_box.currentText() == "Megabyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1000000

                elif self.ui.to_box.currentText() == "Gigabyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text()) * 1000

                elif self.ui.to_box.currentText() == "Terabyte":
                    self.numericalـvalue = float(
                        self.ui.input_box.text())

                self.ui.output_box.setText(str(self.numericalـvalue))

    def reset(self):
        self.ui.input_box.setText("")
        self.ui.output_box.setText("")
        self.numericalـvalue = ""


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()
