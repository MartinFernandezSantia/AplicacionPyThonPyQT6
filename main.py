from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox, QWidget
from PyQt6.QtCore import QDate, Qt
from PyQt6.uic.load_ui import loadUi
from modelos.usuario import Usuario
from modelos.cliente import Cliente
from modelos.transaccion import Transaccion
from utils.pdf_generador import generar_pdf
from Front.Login2.loginUi3 import Ui_Form
from bd.base_de_datos import BD

import sys
import os

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()

        # Instancias
        self.login_ui = QWidget()
        self.login_UiForm = Ui_Form()
        self.login_UiForm.setupUi(self.login_ui)
        
        self.main_ui = loadUi(os.path.join("Front", "Proyecto_Inmobiliaria.ui"))
        self.main_ui.stackedWidget.setCurrentWidget(self.main_ui.page_1gestion_clientes)
        self.main_ui.closeEvent = lambda event: self.custom_close_event(event)

        self.modificar_cliente_ui = loadUi(os.path.join("Front", "Modificar Cliente Ventana.ui"))
        self.modificar_transaccion_ui = loadUi(os.path.join("Front", "Modificar Transaccion Ventana.ui"))
        

        # Muestro login al iniciar app
        self.login_ui.show()


        # Login buttons
        self.login_UiForm.pushButton.clicked.connect(self.login)


        # Main UI menu lateral buttons
        self.main_ui.bt_registrar_menulateral.clicked.connect(lambda: self.cambiar_pestaña(self.main_ui.page_1gestion_clientes))
        self.main_ui.bt_transacciones_menulateral.clicked.connect(lambda: self.cambiar_pestaña(self.main_ui.page_5gestion_transacciones))
        self.main_ui.bt_pagos_menulateral.clicked.connect(lambda: (
            self.cambiar_pestaña(self.main_ui.page_12lista_pagos),
            self.abrir_lista_pagos()
            ))
        self.main_ui.bt_salir_menulateral.clicked.connect(lambda: sys.exit())


        # Menu Clientes Buttons
        self.main_ui.bt_gestionar_cliente.clicked.connect(lambda: self.cambiar_pestaña(self.main_ui.page_2registrar_cliente))
        self.main_ui.bt_listar_cliente.clicked.connect(lambda: (
            self.cambiar_pestaña(self.main_ui.page_4eliminar_cliente), 
            self.actualizar_tabla_clientes(Cliente.get())
            ))

        # Listado de clientes
        self.main_ui.bt_eliminar_cliente_2.clicked.connect(lambda: self.eliminar_row(self.main_ui.tabla_cliente, Cliente))
        self.main_ui.bt_volver_menu.clicked.connect(lambda: self.cambiar_pestaña(self.main_ui.page_1gestion_clientes))
        self.main_ui.buscar_cliente.textChanged.connect(self.buscar_clientes)
        self.main_ui.bt_modificar_cliente_2.clicked.connect(self.abrir_modificar_cliente)

        # Agregar cliente
        self.main_ui.bt_Aceptar_Cliente.clicked.connect(self.agregar_cliente)
        self.main_ui.bt_volver_cliente.clicked.connect(lambda: self.cambiar_pestaña(self.main_ui.page_1gestion_clientes))

        # Modificar cliente
        self.modificar_cliente_ui.bt_actulizar_tabla.clicked.connect(self.actualizar_cliente)
        self.modificar_cliente_ui.pushButton_7.clicked.connect(self.modificar_cliente_ui.hide)


        # Menu Transacciones Buttons
        self.main_ui.bt_agregar_Transaccion.clicked.connect(self.abrir_agregar_transaccion)
        self.main_ui.bt_listar_Transaccion.clicked.connect(lambda: (
            self.cambiar_pestaña(self.main_ui.page_8lista_transacciones),
            self.actualizar_tabla_transacciones(Transaccion.get())
            ))
        
        # Listado de transacciones
        self.main_ui.buscar_transacciones.textChanged.connect(self.buscar_transacciones)
        self.main_ui.bt_eliminar_transaccion.clicked.connect(lambda: self.eliminar_row(self.main_ui.tabla_transacciones, Transaccion))
        self.main_ui.bt_Volver_Menu.clicked.connect(lambda: self.cambiar_pestaña(self.main_ui.page_5gestion_transacciones))
        self.main_ui.bt_pdf_transaccion.clicked.connect(self.generar_pdf)

        # Agregar transacciones
        self.main_ui.bt_guardar_transaccion.clicked.connect(self.agregar_transaccion)
        self.main_ui.bt_volver_menu_transaccion.clicked.connect(lambda: self.cambiar_pestaña(self.main_ui.page_5gestion_transacciones))        


        # Listado de Pagos
        self.main_ui.pushButton_31.clicked.connect(self.actualizar_tabla_pagos)
        


    def abrir_agregar_transaccion(self):
        comboBox = self.main_ui.combobox_cliente
        comboBox.clear()
        # Rellenar ComboBox
        for cliente in Cliente.get():
            index = self.main_ui.combobox_cliente.count()
            comboBox.addItem(f"{cliente.nombre} {cliente.apellido}")
            comboBox.setItemData(index, cliente.id)

        # Setear campos de fecha a fecha actual
        self.main_ui.dateEdit_cliente1.setDate(QDate.currentDate())
        self.main_ui.dateEdit_cliente2.setDate(QDate.currentDate())

        self.cambiar_pestaña(self.main_ui.page_6agregar_transaccion)

    def actualizar_cliente(self):
        cliente = Cliente.get(self.cliente_modificado_id)

        cliente.nombre = self.modificar_cliente_ui.line_nombre_modificarCliente.text()
        cliente.apellido = self.modificar_cliente_ui.line_apellido_modificarCliente.text()
        cliente.telefono = self.modificar_cliente_ui.line_email_modificarCliente.text()
        cliente.cuit = int(self.modificar_cliente_ui.line_cuil_modificarCliente.text())
        
        if Cliente.modificar(cliente) == True:
            print("Se han actualizado los datos del cliente")
            self.actualizar_tabla_clientes(Cliente.get())
            self.modificar_cliente_ui.hide()
        else:
            print("Ha habido un error")

    def custom_close_event(self, event):
        self.modificar_cliente_ui.close()
        event.accept()

    def abrir_modificar_cliente(self):
        tabla = self.main_ui.tabla_cliente
        row_seleccionada = tabla.currentRow()

        # Si se selecciono una fila, extraigo cada columna
        if row_seleccionada >= 0:
            data = [tabla.item(row_seleccionada, col) for col in range(4)]
            self.cliente_modificado_id = data[0].data(Qt.ItemDataRole.UserRole)

            # Completo los campos de la ventana con los valores en la fila
            self.modificar_cliente_ui.line_nombre_modificarCliente.setText(data[0].text())
            self.modificar_cliente_ui.line_apellido_modificarCliente.setText(data[1].text())
            self.modificar_cliente_ui.line_email_modificarCliente.setText(data[2].text())
            self.modificar_cliente_ui.line_cuil_modificarCliente.setText(data[3].text())

            # Muestro la ventana
            self.modificar_cliente_ui.show()

    # def abrir_modificar_transaccion(self):
    #     tabla = self.main_ui.tabla_transacciones
    #     row_seleccionada = tabla.currentRow()

    #     # Si se selecciono una fila, extraigo cada columna
    #     if row_seleccionada >= 0:
    #         data = [tabla.item(row_seleccionada, col) for col in range(4)]
    #         self.transaccion_modificada_id = data[0].data(Qt.ItemDataRole.UserRole)

    #         # Completo los campos de la ventana con los valores en la fila
    #         self.modificar_cliente_ui.line_nombre_modificarCliente.setText(data[0].text())
    #         self.modificar_cliente_ui.line_apellido_modificarCliente.setText(data[1].text())
    #         self.modificar_cliente_ui.line_email_modificarCliente.setText(data[2].text())
    #         self.modificar_cliente_ui.line_cuil_modificarCliente.setText(data[3].text())

    #         # Muestro la ventana
    #         self.modificar_cliente_ui.show()
    def generar_pdf(self):
        tabla = self.main_ui.tabla_transacciones
        row_seleccionada = tabla.currentRow()

        if row_seleccionada >= 0:
            item = tabla.item(row_seleccionada, 0)

            if item:
                id = item.data(Qt.ItemDataRole.UserRole)
                transaccion = Transaccion.get(id)

                generar_pdf(transaccion)

    def setRowData(self, row, data, table, id):
        # Por cada columna de la tabla actualizo su valor con el correspondiente en data
        table.insertRow(row)
        for col, value in enumerate(data):
            item = QTableWidgetItem(str(value))
            table.setItem(row, col, item)
            item.setData(Qt.ItemDataRole.UserRole, id)

    def eliminar_row(self, table, instance_type):
        # Elimino la fila actualmente seleccionada de la tabla y de la BD.
        row_seleccionada = table.currentRow()

        if row_seleccionada >= 0:
            item = table.item(row_seleccionada, 0)

            if item:
                id = item.data(Qt.ItemDataRole.UserRole)
                if instance_type.eliminar(id) == True:
                    table.removeRow(row_seleccionada)
                    QMessageBox.information(self, "Éxito", "El elemento ha sido eliminado correctamente.")
                else:
                    QMessageBox.critical(self, "Error", "Se produjo un error al intentar eliminar el elemento.")
        else:
            QMessageBox.warning(self, "Error de seleccion", "Si desea eliminar un elemento, primero debe seleccionarlo.")

    def login(self):
        # Inicio sesión
        contraseña = self.login_UiForm.lineEdit_2.text()
        nombre = self.login_UiForm.lineEdit.text()

        usuario = Usuario.login(nombre, contraseña)

        if usuario != None:
            self.login_ui.hide()
            self.main_ui.show()
            QMessageBox.information(self, "Éxito", f"Inicio de sesión exitoso\n Bienvenido/a {usuario.nombre}.")
        else:
            QMessageBox.warning(self, "Error de Inicio de Sesión", "Nombre de usuario o contraseña incorrectos.")

    def cambiar_pestaña(self, pestaña):
        self.main_ui.stackedWidget.setCurrentWidget(pestaña)

    def buscar_clientes(self):
        # Tomo todos los clientes, filtro por el texto de la barra de busqueda y actualizo la tabla
        clientes = Cliente.get()
        search_text = self.main_ui.buscar_cliente.text().lower()
        filtered_clients = [cliente for cliente in clientes if search_text in cliente.nombre.lower()]
        self.actualizar_tabla_clientes(filtered_clients)

    def actualizar_tabla_clientes(self, clientes):
        # Tomo la tabla de clientes y elimino todas las filas
        tabla = self.main_ui.tabla_cliente
        tabla.setRowCount(0)

        # Por cada cliente actualizo de una en una las filas de la tabla
        for row, cliente in enumerate(clientes):
            data = [cliente.nombre, cliente.apellido, "-" if cliente.telefono is None else cliente.telefono, cliente.cuit]
            self.setRowData(row, data, tabla, cliente.id)

    def agregar_cliente(self):
        nombre = self.main_ui.line_nombre_registro_cliente
        apellido = self.main_ui.line_apellido_registro_cliente
        telefono = self.main_ui.lineEdit
        cuit = self.main_ui.spinBox

        nuevo_cliente = Cliente(nombre.text(), apellido.text(), cuit.value(), telefono.text() if telefono.text() != "" else None)

        if nuevo_cliente.crear() is True:
            QMessageBox.information(self, "Éxito", f"{nuevo_cliente.nombre} {nuevo_cliente.apellido} ha sido agregado exitosamente.")
            nombre.clear()
            apellido.clear()
            telefono.clear()
            cuit.setValue(0)
        else:
            QMessageBox.critical(self, "Error al crear cliente", "Un cliente con el CUIT proporcionado ya existe.")
        
    def actualizar_tabla_transacciones(self, transacciones):
        # Tomo la tabla de transacciones y elimino todas las filas
        tabla = self.main_ui.tabla_transacciones
        tabla.setRowCount(0)

        # Por cada transaccion actualizo de una en una las filas de la tabla
        for row, transaccion in enumerate(transacciones):
            cliente = Cliente.get(transaccion.id_cliente)
            data = [cliente.nombre, transaccion.valor_final, transaccion.cuotas, transaccion.aumento, transaccion.valor_cuota]

            self.setRowData(row, data, tabla, transaccion.id)
        
    def buscar_transacciones(self):
        # Tomo todas las transacciones, filtro por el texto de la barra de busqueda y actualizo la tabla
        transacciones = Transaccion.get()

        search_text = self.main_ui.buscar_transacciones.text().lower()
        filtered_transactions = []

        for transaccion in transacciones:
            cliente = Cliente.get(transaccion.id_cliente)

            if search_text in cliente.nombre.lower():
                filtered_transactions.append(transaccion)

        self.actualizar_tabla_transacciones(filtered_transactions)

    def agregar_transaccion(self):
        id_cliente = self.main_ui.combobox_cliente.itemData(self.main_ui.combobox_cliente.currentIndex())
        valor_final = self.main_ui.doubleSpinBox_cliente1
        cuotas = self.main_ui.spinBox_2_cliente
        valor_cuota = self.main_ui.doubleSpinBox_cliente2
        aumento = self.main_ui.doubleSpinBox_cliente3
        fecha_boleto = self.main_ui.dateEdit_cliente1
        fecha_primera_cuota = self.main_ui.dateEdit_cliente2

        nueva_transaccion = Transaccion(
            id_cliente, 
            valor_final.value(), 
            cuotas.value(), 
            valor_cuota.value(), 
            aumento.value(),
            fecha_boleto.date().toPyDate(),
            fecha_primera_cuota.date().toPyDate()
            )
        if nueva_transaccion.crear() == True:
            QMessageBox.information(self, "Exito", "Se ha agregado la transacción exitosamente.")
            self.main_ui.combobox_cliente.setCurrentIndex(0)
            valor_final.setValue(0)
            cuotas.setValue(0)
            valor_cuota.setValue(0)
            aumento.setValue(0)
            fecha_boleto.setDate(QDate.currentDate())
            fecha_primera_cuota.setDate(QDate.currentDate())
        else:
            QMessageBox.critical(self, "Error", "El cliente seleccionado no existe.")

    def actualizar_tabla_pagos(self):
        # Tomo la tabla de pagos y elimino todas las filas
        tabla = self.main_ui.tableWidget
        tabla.setRowCount(0)

        # Filtros
        estado = self.main_ui.comboBox.currentIndex()
        mes = self.main_ui.comboBox_2.currentIndex() + 1
        año = self.main_ui.comboBox_3.currentText()

        transacciones = Transaccion.get()

        row_counter = 0

        for transaccion in transacciones:
            cuotas = transaccion.get_cuotas()

            # Por cada cuota actualizo de una en una las filas de la tabla
            for cuota in cuotas:
                estado_cuota = cuota["estado"]
                fecha = cuota["fecha"]

                # Si la cuota coincide con los filtros
                if estado == estado_cuota and mes == fecha.month and int(año) == fecha.year:

                    cliente = Cliente.get(transaccion.id_cliente)
                    nombre_completo = f"{cliente.nombre} {cliente.apellido}"
                    fecha_pago = cuota["fecha_pago"] if cuota["fecha_pago"] != None else "-"

                    data = [nombre_completo, cuota["cuota"], cuota["valor"], fecha_pago]

                    self.setRowData(row_counter, data, tabla, cuota["id"])


            row_counter += tabla.rowCount()

    def abrir_lista_pagos(self):
        # Relleno el comboBox de AÑO
        años = list(set(int(year[0]) for year in Transaccion.get_años_cuotas()))
        años.sort()

        comboBox_año = self.main_ui.comboBox_3
        comboBox_año.clear()

        for año in años:
            comboBox_año.addItem(str(año))

        # Muestro lista de pagos
        self.actualizar_tabla_pagos

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    sys.exit(app.exec())