# Importar librerías
import sys
import numpy as np
from home import Home
from PyQt6.QtWidgets import (QMainWindow, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QApplication,
                             QLabel)

app = QApplication(sys.argv)


class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.test_home = Home()  # Ventana siguiente
        # Layouts necesarios
        self.principal_layout = QVBoxLayout()
        self.column1 = QVBoxLayout()
        self.column2 = QVBoxLayout()
        self.column3 = QVBoxLayout()
        self.array = QHBoxLayout()

        # Label principal
        self.label = QLabel()
        self.label.setText('Ingrese la clave del cifrado')
        self.principal_layout.addWidget(self.label)

        # Columna 1
        self.n1 = QLineEdit(self)
        self.column1.addWidget(self.n1)

        self.n2 = QLineEdit(self)
        self.column1.addWidget(self.n2)

        self.n3 = QLineEdit(self)
        self.column1.addWidget(self.n3)

        # Columna 2
        self.n4 = QLineEdit(self)
        self.column2.addWidget(self.n4)

        self.n5 = QLineEdit(self)
        self.column2.addWidget(self.n5)

        self.n6 = QLineEdit(self)
        self.column2.addWidget(self.n6)

        # Columna 3
        self.n7 = QLineEdit(self)
        self.column3.addWidget(self.n7)

        self.n8 = QLineEdit(self)
        self.column3.addWidget(self.n8)

        self.n9 = QLineEdit(self)
        self.column3.addWidget(self.n9)

        # Unificar los espacios para la matriz
        self.array.addLayout(self.column1)
        self.array.addLayout(self.column2)
        self.array.addLayout(self.column3)

        # Agregar la matriz al layout principal
        self.principal_layout.addLayout(self.array)

        # Botón de continuar
        self.button = QPushButton('Continuar', self)
        self.button.clicked.connect(self.continue_click)  # Acción al dar click al botón
        self.principal_layout.addWidget(self.button)

        # Agregar layout principal a la ventana general
        widget = QWidget()
        widget.setLayout(self.principal_layout)
        self.setCentralWidget(widget)

    def continue_click(self):
        # Se cierra la ventana actual, se guardan los datos y se abre la sigueinte ventana
        self.close()
        self.determinant()

    def determinant(self):
        # Crear la matriz a partir de las variables
        n1 = self.n1.text()
        n2 = self.n2.text()
        n3 = self.n3.text()
        n4 = self.n4.text()
        n5 = self.n5.text()
        n6 = self.n6.text()
        n7 = self.n7.text()
        n8 = self.n8.text()
        n9 = self.n9.text()
        array = np.array([[n1, n4, n7],
                          [n2, n5, n8],
                          [n3, n6, n9]])

        # Resultado de la eterminante
        det = np.linalg.det(array)

        # Condición de la determinante
        if det != 0:
            yes_no = True
        else:
            yes_no = False

        if yes_no:
            self.test_home.load_ui()
