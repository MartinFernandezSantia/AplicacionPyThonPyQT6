from PyQt6.QtCore import Qt, QSize, QRect, QCoreApplication, QMetaObject
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton, QApplication, QGraphicsDropShadowEffect
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(625, 565)
        Form.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        Form.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.widget = QWidget(Form)
        self.widget.setGeometry(QRect(30, 30, 550, 500))
        self.widget.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color:rgba(85, 98, 112, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{\n"
"    color: rgba(131, 96, 53, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(91, 88, 53, 255);\n"
"}\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.label = QLabel(self.widget)
        self.label.setGeometry(QRect(40, 30, 280, 430))
        self.label.setStyleSheet("border-image: url(C:/Users/Cesar/Desktop/loginUi3/background.jpg);\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QLabel(self.widget)
        self.label_2.setGeometry(QRect(40, 30, 280, 430))
        self.label_2.setStyleSheet("background-color:rgba(0, 0, 0, 80);\n"
"border-top-left-radius: 50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setGeometry(QRect(270, 30, 240, 430))
        self.label_3.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setGeometry(QRect(340, 80, 100, 40))
        font = self.label_4.font()
        font.setPointSize(20)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setGeometry(QRect(295, 150, 190, 40))
        font = self.lineEdit.font()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QRect(295, 215, 190, 40))
        font = self.lineEdit_2.font()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setGeometry(QRect(295, 295, 190, 40))
        font = self.pushButton.font()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QLabel(self.widget)
        self.label_5.setGeometry(QRect(301, 345, 181, 16))
        self.label_5.setStyleSheet("color:rgba(0, 0, 0, 210);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget = QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QRect(318, 383, 141, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMaximumSize(QSize(30, 30))
        font = self.pushButton_2.font()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setMaximumSize(QSize(30, 30))
        font = self.pushButton_3.font()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setMaximumSize(QSize(30, 30))
        font = self.pushButton_4.font()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setMaximumSize(QSize(30, 30))
        font = self.pushButton_5.font()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.label_6 = QLabel(self.widget)
        self.label_6.setGeometry(QRect(40, 65, 230, 130))
        self.label_6.setStyleSheet("background-color:rgba(0, 0, 0, 75);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QLabel(self.widget)
        self.label_7.setGeometry(QRect(50, 80, 180, 40))
        font = self.label_7.font()
        font.setPointSize(22)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(255, 255, 255, 200);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QLabel(self.widget)
        self.label_8.setGeometry(QRect(50, 145, 220, 50))
        font = self.label_8.font()
        font.setPointSize(10)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(255, 255, 255, 170);")
        self.label_8.setObjectName("label_8")

        self.label.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Ingreso"))
        self.lineEdit.setPlaceholderText(_translate("Form", "  Usuario"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Contraseña"))
        self.pushButton.setText(_translate("Form", "L O G I N"))
        self.label_5.setText(_translate("Form", "Ingrese Usuario y Contraseña"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_3.setText(_translate("Form", "0"))
        self.pushButton_4.setText(_translate("Form", "2"))
        self.pushButton_5.setText(_translate("Form", "4"))
        self.label_7.setText(_translate("Form", "BIENVENIDO"))
        self.label_8.setText(_translate("Form", "Aplicacion de Gestion de Lotes"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())



