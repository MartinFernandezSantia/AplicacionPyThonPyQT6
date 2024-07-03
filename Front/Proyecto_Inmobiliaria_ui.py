# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Proyecto_Inmobiliaria.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1050, 687)
        MainWindow.setMinimumSize(QSize(200, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 42))
        self.frame_superior.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #000000;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 61, 61);\n"
"    border-radius: 20px;\n"
"}\n"
"")
        self.frame_superior.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bt_menu = QPushButton(self.frame_superior)
        self.bt_menu.setObjectName(u"bt_menu")
        self.bt_menu.setMinimumSize(QSize(200, 0))
        icon = QIcon()
        icon.addFile(u"img/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QSize(38, 38))

        self.horizontalLayout.addWidget(self.bt_menu)

        self.horizontalSpacer = QSpacerItem(635, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bt_restaurar = QPushButton(self.frame_superior)
        self.bt_restaurar.setObjectName(u"bt_restaurar")
        self.bt_restaurar.setMinimumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u"img/minus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_restaurar.setIcon(icon1)
        self.bt_restaurar.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.bt_restaurar)

        self.bt_minimizar = QPushButton(self.frame_superior)
        self.bt_minimizar.setObjectName(u"bt_minimizar")
        self.bt_minimizar.setMinimumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(u"img/minimize-2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_minimizar.setIcon(icon2)
        self.bt_minimizar.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.bt_minimizar)

        self.bt_maximizar = QPushButton(self.frame_superior)
        self.bt_maximizar.setObjectName(u"bt_maximizar")
        self.bt_maximizar.setMinimumSize(QSize(40, 40))
        icon3 = QIcon()
        icon3.addFile(u"img/maximize-2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_maximizar.setIcon(icon3)
        self.bt_maximizar.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.bt_maximizar)

        self.bt_cerrar = QPushButton(self.frame_superior)
        self.bt_cerrar.setObjectName(u"bt_cerrar")
        self.bt_cerrar.setMinimumSize(QSize(40, 40))
        icon4 = QIcon()
        icon4.addFile(u"img/x.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_cerrar.setIcon(icon4)
        self.bt_cerrar.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.bt_cerrar)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_contenido = QFrame(self.frame)
        self.frame_contenido.setObjectName(u"frame_contenido")
        self.frame_contenido.setMinimumSize(QSize(200, 0))
        self.frame_contenido.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_contenido.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_contenido)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_control = QFrame(self.frame_contenido)
        self.frame_control.setObjectName(u"frame_control")
        self.frame_control.setMinimumSize(QSize(200, 0))
        self.frame_control.setMaximumSize(QSize(0, 16777215))
        self.frame_control.setStyleSheet(u"\n"
"QFrame{\n"
"background-color:rgb(0, 206, 151);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:rgb(61, 61, 61);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 77 10pt\"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(0, 0, 0);\n"
"font: 77 10pt\"Arial Black\";\n"
"}")
        self.frame_control.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_control.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_control)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.bt_datos = QPushButton(self.frame_control)
        self.bt_datos.setObjectName(u"bt_datos")
        self.bt_datos.setMinimumSize(QSize(0, 40))
        icon5 = QIcon()
        icon5.addFile(u"img/database.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_datos.setIcon(icon5)
        self.bt_datos.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.bt_datos)

        self.bt_registrar = QPushButton(self.frame_control)
        self.bt_registrar.setObjectName(u"bt_registrar")
        self.bt_registrar.setMinimumSize(QSize(0, 40))
        icon6 = QIcon()
        icon6.addFile(u"img/file-plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_registrar.setIcon(icon6)
        self.bt_registrar.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.bt_registrar)

        self.bt_actualizar_2 = QPushButton(self.frame_control)
        self.bt_actualizar_2.setObjectName(u"bt_actualizar_2")
        self.bt_actualizar_2.setMinimumSize(QSize(0, 40))
        icon7 = QIcon()
        icon7.addFile(u"img/upload-cloud.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_actualizar_2.setIcon(icon7)
        self.bt_actualizar_2.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.bt_actualizar_2)

        self.bt_eliminar_menu = QPushButton(self.frame_control)
        self.bt_eliminar_menu.setObjectName(u"bt_eliminar_menu")
        self.bt_eliminar_menu.setMinimumSize(QSize(0, 40))
        icon8 = QIcon()
        icon8.addFile(u"img/trash-2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_eliminar_menu.setIcon(icon8)
        self.bt_eliminar_menu.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.bt_eliminar_menu)

        self.bt_ajustes = QPushButton(self.frame_control)
        self.bt_ajustes.setObjectName(u"bt_ajustes")
        self.bt_ajustes.setMinimumSize(QSize(0, 40))
        icon9 = QIcon()
        icon9.addFile(u"img/tool.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_ajustes.setIcon(icon9)
        self.bt_ajustes.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.bt_ajustes)


        self.horizontalLayout_2.addWidget(self.frame_control)

        self.frame_paginas = QFrame(self.frame_contenido)
        self.frame_paginas.setObjectName(u"frame_paginas")
        self.frame_paginas.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QLabel {\n"
"    font: 87 12pt \"Arial Black\";\n"
"    background-color: #000000;\n"
"    color: rgb(0, 206, 151);\n"
"    border: 0px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 0px;\n"
"    color: rgb(255, 255, 255);\n"
"    border-bottom: 2px solid rgb(61, 61, 61);\n"
"    font: 75 12pt \"Times New Roman\";\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(61, 61, 61);\n"
"    border-radius: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    gridline-color: rgb(0, 206, 151);\n"
"    font-size: 12pt;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(0, 206, 151);\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: rgb(0, 0, 0);\n"
"    border: 1px soli"
                        "d rgb(0, 206, 151);\n"
"}\n"
"")
        self.frame_paginas.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_paginas.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_paginas)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_paginas)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_actualizar = QWidget()
        self.page_actualizar.setObjectName(u"page_actualizar")
        self.verticalLayout_10 = QVBoxLayout(self.page_actualizar)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_15 = QLabel(self.page_actualizar)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_15)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.page_actualizar)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.actualizar_buscar = QLineEdit(self.page_actualizar)
        self.actualizar_buscar.setObjectName(u"actualizar_buscar")

        self.horizontalLayout_9.addWidget(self.actualizar_buscar)

        self.bt_buscar_actualizar = QPushButton(self.page_actualizar)
        self.bt_buscar_actualizar.setObjectName(u"bt_buscar_actualizar")
        self.bt_buscar_actualizar.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_9.addWidget(self.bt_buscar_actualizar)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(30)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_13 = QLabel(self.page_actualizar)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_9.addWidget(self.label_13)

        self.label_12 = QLabel(self.page_actualizar)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_9.addWidget(self.label_12)

        self.label_10 = QLabel(self.page_actualizar)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_9.addWidget(self.label_10)

        self.label_16 = QLabel(self.page_actualizar)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_9.addWidget(self.label_16)

        self.label_11 = QLabel(self.page_actualizar)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_9.addWidget(self.label_11)


        self.horizontalLayout_7.addLayout(self.verticalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(30)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lineEdit_11 = QLineEdit(self.page_actualizar)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.verticalLayout_8.addWidget(self.lineEdit_11)

        self.lineEdit_10 = QLineEdit(self.page_actualizar)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.verticalLayout_8.addWidget(self.lineEdit_10)

        self.lineEdit_9 = QLineEdit(self.page_actualizar)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.verticalLayout_8.addWidget(self.lineEdit_9)

        self.lineEdit_7 = QLineEdit(self.page_actualizar)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout_8.addWidget(self.lineEdit_7)

        self.lineEdit_8 = QLineEdit(self.page_actualizar)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.verticalLayout_8.addWidget(self.lineEdit_8)


        self.horizontalLayout_7.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.signal_actualizar = QLabel(self.page_actualizar)
        self.signal_actualizar.setObjectName(u"signal_actualizar")
        self.signal_actualizar.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_8.addWidget(self.signal_actualizar)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.bt_actulizar_tabla = QPushButton(self.page_actualizar)
        self.bt_actulizar_tabla.setObjectName(u"bt_actulizar_tabla")
        self.bt_actulizar_tabla.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_8.addWidget(self.bt_actulizar_tabla)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.stackedWidget.addWidget(self.page_actualizar)
        self.page_pdf = QWidget()
        self.page_pdf.setObjectName(u"page_pdf")
        self.verticalLayout_14 = QVBoxLayout(self.page_pdf)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_14 = QLabel(self.page_pdf)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_23 = QLabel(self.page_pdf)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_13.addWidget(self.label_23)

        self.lineEdit_15 = QLineEdit(self.page_pdf)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.horizontalLayout_13.addWidget(self.lineEdit_15)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)

        self.pushButton_2 = QPushButton(self.page_pdf)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_13.addWidget(self.pushButton_2)


        self.verticalLayout_14.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_5 = QSpacerItem(20, 130, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_5)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(30)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_17 = QLabel(self.page_pdf)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_13.addWidget(self.label_17)

        self.label_20 = QLabel(self.page_pdf)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_13.addWidget(self.label_20)

        self.label_21 = QLabel(self.page_pdf)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_13.addWidget(self.label_21)

        self.label_22 = QLabel(self.page_pdf)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_13.addWidget(self.label_22)


        self.horizontalLayout_12.addLayout(self.verticalLayout_13)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(30)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lineEdit_6 = QLineEdit(self.page_pdf)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_12.addWidget(self.lineEdit_6)

        self.lineEdit_12 = QLineEdit(self.page_pdf)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.verticalLayout_12.addWidget(self.lineEdit_12)

        self.lineEdit_13 = QLineEdit(self.page_pdf)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.verticalLayout_12.addWidget(self.lineEdit_13)

        self.lineEdit_14 = QLineEdit(self.page_pdf)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.verticalLayout_12.addWidget(self.lineEdit_14)


        self.horizontalLayout_12.addLayout(self.verticalLayout_12)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_10)


        self.verticalLayout_14.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_6 = QSpacerItem(20, 130, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_6)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)

        self.pushButton = QPushButton(self.page_pdf)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_14.addWidget(self.pushButton)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_12)


        self.verticalLayout_14.addLayout(self.horizontalLayout_14)

        self.stackedWidget.addWidget(self.page_pdf)
        self.page_datos = QWidget()
        self.page_datos.setObjectName(u"page_datos")
        self.verticalLayout_5 = QVBoxLayout(self.page_datos)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.page_datos)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.tabla_clientes = QTableWidget(self.page_datos)
        if (self.tabla_clientes.columnCount() < 8):
            self.tabla_clientes.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_clientes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_clientes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_clientes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_clientes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_clientes.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_clientes.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_clientes.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_clientes.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tabla_clientes.setObjectName(u"tabla_clientes")

        self.verticalLayout_5.addWidget(self.tabla_clientes)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.bt_refrescar = QPushButton(self.page_datos)
        self.bt_refrescar.setObjectName(u"bt_refrescar")
        self.bt_refrescar.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_3.addWidget(self.bt_refrescar)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.page_datos)
        self.page_eliminar = QWidget()
        self.page_eliminar.setObjectName(u"page_eliminar")
        self.verticalLayout_11 = QVBoxLayout(self.page_eliminar)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_18 = QLabel(self.page_eliminar)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_18)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_19 = QLabel(self.page_eliminar)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_10.addWidget(self.label_19)

        self.eliminar_buscar = QLineEdit(self.page_eliminar)
        self.eliminar_buscar.setObjectName(u"eliminar_buscar")

        self.horizontalLayout_10.addWidget(self.eliminar_buscar)

        self.bt_buscar_eliminar = QPushButton(self.page_eliminar)
        self.bt_buscar_eliminar.setObjectName(u"bt_buscar_eliminar")
        self.bt_buscar_eliminar.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_10.addWidget(self.bt_buscar_eliminar)


        self.verticalLayout_11.addLayout(self.horizontalLayout_10)

        self.tabla_borrar = QTableWidget(self.page_eliminar)
        if (self.tabla_borrar.columnCount() < 8):
            self.tabla_borrar.setColumnCount(8)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        self.tabla_borrar.setObjectName(u"tabla_borrar")

        self.verticalLayout_11.addWidget(self.tabla_borrar)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.signal_eliminar = QLabel(self.page_eliminar)
        self.signal_eliminar.setObjectName(u"signal_eliminar")
        self.signal_eliminar.setMinimumSize(QSize(200, 30))

        self.horizontalLayout_11.addWidget(self.signal_eliminar)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.bt_eliminar = QPushButton(self.page_eliminar)
        self.bt_eliminar.setObjectName(u"bt_eliminar")
        self.bt_eliminar.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_11.addWidget(self.bt_eliminar)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.stackedWidget.addWidget(self.page_eliminar)
        self.page_ajustes = QWidget()
        self.page_ajustes.setObjectName(u"page_ajustes")
        self.stackedWidget.addWidget(self.page_ajustes)
        self.page_registrar = QWidget()
        self.page_registrar.setObjectName(u"page_registrar")
        self.verticalLayout_7 = QVBoxLayout(self.page_registrar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.page_registrar)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.page_registrar)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.label_3 = QLabel(self.page_registrar)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.label_4 = QLabel(self.page_registrar)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.label_5 = QLabel(self.page_registrar)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.label_6 = QLabel(self.page_registrar)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(self.page_registrar)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.page_registrar)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.page_registrar)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.page_registrar)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.page_registrar)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout.addWidget(self.lineEdit_5)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.signal_agregar = QLabel(self.page_registrar)
        self.signal_agregar.setObjectName(u"signal_agregar")
        self.signal_agregar.setMinimumSize(QSize(200, 30))

        self.horizontalLayout_6.addWidget(self.signal_agregar)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.label_8 = QLabel(self.page_registrar)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(200, 0))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.bt_aceptarR = QPushButton(self.page_registrar)
        self.bt_aceptarR.setObjectName(u"bt_aceptarR")
        self.bt_aceptarR.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_6.addWidget(self.bt_aceptarR)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.page_registrar)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_paginas)


        self.verticalLayout_2.addWidget(self.frame_contenido)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)

        self.horizontalLayout_4.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_menu.setText("")
        self.bt_restaurar.setText("")
        self.bt_minimizar.setText("")
        self.bt_maximizar.setText("")
        self.bt_cerrar.setText("")
        self.bt_datos.setText(QCoreApplication.translate("MainWindow", u"BASE DATOS", None))
        self.bt_registrar.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
        self.bt_actualizar_2.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.bt_eliminar_menu.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        self.bt_ajustes.setText(QCoreApplication.translate("MainWindow", u"AJUSTES", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR USUARIOS", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"NOMBRE DEL USUARIO", None))
        self.bt_buscar_actualizar.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"APELLIDO", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"PASSWORD", None))
        self.signal_actualizar.setText("")
        self.bt_actulizar_tabla.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"GENERADOR DE PDF", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"NOMBRE DEL CLIENTE ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"ID CLIENTE", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"VALOR FINAL", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"CUOTA", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"AUMENTO", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"GENERAR PDF", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CLIENTES", None))
        ___qtablewidgetitem = self.tabla_clientes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tabla_clientes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None));
        ___qtablewidgetitem2 = self.tabla_clientes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"APELLIDO", None));
        ___qtablewidgetitem3 = self.tabla_clientes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"TELEFONO", None));
        ___qtablewidgetitem4 = self.tabla_clientes.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"CUIL", None));
        ___qtablewidgetitem5 = self.tabla_clientes.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"LOTE", None));
        ___qtablewidgetitem6 = self.tabla_clientes.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"TRANSACCION", None));
        ___qtablewidgetitem7 = self.tabla_clientes.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"CUOTA", None));
        self.bt_refrescar.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR CLIENTES", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"NOMBRE DEL CLIENTE", None))
        self.bt_buscar_eliminar.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        ___qtablewidgetitem8 = self.tabla_borrar.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem9 = self.tabla_borrar.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None));
        ___qtablewidgetitem10 = self.tabla_borrar.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"APELLIDO", None));
        ___qtablewidgetitem11 = self.tabla_borrar.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"TELEFONO", None));
        ___qtablewidgetitem12 = self.tabla_borrar.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"CUIL", None));
        ___qtablewidgetitem13 = self.tabla_borrar.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"LOTE", None));
        ___qtablewidgetitem14 = self.tabla_borrar.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"TRANSACCION", None));
        ___qtablewidgetitem15 = self.tabla_borrar.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"CUOTA", None));
        self.signal_eliminar.setText("")
        self.bt_eliminar.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"REGISTRO DE USUARIO", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"APELLIDO", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"PASSWORD", None))
        self.signal_agregar.setText("")
        self.label_8.setText("")
        self.bt_aceptarR.setText(QCoreApplication.translate("MainWindow", u"ACEPTAR", None))
    # retranslateUi

