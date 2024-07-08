# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginUi3.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(956, 728)
        font = QFont()
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: rgba(100, 150, 200, 0.8);\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 0, 211, 411))
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setStyleSheet(u"background-color:rgba(255, 255, 255, 255);\n"
"border-radius:10px;\n"
"")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 25, 270, 360))
        self.label_2.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 80, 80, 255), stop:0.1 rgba(0, 100, 100, 255), stop:1 rgba(0, 255, 150, 255));\n"
"\n"
"\n"
"border-radius:10px;\n"
"\n"
"")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(350, 30, 101, 19))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color:rgba(0,0,0, 200);")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(330, 80, 141, 25))
        self.lineEdit.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;")
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(330, 160, 141, 25))
        self.lineEdit_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(330, 290, 141, 40))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.pushButton.setFont(font2)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(330, 360, 141, 19))
        font3 = QFont()
        font3.setBold(False)
        self.label_4.setFont(font3)
        self.label_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_4.setStyleSheet(u"border-radius:10px;\n"
"background-color:rgba(0,0,0,0);\n"
"\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 50, 161, 41))
        font4 = QFont()
        font4.setPointSize(22)
        font4.setBold(True)
        self.label_5.setFont(font4)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 80, 231, 71))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setItalic(False)
        self.label_6.setFont(font5)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 210, 261, 171))
        font6 = QFont()
        font6.setFamilies([u"HoloLens MDL2 Assets"])
        font6.setPointSize(290)
        font6.setBold(False)
        font6.setItalic(True)
        font6.setUnderline(False)
        font6.setStrikeOut(True)
        self.label_7.setFont(font6)
        self.label_7.setStyleSheet(u"color: rgba(0, 225, 199, 0.4);\n"
"\n"
"\n"
"\n"
"")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(80, 250, 181, 19))
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_8.setStyleSheet(u"border-radius:10px;\n"
"background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(90, 270, 161, 20))
        self.label_9.setFont(font3)
        self.label_9.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_9.setStyleSheet(u"border-radius:10px;\n"
"background-color:rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(80, 290, 181, 20))
        self.label_10.setFont(font3)
        self.label_10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_10.setStyleSheet(u"border-radius:10px;\n"
"background-color:rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"L O G I N ", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"            Usuario", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"        Contrase\u00f1a ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"I N G R E S A R ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Copyright", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Bienvenido", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Al sistema de Usuario  \n"
" Control de Lotes ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\ue7a9", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Programado y Dise\u00f1ado", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u2022 Cesar Augusto Da Silva ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u2022 Martin Fernandez Santia", None))
    # retranslateUi

