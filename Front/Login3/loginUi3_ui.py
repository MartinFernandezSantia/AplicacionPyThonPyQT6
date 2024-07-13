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
    QPushButton, QSizePolicy, QWidget)
import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(656, 565)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(49, 39, 531, 491))
        self.widget.setStyleSheet(u"QPushButton#pushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton#label:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color:rgba(85, 98, 112, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{\n"
"	color: rgba(131, 96, 53, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
"	padding-left:5px;\n"
""
                        "	padding-top:5px;\n"
"	color:rgba(91, 88, 53, 255);\n"
"}\n"
"\n"
"")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 280, 430))
        self.label.setStyleSheet(u"border-image: url(:/images/background.jpg);\n"
"border-top-left-radius: 50px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QRect(50, 30, 621, 431))
        self.label_2.setMinimumSize(QSize(561, 431))
        self.label_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 80);\n"
"border-top-left-radius: 50px;\n"
"\n"
"/* styles.css */\n"
"\n"
"QLabel{\n"
"    border-top-right-radius: 50px;\n"
"    background-color: rgba(0, 0, 0, 80);\n"
"}\n"
"\n"
"\n"
"")
        self.label_2.setPixmap(QPixmap(u"Login4_recorte.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(269, 30, 231, 431))
        self.label_3.setStyleSheet(u"background-color:rgba(255, 255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(340, 80, 100, 40))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color:rgba(0, 0, 0, 200);")
        self.bt_line_usuario = QLineEdit(self.widget)
        self.bt_line_usuario.setObjectName(u"bt_line_usuario")
        self.bt_line_usuario.setGeometry(QRect(295, 150, 190, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.bt_line_usuario.setFont(font1)
        self.bt_line_usuario.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.bt_line_contrasenia = QLineEdit(self.widget)
        self.bt_line_contrasenia.setObjectName(u"bt_line_contrasenia")
        self.bt_line_contrasenia.setGeometry(QRect(295, 215, 190, 40))
        self.bt_line_contrasenia.setFont(font1)
        self.bt_line_contrasenia.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.bt_line_contrasenia.setEchoMode(QLineEdit.EchoMode.Password)
        self.bt_login_ingreso = QPushButton(self.widget)
        self.bt_login_ingreso.setObjectName(u"bt_login_ingreso")
        self.bt_login_ingreso.setGeometry(QRect(295, 295, 190, 40))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.bt_login_ingreso.setFont(font2)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(290, 340, 191, 20))
        self.label_5.setStyleSheet(u"color:rgba(0, 0, 0, 210);")
        self.horizontalLayoutWidget = QWidget(self.widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(318, 383, 141, 32))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(30, 30))
        font3 = QFont()
        font3.setFamilies([u"Tahoma"])
        font3.setPointSize(15)
        self.pushButton_2.setFont(font3)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(30, 30))
        self.pushButton_3.setFont(font3)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(30, 30))
        self.pushButton_4.setFont(font3)

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(30, 30))
        font4 = QFont()
        font4.setFamilies([u"Tahoma"])
        font4.setPointSize(15)
        font4.setBold(False)
        self.pushButton_5.setFont(font4)

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 190, 221, 91))
        self.label_6.setStyleSheet(u"background-color:rgba(0, 0, 0, 75);")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 190, 180, 40))
        font5 = QFont()
        font5.setPointSize(22)
        font5.setBold(True)
        self.label_7.setFont(font5)
        self.label_7.setStyleSheet(u"color:rgba(255, 255, 255, 200);")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 230, 201, 50))
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        self.label_8.setFont(font6)
        self.label_8.setStyleSheet(u"color:rgba(255, 255, 255, 170);")
        self.bt_login_salir = QLabel(self.widget)
        self.bt_login_salir.setObjectName(u"bt_login_salir")
        self.bt_login_salir.setGeometry(QRect(450, 30, 56, 51))
        self.bt_login_salir.setPixmap(QPixmap(u"Salir.png"))
        self.bt_login_salir.setScaledContents(True)
        self.bt_login_salir.setWordWrap(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Ingreso", None))
        self.bt_line_usuario.setPlaceholderText(QCoreApplication.translate("Form", u"Usuario", None))
        self.bt_line_contrasenia.setPlaceholderText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.bt_login_ingreso.setText(QCoreApplication.translate("Form", u"L O G I N ", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Ingrese Usuario y Contrase\u00f1a", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"4", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"BIENVENIDO", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"       Sistema Control de Lotes.", None))
        self.bt_login_salir.setText("")
    # retranslateUi

