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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1022, 868)
        MainWindow.setMinimumSize(QSize(900, 868))
        MainWindow.setSizeIncrement(QSize(0, 0))
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_22 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout_2 = QVBoxLayout(self.frame_control)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.bt_datos_menulateral = QPushButton(self.frame_control)
        self.bt_datos_menulateral.setObjectName(u"bt_datos_menulateral")
        self.bt_datos_menulateral.setMinimumSize(QSize(0, 40))
        icon = QIcon()
        icon.addFile(u"img/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_datos_menulateral.setIcon(icon)
        self.bt_datos_menulateral.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.bt_datos_menulateral)

        self.bt_registrar_menulateral = QPushButton(self.frame_control)
        self.bt_registrar_menulateral.setObjectName(u"bt_registrar_menulateral")
        self.bt_registrar_menulateral.setMinimumSize(QSize(0, 40))
        icon1 = QIcon()
        icon1.addFile(u"img/user (1).svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_registrar_menulateral.setIcon(icon1)
        self.bt_registrar_menulateral.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.bt_registrar_menulateral)

        self.bt_transacciones_menulateral = QPushButton(self.frame_control)
        self.bt_transacciones_menulateral.setObjectName(u"bt_transacciones_menulateral")
        self.bt_transacciones_menulateral.setMinimumSize(QSize(0, 40))
        icon2 = QIcon()
        icon2.addFile(u"img/globe.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_transacciones_menulateral.setIcon(icon2)
        self.bt_transacciones_menulateral.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.bt_transacciones_menulateral)

        self.bt_pagos_menulateral = QPushButton(self.frame_control)
        self.bt_pagos_menulateral.setObjectName(u"bt_pagos_menulateral")
        self.bt_pagos_menulateral.setMinimumSize(QSize(0, 40))
        icon3 = QIcon()
        icon3.addFile(u"img/dollar-sign.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_pagos_menulateral.setIcon(icon3)
        self.bt_pagos_menulateral.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.bt_pagos_menulateral)

        self.bt_pdf_menu = QPushButton(self.frame_control)
        self.bt_pdf_menu.setObjectName(u"bt_pdf_menu")
        self.bt_pdf_menu.setMinimumSize(QSize(0, 40))
        icon4 = QIcon()
        icon4.addFile(u"img/file-plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_pdf_menu.setIcon(icon4)
        self.bt_pdf_menu.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.bt_pdf_menu)

        self.bt_salir_menulateral = QPushButton(self.frame_control)
        self.bt_salir_menulateral.setObjectName(u"bt_salir_menulateral")
        self.bt_salir_menulateral.setMinimumSize(QSize(0, 40))
        icon5 = QIcon()
        icon5.addFile(u"img/log-out.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_salir_menulateral.setIcon(icon5)
        self.bt_salir_menulateral.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.bt_salir_menulateral)


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
        self.stackedWidget.setMinimumSize(QSize(120, 30))
        self.stackedWidget.setStyleSheet(u"")
        self.page_3modificar_cliente = QWidget()
        self.page_3modificar_cliente.setObjectName(u"page_3modificar_cliente")
        self.verticalLayout_10 = QVBoxLayout(self.page_3modificar_cliente)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_15 = QLabel(self.page_3modificar_cliente)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_15)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.page_3modificar_cliente)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.actualizar_buscar = QLineEdit(self.page_3modificar_cliente)
        self.actualizar_buscar.setObjectName(u"actualizar_buscar")

        self.horizontalLayout_9.addWidget(self.actualizar_buscar)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_38)

        self.bt_buscar_actualizar = QPushButton(self.page_3modificar_cliente)
        self.bt_buscar_actualizar.setObjectName(u"bt_buscar_actualizar")
        self.bt_buscar_actualizar.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_9.addWidget(self.bt_buscar_actualizar)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(30)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(30)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_12 = QLabel(self.page_3modificar_cliente)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_9.addWidget(self.label_12)

        self.label_10 = QLabel(self.page_3modificar_cliente)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_9.addWidget(self.label_10)

        self.label_16 = QLabel(self.page_3modificar_cliente)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_9.addWidget(self.label_16)

        self.label_11 = QLabel(self.page_3modificar_cliente)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_9.addWidget(self.label_11)


        self.horizontalLayout_7.addLayout(self.verticalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(30)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.line_nombre_modificarCliente = QLineEdit(self.page_3modificar_cliente)
        self.line_nombre_modificarCliente.setObjectName(u"line_nombre_modificarCliente")

        self.verticalLayout_8.addWidget(self.line_nombre_modificarCliente)

        self.line_apellido_modificarCliente = QLineEdit(self.page_3modificar_cliente)
        self.line_apellido_modificarCliente.setObjectName(u"line_apellido_modificarCliente")

        self.verticalLayout_8.addWidget(self.line_apellido_modificarCliente)

        self.line_email_modificarCliente = QLineEdit(self.page_3modificar_cliente)
        self.line_email_modificarCliente.setObjectName(u"line_email_modificarCliente")

        self.verticalLayout_8.addWidget(self.line_email_modificarCliente)

        self.line_cuil_modificarCliente = QLineEdit(self.page_3modificar_cliente)
        self.line_cuil_modificarCliente.setObjectName(u"line_cuil_modificarCliente")

        self.verticalLayout_8.addWidget(self.line_cuil_modificarCliente)


        self.horizontalLayout_7.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_7 = QPushButton(self.page_3modificar_cliente)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_8.addWidget(self.pushButton_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.bt_actulizar_tabla = QPushButton(self.page_3modificar_cliente)
        self.bt_actulizar_tabla.setObjectName(u"bt_actulizar_tabla")
        self.bt_actulizar_tabla.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_8.addWidget(self.bt_actulizar_tabla)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.stackedWidget.addWidget(self.page_3modificar_cliente)
        self.page_13pdf = QWidget()
        self.page_13pdf.setObjectName(u"page_13pdf")
        self.verticalLayout_14 = QVBoxLayout(self.page_13pdf)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_14 = QLabel(self.page_13pdf)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_23 = QLabel(self.page_13pdf)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_13.addWidget(self.label_23)

        self.lineEdit_15 = QLineEdit(self.page_13pdf)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.horizontalLayout_13.addWidget(self.lineEdit_15)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)

        self.pushButton_2 = QPushButton(self.page_13pdf)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_13.addWidget(self.pushButton_2)


        self.verticalLayout_14.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_5 = QSpacerItem(20, 259, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_5)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(30)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(30)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_17 = QLabel(self.page_13pdf)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_13.addWidget(self.label_17)

        self.label_20 = QLabel(self.page_13pdf)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_13.addWidget(self.label_20)

        self.label_21 = QLabel(self.page_13pdf)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_13.addWidget(self.label_21)

        self.label_22 = QLabel(self.page_13pdf)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_13.addWidget(self.label_22)


        self.horizontalLayout_12.addLayout(self.verticalLayout_13)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(30)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lineEdit_6 = QLineEdit(self.page_13pdf)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_12.addWidget(self.lineEdit_6)

        self.lineEdit_12 = QLineEdit(self.page_13pdf)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.verticalLayout_12.addWidget(self.lineEdit_12)

        self.lineEdit_13 = QLineEdit(self.page_13pdf)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.verticalLayout_12.addWidget(self.lineEdit_13)

        self.lineEdit_14 = QLineEdit(self.page_13pdf)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.verticalLayout_12.addWidget(self.lineEdit_14)


        self.horizontalLayout_12.addLayout(self.verticalLayout_12)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_10)


        self.verticalLayout_14.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_6 = QSpacerItem(20, 258, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_6)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton_8 = QPushButton(self.page_13pdf)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_14.addWidget(self.pushButton_8)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)

        self.pushButton = QPushButton(self.page_13pdf)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_14.addWidget(self.pushButton)


        self.verticalLayout_14.addLayout(self.horizontalLayout_14)

        self.stackedWidget.addWidget(self.page_13pdf)
        self.page_8lista_transacciones = QWidget()
        self.page_8lista_transacciones.setObjectName(u"page_8lista_transacciones")
        self.verticalLayout_5 = QVBoxLayout(self.page_8lista_transacciones)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.page_8lista_transacciones)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_50 = QLabel(self.page_8lista_transacciones)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_23.addWidget(self.label_50)

        self.lineEdit_41 = QLineEdit(self.page_8lista_transacciones)
        self.lineEdit_41.setObjectName(u"lineEdit_41")

        self.horizontalLayout_23.addWidget(self.lineEdit_41)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_23)

        self.pushButton_21 = QPushButton(self.page_8lista_transacciones)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_23.addWidget(self.pushButton_21)


        self.verticalLayout_5.addLayout(self.horizontalLayout_23)

        self.tabla_clientes = QTableWidget(self.page_8lista_transacciones)
        if (self.tabla_clientes.columnCount() < 5):
            self.tabla_clientes.setColumnCount(5)
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
        if (self.tabla_clientes.rowCount() < 200):
            self.tabla_clientes.setRowCount(200)
        self.tabla_clientes.setObjectName(u"tabla_clientes")
        self.tabla_clientes.setRowCount(200)
        self.tabla_clientes.horizontalHeader().setMinimumSectionSize(50)
        self.tabla_clientes.horizontalHeader().setDefaultSectionSize(120)
        self.tabla_clientes.verticalHeader().setCascadingSectionResizes(True)
        self.tabla_clientes.verticalHeader().setMinimumSectionSize(20)
        self.tabla_clientes.verticalHeader().setDefaultSectionSize(27)

        self.verticalLayout_5.addWidget(self.tabla_clientes)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bt_Volver_Menu = QPushButton(self.page_8lista_transacciones)
        self.bt_Volver_Menu.setObjectName(u"bt_Volver_Menu")
        self.bt_Volver_Menu.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_3.addWidget(self.bt_Volver_Menu)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.bt_eliminar_transaccion = QPushButton(self.page_8lista_transacciones)
        self.bt_eliminar_transaccion.setObjectName(u"bt_eliminar_transaccion")
        self.bt_eliminar_transaccion.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_3.addWidget(self.bt_eliminar_transaccion)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.page_8lista_transacciones)
        self.page_4eliminar_cliente = QWidget()
        self.page_4eliminar_cliente.setObjectName(u"page_4eliminar_cliente")
        self.verticalLayout_11 = QVBoxLayout(self.page_4eliminar_cliente)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_18 = QLabel(self.page_4eliminar_cliente)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_18)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_19 = QLabel(self.page_4eliminar_cliente)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_10.addWidget(self.label_19)

        self.eliminar_buscar = QLineEdit(self.page_4eliminar_cliente)
        self.eliminar_buscar.setObjectName(u"eliminar_buscar")

        self.horizontalLayout_10.addWidget(self.eliminar_buscar)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_33)

        self.bt_buscar_eliminar = QPushButton(self.page_4eliminar_cliente)
        self.bt_buscar_eliminar.setObjectName(u"bt_buscar_eliminar")
        self.bt_buscar_eliminar.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_10.addWidget(self.bt_buscar_eliminar)


        self.verticalLayout_11.addLayout(self.horizontalLayout_10)

        self.tabla_borrar = QTableWidget(self.page_4eliminar_cliente)
        if (self.tabla_borrar.columnCount() < 5):
            self.tabla_borrar.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        if (self.tabla_borrar.rowCount() < 200):
            self.tabla_borrar.setRowCount(200)
        self.tabla_borrar.setObjectName(u"tabla_borrar")
        self.tabla_borrar.setMinimumSize(QSize(120, 30))
        self.tabla_borrar.setSizeIncrement(QSize(0, 0))
        self.tabla_borrar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabla_borrar.setAutoFillBackground(False)
        self.tabla_borrar.setStyleSheet(u"")
        self.tabla_borrar.setMidLineWidth(0)
        self.tabla_borrar.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tabla_borrar.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tabla_borrar.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tabla_borrar.setAutoScroll(True)
        self.tabla_borrar.setAutoScrollMargin(16)
        self.tabla_borrar.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tabla_borrar.setShowGrid(True)
        self.tabla_borrar.setSortingEnabled(False)
        self.tabla_borrar.setWordWrap(True)
        self.tabla_borrar.setRowCount(200)
        self.tabla_borrar.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_borrar.horizontalHeader().setMinimumSectionSize(50)
        self.tabla_borrar.horizontalHeader().setDefaultSectionSize(120)
        self.tabla_borrar.horizontalHeader().setHighlightSections(False)
        self.tabla_borrar.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabla_borrar.horizontalHeader().setStretchLastSection(False)
        self.tabla_borrar.verticalHeader().setVisible(True)
        self.tabla_borrar.verticalHeader().setCascadingSectionResizes(True)
        self.tabla_borrar.verticalHeader().setMinimumSectionSize(20)
        self.tabla_borrar.verticalHeader().setDefaultSectionSize(27)
        self.tabla_borrar.verticalHeader().setProperty("showSortIndicator", False)
        self.tabla_borrar.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_11.addWidget(self.tabla_borrar)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_3 = QPushButton(self.page_4eliminar_cliente)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(120, 30))
        self.pushButton_3.setSizeIncrement(QSize(120, 30))

        self.horizontalLayout_11.addWidget(self.pushButton_3)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.bt_eliminar = QPushButton(self.page_4eliminar_cliente)
        self.bt_eliminar.setObjectName(u"bt_eliminar")
        self.bt_eliminar.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_11.addWidget(self.bt_eliminar)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.stackedWidget.addWidget(self.page_4eliminar_cliente)
        self.page_1gestion_clientes = QWidget()
        self.page_1gestion_clientes.setObjectName(u"page_1gestion_clientes")
        self.verticalLayout_15 = QVBoxLayout(self.page_1gestion_clientes)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_27 = QLabel(self.page_1gestion_clientes)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_27)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(30)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_12)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(30)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_13 = QLabel(self.page_1gestion_clientes)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_16.addWidget(self.label_13)

        self.label_24 = QLabel(self.page_1gestion_clientes)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_16.addWidget(self.label_24)

        self.label_25 = QLabel(self.page_1gestion_clientes)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_16.addWidget(self.label_25)


        self.horizontalLayout_4.addLayout(self.verticalLayout_16)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.bt_gestionar_cliente = QPushButton(self.page_1gestion_clientes)
        self.bt_gestionar_cliente.setObjectName(u"bt_gestionar_cliente")
        self.bt_gestionar_cliente.setMinimumSize(QSize(200, 30))

        self.verticalLayout_3.addWidget(self.bt_gestionar_cliente)

        self.bt_modificar_cliente = QPushButton(self.page_1gestion_clientes)
        self.bt_modificar_cliente.setObjectName(u"bt_modificar_cliente")
        self.bt_modificar_cliente.setMinimumSize(QSize(200, 30))

        self.verticalLayout_3.addWidget(self.bt_modificar_cliente)

        self.bt_eliminar_cliente = QPushButton(self.page_1gestion_clientes)
        self.bt_eliminar_cliente.setObjectName(u"bt_eliminar_cliente")
        self.bt_eliminar_cliente.setMinimumSize(QSize(200, 30))

        self.verticalLayout_3.addWidget(self.bt_eliminar_cliente)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_15.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_8)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)

        self.bt_volver_gestion_cliente = QPushButton(self.page_1gestion_clientes)
        self.bt_volver_gestion_cliente.setObjectName(u"bt_volver_gestion_cliente")
        self.bt_volver_gestion_cliente.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_15.addWidget(self.bt_volver_gestion_cliente)


        self.verticalLayout_15.addLayout(self.horizontalLayout_15)

        self.stackedWidget.addWidget(self.page_1gestion_clientes)
        self.page_5gestion_transacciones = QWidget()
        self.page_5gestion_transacciones.setObjectName(u"page_5gestion_transacciones")
        self.verticalLayout_17 = QVBoxLayout(self.page_5gestion_transacciones)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_32 = QLabel(self.page_5gestion_transacciones)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_32)

        self.verticalSpacer_10 = QSpacerItem(20, 264, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_10)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(30)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_15)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(30)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_28 = QLabel(self.page_5gestion_transacciones)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_19.addWidget(self.label_28)

        self.label_29 = QLabel(self.page_5gestion_transacciones)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_19.addWidget(self.label_29)

        self.label_30 = QLabel(self.page_5gestion_transacciones)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_19.addWidget(self.label_30)

        self.label_31 = QLabel(self.page_5gestion_transacciones)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_19.addWidget(self.label_31)


        self.horizontalLayout_17.addLayout(self.verticalLayout_19)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(30)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.pushButton_12 = QPushButton(self.page_5gestion_transacciones)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(220)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setMinimumSize(QSize(200, 30))

        self.verticalLayout_18.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.page_5gestion_transacciones)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(200, 30))

        self.verticalLayout_18.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.page_5gestion_transacciones)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(200, 30))

        self.verticalLayout_18.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.page_5gestion_transacciones)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(200, 30))

        self.verticalLayout_18.addWidget(self.pushButton_15)


        self.horizontalLayout_17.addLayout(self.verticalLayout_18)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_14)


        self.verticalLayout_17.addLayout(self.horizontalLayout_17)

        self.verticalSpacer_9 = QSpacerItem(20, 263, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_13)

        self.pushButton_11 = QPushButton(self.page_5gestion_transacciones)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(120, 30))

        self.horizontalLayout.addWidget(self.pushButton_11)


        self.verticalLayout_17.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.page_5gestion_transacciones)
        self.page_6agregar_transaccion = QWidget()
        self.page_6agregar_transaccion.setObjectName(u"page_6agregar_transaccion")
        self.verticalLayout_23 = QVBoxLayout(self.page_6agregar_transaccion)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_33 = QLabel(self.page_6agregar_transaccion)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_33)

        self.verticalSpacer_12 = QSpacerItem(20, 198, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_12)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_17)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(30)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_34 = QLabel(self.page_6agregar_transaccion)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_21.addWidget(self.label_34)

        self.label_35 = QLabel(self.page_6agregar_transaccion)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_21.addWidget(self.label_35)

        self.label_36 = QLabel(self.page_6agregar_transaccion)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_21.addWidget(self.label_36)

        self.label_37 = QLabel(self.page_6agregar_transaccion)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_21.addWidget(self.label_37)

        self.label_38 = QLabel(self.page_6agregar_transaccion)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_21.addWidget(self.label_38)

        self.label_39 = QLabel(self.page_6agregar_transaccion)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_21.addWidget(self.label_39)

        self.label_40 = QLabel(self.page_6agregar_transaccion)
        self.label_40.setObjectName(u"label_40")

        self.verticalLayout_21.addWidget(self.label_40)


        self.horizontalLayout_19.addLayout(self.verticalLayout_21)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(30)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.lineEdit_11 = QLineEdit(self.page_6agregar_transaccion)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.verticalLayout_20.addWidget(self.lineEdit_11)

        self.lineEdit_16 = QLineEdit(self.page_6agregar_transaccion)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.verticalLayout_20.addWidget(self.lineEdit_16)

        self.lineEdit_17 = QLineEdit(self.page_6agregar_transaccion)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.verticalLayout_20.addWidget(self.lineEdit_17)

        self.lineEdit_18 = QLineEdit(self.page_6agregar_transaccion)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.verticalLayout_20.addWidget(self.lineEdit_18)

        self.lineEdit_19 = QLineEdit(self.page_6agregar_transaccion)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.verticalLayout_20.addWidget(self.lineEdit_19)

        self.lineEdit_20 = QLineEdit(self.page_6agregar_transaccion)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.verticalLayout_20.addWidget(self.lineEdit_20)

        self.lineEdit_21 = QLineEdit(self.page_6agregar_transaccion)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.verticalLayout_20.addWidget(self.lineEdit_21)


        self.horizontalLayout_19.addLayout(self.verticalLayout_20)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_18)


        self.verticalLayout_23.addLayout(self.horizontalLayout_19)

        self.verticalSpacer_11 = QSpacerItem(20, 198, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_11)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pushButton_16 = QPushButton(self.page_6agregar_transaccion)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_18.addWidget(self.pushButton_16)

        self.horizontalSpacer_16 = QSpacerItem(117, 27, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_16)

        self.pushButton_17 = QPushButton(self.page_6agregar_transaccion)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_18.addWidget(self.pushButton_17)


        self.verticalLayout_23.addLayout(self.horizontalLayout_18)

        self.stackedWidget.addWidget(self.page_6agregar_transaccion)
        self.page_7modificar_transaccion = QWidget()
        self.page_7modificar_transaccion.setObjectName(u"page_7modificar_transaccion")
        self.verticalLayout_26 = QVBoxLayout(self.page_7modificar_transaccion)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_41 = QLabel(self.page_7modificar_transaccion)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_41)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_42 = QLabel(self.page_7modificar_transaccion)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_21.addWidget(self.label_42)

        self.lineEdit_29 = QLineEdit(self.page_7modificar_transaccion)
        self.lineEdit_29.setObjectName(u"lineEdit_29")

        self.horizontalLayout_21.addWidget(self.lineEdit_29)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_34)

        self.pushButton_20 = QPushButton(self.page_7modificar_transaccion)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_21.addWidget(self.pushButton_20)


        self.verticalLayout_26.addLayout(self.horizontalLayout_21)

        self.verticalSpacer_13 = QSpacerItem(20, 179, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_13)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_21)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(30)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_43 = QLabel(self.page_7modificar_transaccion)
        self.label_43.setObjectName(u"label_43")

        self.verticalLayout_25.addWidget(self.label_43)

        self.label_44 = QLabel(self.page_7modificar_transaccion)
        self.label_44.setObjectName(u"label_44")

        self.verticalLayout_25.addWidget(self.label_44)

        self.label_45 = QLabel(self.page_7modificar_transaccion)
        self.label_45.setObjectName(u"label_45")

        self.verticalLayout_25.addWidget(self.label_45)

        self.label_46 = QLabel(self.page_7modificar_transaccion)
        self.label_46.setObjectName(u"label_46")

        self.verticalLayout_25.addWidget(self.label_46)

        self.label_47 = QLabel(self.page_7modificar_transaccion)
        self.label_47.setObjectName(u"label_47")

        self.verticalLayout_25.addWidget(self.label_47)

        self.label_48 = QLabel(self.page_7modificar_transaccion)
        self.label_48.setObjectName(u"label_48")

        self.verticalLayout_25.addWidget(self.label_48)

        self.label_49 = QLabel(self.page_7modificar_transaccion)
        self.label_49.setObjectName(u"label_49")

        self.verticalLayout_25.addWidget(self.label_49)


        self.horizontalLayout_22.addLayout(self.verticalLayout_25)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(30)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.lineEdit_22 = QLineEdit(self.page_7modificar_transaccion)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.verticalLayout_24.addWidget(self.lineEdit_22)

        self.lineEdit_23 = QLineEdit(self.page_7modificar_transaccion)
        self.lineEdit_23.setObjectName(u"lineEdit_23")

        self.verticalLayout_24.addWidget(self.lineEdit_23)

        self.lineEdit_24 = QLineEdit(self.page_7modificar_transaccion)
        self.lineEdit_24.setObjectName(u"lineEdit_24")

        self.verticalLayout_24.addWidget(self.lineEdit_24)

        self.lineEdit_25 = QLineEdit(self.page_7modificar_transaccion)
        self.lineEdit_25.setObjectName(u"lineEdit_25")

        self.verticalLayout_24.addWidget(self.lineEdit_25)

        self.lineEdit_26 = QLineEdit(self.page_7modificar_transaccion)
        self.lineEdit_26.setObjectName(u"lineEdit_26")

        self.verticalLayout_24.addWidget(self.lineEdit_26)

        self.lineEdit_27 = QLineEdit(self.page_7modificar_transaccion)
        self.lineEdit_27.setObjectName(u"lineEdit_27")

        self.verticalLayout_24.addWidget(self.lineEdit_27)

        self.lineEdit_28 = QLineEdit(self.page_7modificar_transaccion)
        self.lineEdit_28.setObjectName(u"lineEdit_28")

        self.verticalLayout_24.addWidget(self.lineEdit_28)


        self.horizontalLayout_22.addLayout(self.verticalLayout_24)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_20)


        self.verticalLayout_26.addLayout(self.horizontalLayout_22)

        self.verticalSpacer_14 = QSpacerItem(20, 179, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_14)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pushButton_19 = QPushButton(self.page_7modificar_transaccion)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_20.addWidget(self.pushButton_19)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_19)

        self.pushButton_18 = QPushButton(self.page_7modificar_transaccion)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_20.addWidget(self.pushButton_18)


        self.verticalLayout_26.addLayout(self.horizontalLayout_20)

        self.stackedWidget.addWidget(self.page_7modificar_transaccion)
        self.page_9gestion_pagos = QWidget()
        self.page_9gestion_pagos.setObjectName(u"page_9gestion_pagos")
        self.verticalLayout_29 = QVBoxLayout(self.page_9gestion_pagos)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_8 = QLabel(self.page_9gestion_pagos)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_8)

        self.verticalSpacer_16 = QSpacerItem(20, 264, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_16)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(30)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_24)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setSpacing(30)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_51 = QLabel(self.page_9gestion_pagos)
        self.label_51.setObjectName(u"label_51")

        self.verticalLayout_28.addWidget(self.label_51)

        self.label_52 = QLabel(self.page_9gestion_pagos)
        self.label_52.setObjectName(u"label_52")

        self.verticalLayout_28.addWidget(self.label_52)

        self.label_53 = QLabel(self.page_9gestion_pagos)
        self.label_53.setObjectName(u"label_53")

        self.verticalLayout_28.addWidget(self.label_53)

        self.label_54 = QLabel(self.page_9gestion_pagos)
        self.label_54.setObjectName(u"label_54")

        self.verticalLayout_28.addWidget(self.label_54)


        self.horizontalLayout_24.addLayout(self.verticalLayout_28)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(30)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.pushButton_22 = QPushButton(self.page_9gestion_pagos)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(120, 30))

        self.verticalLayout_27.addWidget(self.pushButton_22)

        self.pushButton_23 = QPushButton(self.page_9gestion_pagos)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(120, 30))

        self.verticalLayout_27.addWidget(self.pushButton_23)

        self.pushButton_24 = QPushButton(self.page_9gestion_pagos)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(120, 30))

        self.verticalLayout_27.addWidget(self.pushButton_24)

        self.pushButton_25 = QPushButton(self.page_9gestion_pagos)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMinimumSize(QSize(120, 30))

        self.verticalLayout_27.addWidget(self.pushButton_25)


        self.horizontalLayout_24.addLayout(self.verticalLayout_27)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_25)


        self.verticalLayout_29.addLayout(self.horizontalLayout_24)

        self.verticalSpacer_15 = QSpacerItem(20, 263, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_15)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_22)

        self.pushButton_26 = QPushButton(self.page_9gestion_pagos)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_33.addWidget(self.pushButton_26)


        self.verticalLayout_29.addLayout(self.horizontalLayout_33)

        self.stackedWidget.addWidget(self.page_9gestion_pagos)
        self.page_10registrar_pago = QWidget()
        self.page_10registrar_pago.setObjectName(u"page_10registrar_pago")
        self.verticalLayout_32 = QVBoxLayout(self.page_10registrar_pago)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_55 = QLabel(self.page_10registrar_pago)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_55)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_57 = QLabel(self.page_10registrar_pago)
        self.label_57.setObjectName(u"label_57")

        self.horizontalLayout_26.addWidget(self.label_57)

        self.lineEdit_30 = QLineEdit(self.page_10registrar_pago)
        self.lineEdit_30.setObjectName(u"lineEdit_30")

        self.horizontalLayout_26.addWidget(self.lineEdit_30)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_35)

        self.pushButton_28 = QPushButton(self.page_10registrar_pago)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_26.addWidget(self.pushButton_28)


        self.verticalLayout_32.addLayout(self.horizontalLayout_26)

        self.verticalSpacer_18 = QSpacerItem(20, 259, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_18)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(30)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_27)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setSpacing(30)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_58 = QLabel(self.page_10registrar_pago)
        self.label_58.setObjectName(u"label_58")

        self.verticalLayout_31.addWidget(self.label_58)

        self.label_59 = QLabel(self.page_10registrar_pago)
        self.label_59.setObjectName(u"label_59")

        self.verticalLayout_31.addWidget(self.label_59)

        self.label_60 = QLabel(self.page_10registrar_pago)
        self.label_60.setObjectName(u"label_60")

        self.verticalLayout_31.addWidget(self.label_60)

        self.label_61 = QLabel(self.page_10registrar_pago)
        self.label_61.setObjectName(u"label_61")

        self.verticalLayout_31.addWidget(self.label_61)


        self.horizontalLayout_27.addLayout(self.verticalLayout_31)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setSpacing(30)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.lineEdit_31 = QLineEdit(self.page_10registrar_pago)
        self.lineEdit_31.setObjectName(u"lineEdit_31")

        self.verticalLayout_30.addWidget(self.lineEdit_31)

        self.lineEdit_32 = QLineEdit(self.page_10registrar_pago)
        self.lineEdit_32.setObjectName(u"lineEdit_32")

        self.verticalLayout_30.addWidget(self.lineEdit_32)

        self.lineEdit_33 = QLineEdit(self.page_10registrar_pago)
        self.lineEdit_33.setObjectName(u"lineEdit_33")

        self.verticalLayout_30.addWidget(self.lineEdit_33)

        self.lineEdit_34 = QLineEdit(self.page_10registrar_pago)
        self.lineEdit_34.setObjectName(u"lineEdit_34")

        self.verticalLayout_30.addWidget(self.lineEdit_34)


        self.horizontalLayout_27.addLayout(self.verticalLayout_30)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_28)


        self.verticalLayout_32.addLayout(self.horizontalLayout_27)

        self.verticalSpacer_17 = QSpacerItem(20, 258, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_17)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.pushButton_32 = QPushButton(self.page_10registrar_pago)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_25.addWidget(self.pushButton_32)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_26)

        self.pushButton_33 = QPushButton(self.page_10registrar_pago)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_25.addWidget(self.pushButton_33)


        self.verticalLayout_32.addLayout(self.horizontalLayout_25)

        self.stackedWidget.addWidget(self.page_10registrar_pago)
        self.page_11modificar_pago = QWidget()
        self.page_11modificar_pago.setObjectName(u"page_11modificar_pago")
        self.verticalLayout_35 = QVBoxLayout(self.page_11modificar_pago)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_56 = QLabel(self.page_11modificar_pago)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_56)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_62 = QLabel(self.page_11modificar_pago)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_30.addWidget(self.label_62)

        self.lineEdit_35 = QLineEdit(self.page_11modificar_pago)
        self.lineEdit_35.setObjectName(u"lineEdit_35")

        self.horizontalLayout_30.addWidget(self.lineEdit_35)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_36)

        self.pushButton_27 = QPushButton(self.page_11modificar_pago)
        self.pushButton_27.setObjectName(u"pushButton_27")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_27.sizePolicy().hasHeightForWidth())
        self.pushButton_27.setSizePolicy(sizePolicy1)
        self.pushButton_27.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_30.addWidget(self.pushButton_27)


        self.verticalLayout_35.addLayout(self.horizontalLayout_30)

        self.verticalSpacer_19 = QSpacerItem(20, 259, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_19)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setSpacing(30)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_30)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setSpacing(30)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_63 = QLabel(self.page_11modificar_pago)
        self.label_63.setObjectName(u"label_63")

        self.verticalLayout_34.addWidget(self.label_63)

        self.label_64 = QLabel(self.page_11modificar_pago)
        self.label_64.setObjectName(u"label_64")

        self.verticalLayout_34.addWidget(self.label_64)

        self.label_65 = QLabel(self.page_11modificar_pago)
        self.label_65.setObjectName(u"label_65")

        self.verticalLayout_34.addWidget(self.label_65)

        self.label_66 = QLabel(self.page_11modificar_pago)
        self.label_66.setObjectName(u"label_66")

        self.verticalLayout_34.addWidget(self.label_66)


        self.horizontalLayout_29.addLayout(self.verticalLayout_34)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setSpacing(30)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.lineEdit_36 = QLineEdit(self.page_11modificar_pago)
        self.lineEdit_36.setObjectName(u"lineEdit_36")

        self.verticalLayout_33.addWidget(self.lineEdit_36)

        self.lineEdit_37 = QLineEdit(self.page_11modificar_pago)
        self.lineEdit_37.setObjectName(u"lineEdit_37")

        self.verticalLayout_33.addWidget(self.lineEdit_37)

        self.lineEdit_38 = QLineEdit(self.page_11modificar_pago)
        self.lineEdit_38.setObjectName(u"lineEdit_38")

        self.verticalLayout_33.addWidget(self.lineEdit_38)

        self.lineEdit_39 = QLineEdit(self.page_11modificar_pago)
        self.lineEdit_39.setObjectName(u"lineEdit_39")

        self.verticalLayout_33.addWidget(self.lineEdit_39)


        self.horizontalLayout_29.addLayout(self.verticalLayout_33)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_31)


        self.verticalLayout_35.addLayout(self.horizontalLayout_29)

        self.verticalSpacer_20 = QSpacerItem(20, 258, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_20)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.pushButton_29 = QPushButton(self.page_11modificar_pago)
        self.pushButton_29.setObjectName(u"pushButton_29")
        sizePolicy1.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy1)
        self.pushButton_29.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_28.addWidget(self.pushButton_29)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_29)

        self.pushButton_30 = QPushButton(self.page_11modificar_pago)
        self.pushButton_30.setObjectName(u"pushButton_30")
        sizePolicy1.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy1)
        self.pushButton_30.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_28.addWidget(self.pushButton_30)


        self.verticalLayout_35.addLayout(self.horizontalLayout_28)

        self.stackedWidget.addWidget(self.page_11modificar_pago)
        self.page_12lista_pagos = QWidget()
        self.page_12lista_pagos.setObjectName(u"page_12lista_pagos")
        self.verticalLayout_36 = QVBoxLayout(self.page_12lista_pagos)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_67 = QLabel(self.page_12lista_pagos)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_67)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_68 = QLabel(self.page_12lista_pagos)
        self.label_68.setObjectName(u"label_68")

        self.horizontalLayout_32.addWidget(self.label_68)

        self.lineEdit_40 = QLineEdit(self.page_12lista_pagos)
        self.lineEdit_40.setObjectName(u"lineEdit_40")

        self.horizontalLayout_32.addWidget(self.lineEdit_40)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_37)

        self.pushButton_31 = QPushButton(self.page_12lista_pagos)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setMinimumSize(QSize(120, 30))
        self.pushButton_31.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_32.addWidget(self.pushButton_31)


        self.verticalLayout_36.addLayout(self.horizontalLayout_32)

        self.tableWidget = QTableWidget(self.page_12lista_pagos)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        if (self.tableWidget.rowCount() < 200):
            self.tableWidget.setRowCount(200)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(200)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)

        self.verticalLayout_36.addWidget(self.tableWidget)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.pushButton_35 = QPushButton(self.page_12lista_pagos)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setMinimumSize(QSize(120, 30))
        self.pushButton_35.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_31.addWidget(self.pushButton_35)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_32)

        self.pushButton_34 = QPushButton(self.page_12lista_pagos)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setMinimumSize(QSize(120, 30))
        self.pushButton_34.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_31.addWidget(self.pushButton_34)


        self.verticalLayout_36.addLayout(self.horizontalLayout_31)

        self.stackedWidget.addWidget(self.page_12lista_pagos)
        self.page_2registrar_cliente = QWidget()
        self.page_2registrar_cliente.setObjectName(u"page_2registrar_cliente")
        self.verticalLayout_7 = QVBoxLayout(self.page_2registrar_cliente)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.page_2registrar_cliente)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(30)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.page_2registrar_cliente)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.label_3 = QLabel(self.page_2registrar_cliente)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.label_4 = QLabel(self.page_2registrar_cliente)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.label_5 = QLabel(self.page_2registrar_cliente)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line_id_registro_cliente = QLineEdit(self.page_2registrar_cliente)
        self.line_id_registro_cliente.setObjectName(u"line_id_registro_cliente")

        self.verticalLayout.addWidget(self.line_id_registro_cliente)

        self.line_nombre_registro_cliente = QLineEdit(self.page_2registrar_cliente)
        self.line_nombre_registro_cliente.setObjectName(u"line_nombre_registro_cliente")

        self.verticalLayout.addWidget(self.line_nombre_registro_cliente)

        self.line_apellido_registro_cliente = QLineEdit(self.page_2registrar_cliente)
        self.line_apellido_registro_cliente.setObjectName(u"line_apellido_registro_cliente")

        self.verticalLayout.addWidget(self.line_apellido_registro_cliente)

        self.line_email_registro_cliente = QLineEdit(self.page_2registrar_cliente)
        self.line_email_registro_cliente.setObjectName(u"line_email_registro_cliente")

        self.verticalLayout.addWidget(self.line_email_registro_cliente)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.bt_Cancelar_Cliente = QPushButton(self.page_2registrar_cliente)
        self.bt_Cancelar_Cliente.setObjectName(u"bt_Cancelar_Cliente")
        self.bt_Cancelar_Cliente.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_6.addWidget(self.bt_Cancelar_Cliente)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.bt_Aceptar_Cliente = QPushButton(self.page_2registrar_cliente)
        self.bt_Aceptar_Cliente.setObjectName(u"bt_Aceptar_Cliente")
        self.bt_Aceptar_Cliente.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_6.addWidget(self.bt_Aceptar_Cliente)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.page_2registrar_cliente)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_paginas)


        self.horizontalLayout_16.addWidget(self.frame_contenido)


        self.verticalLayout_22.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_datos_menulateral.setText(QCoreApplication.translate("MainWindow", u"MENU LATERAL", None))
        self.bt_registrar_menulateral.setText(QCoreApplication.translate("MainWindow", u"CLIENTES", None))
        self.bt_transacciones_menulateral.setText(QCoreApplication.translate("MainWindow", u"TRANSACCIONES", None))
        self.bt_pagos_menulateral.setText(QCoreApplication.translate("MainWindow", u"PAGOS", None))
        self.bt_pdf_menu.setText(QCoreApplication.translate("MainWindow", u"PDF", None))
        self.bt_salir_menulateral.setText(QCoreApplication.translate("MainWindow", u"SALIR", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"MODIFICAR CLIENTE", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"SELECCIONAR CLIENTE", None))
        self.bt_buscar_actualizar.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"APELLIDO", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CUIL", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.bt_actulizar_tabla.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"GENERADOR DE PDF", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"NOMBRE DEL CLIENTE ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"ID CLIENTE", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"VALOR FINAL", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"CUOTA", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"AUMENTO", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"VOLVER", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"GENERAR PDF", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"LISTA DE TRANSACCIONES", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Transacci\u00f3n:", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        ___qtablewidgetitem = self.tabla_clientes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tabla_clientes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None));
        ___qtablewidgetitem2 = self.tabla_clientes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"VALOR FINAL", None));
        ___qtablewidgetitem3 = self.tabla_clientes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"CUOTAS", None));
        ___qtablewidgetitem4 = self.tabla_clientes.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"VALOR DE CUOTA", None));
        self.bt_Volver_Menu.setText(QCoreApplication.translate("MainWindow", u"VOLVER", None))
        self.bt_eliminar_transaccion.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"LISTA DE CLIENTES", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"NOMBRE DEL CLIENTE", None))
        self.bt_buscar_eliminar.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        ___qtablewidgetitem5 = self.tabla_borrar.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem6 = self.tabla_borrar.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None));
        ___qtablewidgetitem7 = self.tabla_borrar.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"APELLIDO", None));
        ___qtablewidgetitem8 = self.tabla_borrar.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"TELEFONO", None));
        ___qtablewidgetitem9 = self.tabla_borrar.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"CUIL", None));

        __sortingEnabled = self.tabla_borrar.isSortingEnabled()
        self.tabla_borrar.setSortingEnabled(False)
        self.tabla_borrar.setSortingEnabled(__sortingEnabled)

        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"VOLVER", None))
        self.bt_eliminar.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"GESTION DE CLIENTES ", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"1)", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"2)", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"3)", None))
        self.bt_gestionar_cliente.setText(QCoreApplication.translate("MainWindow", u"Gestionar Clientes", None))
        self.bt_modificar_cliente.setText(QCoreApplication.translate("MainWindow", u"Modificar Cliente", None))
        self.bt_eliminar_cliente.setText(QCoreApplication.translate("MainWindow", u"Eliminar Cliente", None))
        self.bt_volver_gestion_cliente.setText(QCoreApplication.translate("MainWindow", u"VOLVER", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"GESTI\u00d3N DE TRANSACCIONES ", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"1)", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"2)", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"3)", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"4)", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Agregar Transacci\u00f3n", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Modificar Transacci\u00f3n", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Eliminar Transacci\u00f3n", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Listar Transacciones", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"VOLVER", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u" AGREGAR TRANSACCI\u00d3N ", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Cliente ID", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Valor Final", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Cuotas", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Valor de Cuota", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Aumento", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Fecha de Boleto", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Fecha Primera Cuota", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"VOLVER", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"MODIFICAR TRANSACCI\u00d3N ", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Transacci\u00f3n", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Cliente ID", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Valor Final", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Cuotas", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Valor de Cuota", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Aumento", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Fecha de Boleto", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Fecha Primera Cuota", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"VOLVER", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"GESTI\u00d3N DE PAGOS ", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"1)", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"2)", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"3)", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"4)", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Registrar Pago", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Modificar Pago", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Eliminar Pago", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Listar Pagos", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"VOLVER", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR PAGO  ", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Transacci\u00f3n", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Cuota", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Valor", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"VOLVER", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"MODIFICAR PAGO", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Pago", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Cuota", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Valor", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"VOLVER", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"LISTA DE PAGOS ", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Pago", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"TRANSACCION ID", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"CUOTA", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"ESTADO", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"FECHA", None));
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"VALOR", None));
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"VOLVER", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"REGISTRO DE CLIENTE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"APELLIDO", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None))
        self.bt_Cancelar_Cliente.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.bt_Aceptar_Cliente.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
    # retranslateUi

