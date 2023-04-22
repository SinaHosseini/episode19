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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(90, 90, 90);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_8_word = QRadioButton(self.centralwidget)
        self.btn_8_word.setObjectName(u"btn_8_word")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_8_word.sizePolicy().hasHeightForWidth())
        self.btn_8_word.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_8_word.setFont(font)
        self.btn_8_word.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(116, 116, 116);")

        self.verticalLayout_2.addWidget(self.btn_8_word)

        self.btn_12_word = QRadioButton(self.centralwidget)
        self.btn_12_word.setObjectName(u"btn_12_word")
        sizePolicy1.setHeightForWidth(self.btn_12_word.sizePolicy().hasHeightForWidth())
        self.btn_12_word.setSizePolicy(sizePolicy1)
        self.btn_12_word.setFont(font)
        self.btn_12_word.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(116, 116, 116);")

        self.verticalLayout_2.addWidget(self.btn_12_word)

        self.btn_20_word = QRadioButton(self.centralwidget)
        self.btn_20_word.setObjectName(u"btn_20_word")
        sizePolicy1.setHeightForWidth(self.btn_20_word.sizePolicy().hasHeightForWidth())
        self.btn_20_word.setSizePolicy(sizePolicy1)
        self.btn_20_word.setFont(font)
        self.btn_20_word.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(116, 116, 116);")

        self.verticalLayout_2.addWidget(self.btn_20_word)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 3, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_24 = QPushButton(self.centralwidget)
        self.pushButton_24.setObjectName(u"pushButton_24")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_24, 0, 0, 1, 1)

        self.pushButton_38 = QPushButton(self.centralwidget)
        self.pushButton_38.setObjectName(u"pushButton_38")
        sizePolicy2.setHeightForWidth(self.pushButton_38.sizePolicy().hasHeightForWidth())
        self.pushButton_38.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_38, 0, 35, 1, 1)

        self.pushButton_46 = QPushButton(self.centralwidget)
        self.pushButton_46.setObjectName(u"pushButton_46")
        sizePolicy2.setHeightForWidth(self.pushButton_46.sizePolicy().hasHeightForWidth())
        self.pushButton_46.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_46, 0, 34, 1, 1)

        self.pushButton_30 = QPushButton(self.centralwidget)
        self.pushButton_30.setObjectName(u"pushButton_30")
        sizePolicy2.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_30, 0, 40, 1, 1)

        self.pushButton_51 = QPushButton(self.centralwidget)
        self.pushButton_51.setObjectName(u"pushButton_51")
        sizePolicy2.setHeightForWidth(self.pushButton_51.sizePolicy().hasHeightForWidth())
        self.pushButton_51.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_51, 0, 30, 1, 1)

        self.pushButton_44 = QPushButton(self.centralwidget)
        self.pushButton_44.setObjectName(u"pushButton_44")
        sizePolicy2.setHeightForWidth(self.pushButton_44.sizePolicy().hasHeightForWidth())
        self.pushButton_44.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_44, 0, 8, 1, 1)

        self.pushButton_36 = QPushButton(self.centralwidget)
        self.pushButton_36.setObjectName(u"pushButton_36")
        sizePolicy2.setHeightForWidth(self.pushButton_36.sizePolicy().hasHeightForWidth())
        self.pushButton_36.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_36, 0, 38, 1, 1)

        self.pushButton_23 = QPushButton(self.centralwidget)
        self.pushButton_23.setObjectName(u"pushButton_23")
        sizePolicy2.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_23, 0, 1, 1, 1)

        self.pushButton_41 = QPushButton(self.centralwidget)
        self.pushButton_41.setObjectName(u"pushButton_41")
        sizePolicy2.setHeightForWidth(self.pushButton_41.sizePolicy().hasHeightForWidth())
        self.pushButton_41.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_41, 0, 17, 1, 1)

        self.pushButton_18 = QPushButton(self.centralwidget)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy2.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_18, 0, 48, 1, 1)

        self.pushButton_47 = QPushButton(self.centralwidget)
        self.pushButton_47.setObjectName(u"pushButton_47")
        sizePolicy2.setHeightForWidth(self.pushButton_47.sizePolicy().hasHeightForWidth())
        self.pushButton_47.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_47, 0, 33, 1, 1)

        self.pushButton_53 = QPushButton(self.centralwidget)
        self.pushButton_53.setObjectName(u"pushButton_53")
        sizePolicy2.setHeightForWidth(self.pushButton_53.sizePolicy().hasHeightForWidth())
        self.pushButton_53.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_53, 0, 27, 1, 1)

        self.pushButton_17 = QPushButton(self.centralwidget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy2.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_17, 0, 49, 1, 1)

        self.pushButton_67 = QPushButton(self.centralwidget)
        self.pushButton_67.setObjectName(u"pushButton_67")
        sizePolicy2.setHeightForWidth(self.pushButton_67.sizePolicy().hasHeightForWidth())
        self.pushButton_67.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_67, 0, 14, 1, 1)

        self.pushButton_29 = QPushButton(self.centralwidget)
        self.pushButton_29.setObjectName(u"pushButton_29")
        sizePolicy2.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_29, 0, 37, 1, 1)

        self.pushButton_66 = QPushButton(self.centralwidget)
        self.pushButton_66.setObjectName(u"pushButton_66")
        sizePolicy2.setHeightForWidth(self.pushButton_66.sizePolicy().hasHeightForWidth())
        self.pushButton_66.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_66, 0, 15, 1, 1)

        self.pushButton_35 = QPushButton(self.centralwidget)
        self.pushButton_35.setObjectName(u"pushButton_35")
        sizePolicy2.setHeightForWidth(self.pushButton_35.sizePolicy().hasHeightForWidth())
        self.pushButton_35.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_35, 0, 39, 1, 1)

        self.pushButton_48 = QPushButton(self.centralwidget)
        self.pushButton_48.setObjectName(u"pushButton_48")
        sizePolicy2.setHeightForWidth(self.pushButton_48.sizePolicy().hasHeightForWidth())
        self.pushButton_48.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_48, 0, 29, 1, 1)

        self.pushButton_59 = QPushButton(self.centralwidget)
        self.pushButton_59.setObjectName(u"pushButton_59")
        sizePolicy2.setHeightForWidth(self.pushButton_59.sizePolicy().hasHeightForWidth())
        self.pushButton_59.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_59, 0, 9, 1, 1)

        self.btn_about = QPushButton(self.centralwidget)
        self.btn_about.setObjectName(u"btn_about")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_about.sizePolicy().hasHeightForWidth())
        self.btn_about.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setPointSize(14)
        self.btn_about.setFont(font1)
        self.btn_about.setStyleSheet(u"background-color: rgb(85, 0, 255);")

        self.gridLayout_3.addWidget(self.btn_about, 0, 50, 1, 1)

        self.pushButton_42 = QPushButton(self.centralwidget)
        self.pushButton_42.setObjectName(u"pushButton_42")
        sizePolicy2.setHeightForWidth(self.pushButton_42.sizePolicy().hasHeightForWidth())
        self.pushButton_42.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_42, 0, 6, 1, 1)

        self.pushButton_19 = QPushButton(self.centralwidget)
        self.pushButton_19.setObjectName(u"pushButton_19")
        sizePolicy2.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_19, 0, 47, 1, 1)

        self.pushButton_34 = QPushButton(self.centralwidget)
        self.pushButton_34.setObjectName(u"pushButton_34")
        sizePolicy2.setHeightForWidth(self.pushButton_34.sizePolicy().hasHeightForWidth())
        self.pushButton_34.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_34, 0, 43, 1, 1)

        self.pushButton_56 = QPushButton(self.centralwidget)
        self.pushButton_56.setObjectName(u"pushButton_56")
        sizePolicy2.setHeightForWidth(self.pushButton_56.sizePolicy().hasHeightForWidth())
        self.pushButton_56.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_56, 0, 7, 1, 1)

        self.pushButton_60 = QPushButton(self.centralwidget)
        self.pushButton_60.setObjectName(u"pushButton_60")
        sizePolicy2.setHeightForWidth(self.pushButton_60.sizePolicy().hasHeightForWidth())
        self.pushButton_60.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_60, 0, 25, 1, 1)

        self.pushButton_43 = QPushButton(self.centralwidget)
        self.pushButton_43.setObjectName(u"pushButton_43")
        sizePolicy2.setHeightForWidth(self.pushButton_43.sizePolicy().hasHeightForWidth())
        self.pushButton_43.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_43, 0, 12, 1, 1)

        self.pushButton_49 = QPushButton(self.centralwidget)
        self.pushButton_49.setObjectName(u"pushButton_49")
        sizePolicy2.setHeightForWidth(self.pushButton_49.sizePolicy().hasHeightForWidth())
        self.pushButton_49.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_49, 0, 32, 1, 1)

        self.pushButton_50 = QPushButton(self.centralwidget)
        self.pushButton_50.setObjectName(u"pushButton_50")
        sizePolicy2.setHeightForWidth(self.pushButton_50.sizePolicy().hasHeightForWidth())
        self.pushButton_50.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_50, 0, 31, 1, 1)

        self.pushButton_31 = QPushButton(self.centralwidget)
        self.pushButton_31.setObjectName(u"pushButton_31")
        sizePolicy2.setHeightForWidth(self.pushButton_31.sizePolicy().hasHeightForWidth())
        self.pushButton_31.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_31, 0, 41, 1, 1)

        self.pushButton_45 = QPushButton(self.centralwidget)
        self.pushButton_45.setObjectName(u"pushButton_45")
        sizePolicy2.setHeightForWidth(self.pushButton_45.sizePolicy().hasHeightForWidth())
        self.pushButton_45.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_45, 0, 20, 1, 1)

        self.pushButton_21 = QPushButton(self.centralwidget)
        self.pushButton_21.setObjectName(u"pushButton_21")
        sizePolicy2.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_21, 0, 45, 1, 1)

        self.pushButton_28 = QPushButton(self.centralwidget)
        self.pushButton_28.setObjectName(u"pushButton_28")
        sizePolicy2.setHeightForWidth(self.pushButton_28.sizePolicy().hasHeightForWidth())
        self.pushButton_28.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_28, 0, 42, 1, 1)

        self.pushButton_52 = QPushButton(self.centralwidget)
        self.pushButton_52.setObjectName(u"pushButton_52")
        sizePolicy2.setHeightForWidth(self.pushButton_52.sizePolicy().hasHeightForWidth())
        self.pushButton_52.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_52, 0, 28, 1, 1)

        self.pushButton_27 = QPushButton(self.centralwidget)
        self.pushButton_27.setObjectName(u"pushButton_27")
        sizePolicy2.setHeightForWidth(self.pushButton_27.sizePolicy().hasHeightForWidth())
        self.pushButton_27.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_27, 0, 44, 1, 1)

        self.pushButton_55 = QPushButton(self.centralwidget)
        self.pushButton_55.setObjectName(u"pushButton_55")
        sizePolicy2.setHeightForWidth(self.pushButton_55.sizePolicy().hasHeightForWidth())
        self.pushButton_55.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_55, 0, 21, 1, 1)

        self.pushButton_62 = QPushButton(self.centralwidget)
        self.pushButton_62.setObjectName(u"pushButton_62")
        sizePolicy2.setHeightForWidth(self.pushButton_62.sizePolicy().hasHeightForWidth())
        self.pushButton_62.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_62, 0, 23, 1, 1)

        self.pushButton_65 = QPushButton(self.centralwidget)
        self.pushButton_65.setObjectName(u"pushButton_65")
        sizePolicy2.setHeightForWidth(self.pushButton_65.sizePolicy().hasHeightForWidth())
        self.pushButton_65.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_65, 0, 16, 1, 1)

        self.pushButton_54 = QPushButton(self.centralwidget)
        self.pushButton_54.setObjectName(u"pushButton_54")
        sizePolicy2.setHeightForWidth(self.pushButton_54.sizePolicy().hasHeightForWidth())
        self.pushButton_54.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_54, 0, 26, 1, 1)

        self.pushButton_63 = QPushButton(self.centralwidget)
        self.pushButton_63.setObjectName(u"pushButton_63")
        sizePolicy2.setHeightForWidth(self.pushButton_63.sizePolicy().hasHeightForWidth())
        self.pushButton_63.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_63, 0, 22, 1, 1)

        self.pushButton_32 = QPushButton(self.centralwidget)
        self.pushButton_32.setObjectName(u"pushButton_32")
        sizePolicy2.setHeightForWidth(self.pushButton_32.sizePolicy().hasHeightForWidth())
        self.pushButton_32.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_32, 0, 2, 1, 1)

        self.pushButton_58 = QPushButton(self.centralwidget)
        self.pushButton_58.setObjectName(u"pushButton_58")
        sizePolicy2.setHeightForWidth(self.pushButton_58.sizePolicy().hasHeightForWidth())
        self.pushButton_58.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_58, 0, 10, 1, 1)

        self.pushButton_25 = QPushButton(self.centralwidget)
        self.pushButton_25.setObjectName(u"pushButton_25")
        sizePolicy2.setHeightForWidth(self.pushButton_25.sizePolicy().hasHeightForWidth())
        self.pushButton_25.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_25, 0, 4, 1, 1)

        self.pushButton_61 = QPushButton(self.centralwidget)
        self.pushButton_61.setObjectName(u"pushButton_61")
        sizePolicy2.setHeightForWidth(self.pushButton_61.sizePolicy().hasHeightForWidth())
        self.pushButton_61.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_61, 0, 24, 1, 1)

        self.pushButton_40 = QPushButton(self.centralwidget)
        self.pushButton_40.setObjectName(u"pushButton_40")
        sizePolicy2.setHeightForWidth(self.pushButton_40.sizePolicy().hasHeightForWidth())
        self.pushButton_40.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_40, 0, 19, 1, 1)

        self.pushButton_26 = QPushButton(self.centralwidget)
        self.pushButton_26.setObjectName(u"pushButton_26")
        sizePolicy2.setHeightForWidth(self.pushButton_26.sizePolicy().hasHeightForWidth())
        self.pushButton_26.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_26, 0, 46, 1, 1)

        self.pushButton_57 = QPushButton(self.centralwidget)
        self.pushButton_57.setObjectName(u"pushButton_57")
        sizePolicy2.setHeightForWidth(self.pushButton_57.sizePolicy().hasHeightForWidth())
        self.pushButton_57.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_57, 0, 11, 1, 1)

        self.pushButton_39 = QPushButton(self.centralwidget)
        self.pushButton_39.setObjectName(u"pushButton_39")
        sizePolicy2.setHeightForWidth(self.pushButton_39.sizePolicy().hasHeightForWidth())
        self.pushButton_39.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_39, 0, 5, 1, 1)

        self.pushButton_64 = QPushButton(self.centralwidget)
        self.pushButton_64.setObjectName(u"pushButton_64")
        sizePolicy2.setHeightForWidth(self.pushButton_64.sizePolicy().hasHeightForWidth())
        self.pushButton_64.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_64, 0, 18, 1, 1)

        self.pushButton_20 = QPushButton(self.centralwidget)
        self.pushButton_20.setObjectName(u"pushButton_20")
        sizePolicy2.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_20, 0, 3, 1, 1)

        self.pushButton_37 = QPushButton(self.centralwidget)
        self.pushButton_37.setObjectName(u"pushButton_37")
        sizePolicy2.setHeightForWidth(self.pushButton_37.sizePolicy().hasHeightForWidth())
        self.pushButton_37.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_37, 0, 36, 1, 1)

        self.pushButton_68 = QPushButton(self.centralwidget)
        self.pushButton_68.setObjectName(u"pushButton_68")
        sizePolicy2.setHeightForWidth(self.pushButton_68.sizePolicy().hasHeightForWidth())
        self.pushButton_68.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_68, 0, 13, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.txt_box = QLineEdit(self.centralwidget)
        self.txt_box.setObjectName(u"txt_box")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.txt_box.sizePolicy().hasHeightForWidth())
        self.txt_box.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.txt_box.setFont(font2)
        self.txt_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_box.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.txt_box)

        self.lineEdit_41 = QLineEdit(self.centralwidget)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineEdit_41.sizePolicy().hasHeightForWidth())
        self.lineEdit_41.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_41)

        self.lineEdit_40 = QLineEdit(self.centralwidget)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        sizePolicy5.setHeightForWidth(self.lineEdit_40.sizePolicy().hasHeightForWidth())
        self.lineEdit_40.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_40)

        self.lineEdit_39 = QLineEdit(self.centralwidget)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        sizePolicy5.setHeightForWidth(self.lineEdit_39.sizePolicy().hasHeightForWidth())
        self.lineEdit_39.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_39)

        self.lineEdit_38 = QLineEdit(self.centralwidget)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        sizePolicy5.setHeightForWidth(self.lineEdit_38.sizePolicy().hasHeightForWidth())
        self.lineEdit_38.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_38)

        self.lineEdit_37 = QLineEdit(self.centralwidget)
        self.lineEdit_37.setObjectName(u"lineEdit_37")
        sizePolicy5.setHeightForWidth(self.lineEdit_37.sizePolicy().hasHeightForWidth())
        self.lineEdit_37.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_37)

        self.lineEdit_36 = QLineEdit(self.centralwidget)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        sizePolicy5.setHeightForWidth(self.lineEdit_36.sizePolicy().hasHeightForWidth())
        self.lineEdit_36.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_36)

        self.lineEdit_35 = QLineEdit(self.centralwidget)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        sizePolicy5.setHeightForWidth(self.lineEdit_35.sizePolicy().hasHeightForWidth())
        self.lineEdit_35.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_35)

        self.lineEdit_34 = QLineEdit(self.centralwidget)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        sizePolicy5.setHeightForWidth(self.lineEdit_34.sizePolicy().hasHeightForWidth())
        self.lineEdit_34.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_34)

        self.lineEdit_33 = QLineEdit(self.centralwidget)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        sizePolicy5.setHeightForWidth(self.lineEdit_33.sizePolicy().hasHeightForWidth())
        self.lineEdit_33.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_33)

        self.lineEdit_32 = QLineEdit(self.centralwidget)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        sizePolicy5.setHeightForWidth(self.lineEdit_32.sizePolicy().hasHeightForWidth())
        self.lineEdit_32.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_32)

        self.lineEdit_31 = QLineEdit(self.centralwidget)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        sizePolicy5.setHeightForWidth(self.lineEdit_31.sizePolicy().hasHeightForWidth())
        self.lineEdit_31.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_31)

        self.lineEdit_30 = QLineEdit(self.centralwidget)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        sizePolicy5.setHeightForWidth(self.lineEdit_30.sizePolicy().hasHeightForWidth())
        self.lineEdit_30.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_30)

        self.lineEdit_29 = QLineEdit(self.centralwidget)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        sizePolicy5.setHeightForWidth(self.lineEdit_29.sizePolicy().hasHeightForWidth())
        self.lineEdit_29.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_29)

        self.lineEdit_28 = QLineEdit(self.centralwidget)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        sizePolicy5.setHeightForWidth(self.lineEdit_28.sizePolicy().hasHeightForWidth())
        self.lineEdit_28.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_28)

        self.lineEdit_27 = QLineEdit(self.centralwidget)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        sizePolicy5.setHeightForWidth(self.lineEdit_27.sizePolicy().hasHeightForWidth())
        self.lineEdit_27.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_27)

        self.lineEdit_26 = QLineEdit(self.centralwidget)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        sizePolicy5.setHeightForWidth(self.lineEdit_26.sizePolicy().hasHeightForWidth())
        self.lineEdit_26.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_26)

        self.lineEdit_25 = QLineEdit(self.centralwidget)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        sizePolicy5.setHeightForWidth(self.lineEdit_25.sizePolicy().hasHeightForWidth())
        self.lineEdit_25.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_25)

        self.lineEdit_24 = QLineEdit(self.centralwidget)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        sizePolicy5.setHeightForWidth(self.lineEdit_24.sizePolicy().hasHeightForWidth())
        self.lineEdit_24.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_24)

        self.lineEdit_23 = QLineEdit(self.centralwidget)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        sizePolicy5.setHeightForWidth(self.lineEdit_23.sizePolicy().hasHeightForWidth())
        self.lineEdit_23.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_23)

        self.lineEdit_11 = QLineEdit(self.centralwidget)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy5.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_11)

        self.lineEdit_10 = QLineEdit(self.centralwidget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        sizePolicy5.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_10)

        self.lineEdit_9 = QLineEdit(self.centralwidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        sizePolicy5.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_9)

        self.lineEdit_8 = QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy5.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_8)

        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy5.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_7)

        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy5.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_6)

        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy5.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_5)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy5.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_4)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy5.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_3)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy5.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit_2)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy5.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.lineEdit)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 2, 0, 1, 2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy2.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_13, 4, 6, 1, 1)

        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy2.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_10, 2, 4, 1, 1)

        self.pushButton_15 = QPushButton(self.centralwidget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy2.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_15, 4, 3, 1, 1)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy2.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_9, 8, 4, 1, 1)

        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy2.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_11, 4, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_4, 4, 8, 1, 1)

        self.pushButton_33 = QPushButton(self.centralwidget)
        self.pushButton_33.setObjectName(u"pushButton_33")
        sizePolicy2.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_33, 4, 5, 1, 1)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy2.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_8, 4, 7, 1, 1)

        self.btn_generate = QPushButton(self.centralwidget)
        self.btn_generate.setObjectName(u"btn_generate")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btn_generate.sizePolicy().hasHeightForWidth())
        self.btn_generate.setSizePolicy(sizePolicy6)
        font3 = QFont()
        font3.setPointSize(40)
        font3.setBold(True)
        self.btn_generate.setFont(font3)
        self.btn_generate.setStyleSheet(u"background-color: rgb(250, 155, 0);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.btn_generate, 4, 4, 1, 1)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy2.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_7, 4, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy2.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_5, 9, 4, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy2.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_6, 1, 4, 1, 1)

        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy2.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_12, 7, 4, 1, 1)

        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy2.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_14, 3, 4, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_2, 0, 4, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 1)

        self.pushButton_16 = QPushButton(self.centralwidget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy2.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_16, 6, 4, 1, 1)

        self.btn_res = QPushButton(self.centralwidget)
        self.btn_res.setObjectName(u"btn_res")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_res.sizePolicy().hasHeightForWidth())
        self.btn_res.setSizePolicy(sizePolicy7)
        font4 = QFont()
        font4.setPointSize(40)
        self.btn_res.setFont(font4)
        self.btn_res.setStyleSheet(u"background-color: rgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.btn_res, 5, 4, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 3, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_8_word.setText(QCoreApplication.translate("MainWindow", u"Standard Strength Password(8 characters)", None))
        self.btn_12_word.setText(QCoreApplication.translate("MainWindow", u"Extra Strong Password(12 characters)", None))
        self.btn_20_word.setText(QCoreApplication.translate("MainWindow", u"Super Strong Password(20 characters)", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_53.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_67.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_66.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_59.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"about", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_56.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_60.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_55.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_62.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_65.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_54.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_63.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_58.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_61.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_57.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_64.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_68.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_generate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_res.setText(QCoreApplication.translate("MainWindow", u"Reset pass", None))
    # retranslateUi

