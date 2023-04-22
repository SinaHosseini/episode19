import sys
import random
import string
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.password_length = 0
        self.words_list = list(string.ascii_letters +
                               string.digits + string.punctuation)

        self.ui.btn_8_word.clicked.connect(self.password_mode)
        self.ui.btn_12_word.clicked.connect(self.password_mode)
        self.ui.btn_20_word.clicked.connect(self.password_mode)
        self.ui.btn_generate.clicked.connect(self.show_password)
        self.ui.btn_res.clicked.connect(self.reset)
        self.ui.btn_about.clicked.connect(self.about)

    def password_mode(self):
        if self.ui.btn_8_word.isChecked():
            self.password_length = 8
            self.password = ''.join(random.sample(
                self.words_list, self.password_length))

        elif self.ui.btn_12_word.isChecked():
            self.password_length = 12
            self.password = ''.join(random.sample(
                self.words_list, self.password_length))

        elif self.ui.btn_20_word.isChecked():
            self.password_length = 20
            self.password = ''.join(random.sample(
                self.words_list, self.password_length))

    def show_password(self):
        self.ui.txt_box.setText("")
        self.ui.txt_box.setText(self.password)

    def reset(self):
        self.ui.txt_box.setText("")

    def about(self):
        msg_box = QMessageBox()
        msg_box.setText(
            "First, you choose the length of your password, then press the generate button and receive your password\nReset button to clear the text box ")
        msg_box.exec()


app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()
