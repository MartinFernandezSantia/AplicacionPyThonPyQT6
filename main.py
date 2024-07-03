from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.uic.load_ui import loadUi

import sys
import os

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi(os.path.join("Front", "Proyecto_Inmobiliaria.ui"), self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    mi_app.show()
    sys.exit(app.exec())
