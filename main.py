from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.uic.load_ui import loadUi
from modelos.usuario import Usuario

import sys
import os

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()

        # Instancias
        self.login_ui = loadUi(os.path.join("Front", "Login", "loginUI3.ui"))
        self.main_ui = loadUi(os.path.join("Front", "Proyecto_Inmobiliaria.ui"))
        self.main_ui.stackedWidget.setCurrentWidget(self.main_ui.page_1gestion_clientes)

        
        # Muestro login al iniciar app
        self.login_ui.show()

        # Main UI menu lateral buttons
        self.main_ui.bt_registrar_menulateral.clicked.connect(lambda: self.cambiar_pestaña(self.main_ui.page_1gestion_clientes))
        self.main_ui.bt_transacciones_menulateral.clicked.connect(lambda: self.cambiar_pestaña(self.main_ui.page_5gestion_transacciones))
        self.main_ui.bt_pagos_menulateral.clicked.connect(lambda: self.cambiar_pestaña(self.main_ui.page_9gestion_pagos))
        self.main_ui.bt_salir_menulateral.clicked.connect(lambda: sys.exit())

        # Main UI Gestion Clientes Buttons
        self.main_ui.bt_gestionar_cliente.clicked.connect(lambda: self.cambiar_pestaña(self.main_ui.page_2registrar_cliente))
        self.main_ui.bt_modificar_cliente.clicked.connect(lambda: self.cambiar_pestaña(self.main_ui.page_3modificar_cliente))
        self.main_ui.bt_eliminar_cliente.clicked.connect(lambda: self.cambiar_pestaña(self.main_ui.page_4eliminar_cliente))
        # self.main_ui.bt_lista_cliente.clicked.connect(lambda: self.cambiar_pestaña(self.main_ui.page_4eliminar_cliente))


        # Login buttons
        self.login_ui.bt_login_inicio.clicked.connect(self.login)

    def login(self):
        contraseña = self.login_ui.line_contrasea_login.text()
        nombre = self.login_ui.line_usuario_login.text()

        usuario = Usuario.login(nombre, contraseña)

        if usuario != None:
            print("Se ha iniciado sesion!")
            self.login_ui.hide()
            self.main_ui.show()
        else:
            print("Usuario y/o contraseña incorrectos")

    def cambiar_pestaña(self, pestaña):
        self.main_ui.stackedWidget.setCurrentWidget(pestaña)

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    sys.exit(app.exec())
