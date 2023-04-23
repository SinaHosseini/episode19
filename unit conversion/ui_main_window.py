# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(628, 313)
        MainWindow.setStyleSheet(u"background-color: rgb(239, 239, 239);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_7 = QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setContentsMargins(190, 10, 190, 0)
        self.convert_box = QComboBox(self.centralwidget)
        self.convert_box.addItem("")
        self.convert_box.addItem("")
        self.convert_box.addItem("")
        self.convert_box.addItem("")
        self.convert_box.addItem("")
        self.convert_box.setObjectName(u"convert_box")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.convert_box.sizePolicy().hasHeightForWidth())
        self.convert_box.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.convert_box, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout, 0, 0, 1, 2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, -1, 75, -1)
        self.outout_txt = QLineEdit(self.centralwidget)
        self.outout_txt.setObjectName(u"outout_txt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.outout_txt.sizePolicy().hasHeightForWidth())
        self.outout_txt.setSizePolicy(sizePolicy1)
        self.outout_txt.setStyleSheet(u"background-color: rgb(239, 239, 239);")
        self.outout_txt.setReadOnly(True)

        self.gridLayout_4.addWidget(self.outout_txt, 2, 0, 1, 1)

        self.to_box = QComboBox(self.centralwidget)
        self.to_box.setObjectName(u"to_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.to_box.sizePolicy().hasHeightForWidth())
        self.to_box.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.to_box, 1, 0, 1, 1)

        self.to_txt = QLineEdit(self.centralwidget)
        self.to_txt.setObjectName(u"to_txt")
        sizePolicy1.setHeightForWidth(self.to_txt.sizePolicy().hasHeightForWidth())
        self.to_txt.setSizePolicy(sizePolicy1)
        self.to_txt.setStyleSheet(u"background-color: rgb(239, 239, 239);")
        self.to_txt.setReadOnly(True)

        self.gridLayout_4.addWidget(self.to_txt, 0, 0, 1, 1)

        self.output_box = QLineEdit(self.centralwidget)
        self.output_box.setObjectName(u"output_box")
        self.output_box.setReadOnly(True)

        self.gridLayout_4.addWidget(self.output_box, 3, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_4, 1, 1, 1, 1)

        self.calculate_btn = QPushButton(self.centralwidget)
        self.calculate_btn.setObjectName(u"calculate_btn")
        sizePolicy1.setHeightForWidth(self.calculate_btn.sizePolicy().hasHeightForWidth())
        self.calculate_btn.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.calculate_btn, 2, 1, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, -1, 75, -1)
        self.from_box = QComboBox(self.centralwidget)
        self.from_box.setObjectName(u"from_box")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.from_box.sizePolicy().hasHeightForWidth())
        self.from_box.setSizePolicy(sizePolicy3)

        self.gridLayout_5.addWidget(self.from_box, 1, 0, 1, 1)

        self.input_box = QLineEdit(self.centralwidget)
        self.input_box.setObjectName(u"input_box")

        self.gridLayout_5.addWidget(self.input_box, 3, 0, 1, 1)

        self.frome_txt = QLineEdit(self.centralwidget)
        self.frome_txt.setObjectName(u"frome_txt")
        sizePolicy1.setHeightForWidth(self.frome_txt.sizePolicy().hasHeightForWidth())
        self.frome_txt.setSizePolicy(sizePolicy1)
        self.frome_txt.setStyleSheet(u"background-color: rgb(239, 239, 239);")
        self.frome_txt.setReadOnly(True)

        self.gridLayout_5.addWidget(self.frome_txt, 0, 0, 1, 1)

        self.input_txt = QLineEdit(self.centralwidget)
        self.input_txt.setObjectName(u"input_txt")
        sizePolicy1.setHeightForWidth(self.input_txt.sizePolicy().hasHeightForWidth())
        self.input_txt.setSizePolicy(sizePolicy1)
        self.input_txt.setStyleSheet(u"background-color: rgb(239, 239, 239);")
        self.input_txt.setReadOnly(True)

        self.gridLayout_5.addWidget(self.input_txt, 2, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_5, 1, 0, 1, 1)

        self.reset_btn = QPushButton(self.centralwidget)
        self.reset_btn.setObjectName(u"reset_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.reset_btn.sizePolicy().hasHeightForWidth())
        self.reset_btn.setSizePolicy(sizePolicy4)

        self.gridLayout_7.addWidget(self.reset_btn, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 628, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.convert_box.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.convert_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Mass", None))
        self.convert_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Length", None))
        self.convert_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.convert_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Digital volume", None))

        self.outout_txt.setText(QCoreApplication.translate("MainWindow", u"output:", None))
        self.to_txt.setText(QCoreApplication.translate("MainWindow", u"to:", None))
        self.calculate_btn.setText(QCoreApplication.translate("MainWindow", u"calculate", None))
        self.frome_txt.setText(QCoreApplication.translate("MainWindow", u"from:", None))
        self.input_txt.setText(QCoreApplication.translate("MainWindow", u"input:", None))
        self.reset_btn.setText(QCoreApplication.translate("MainWindow", u"reset", None))
    # retranslateUi

