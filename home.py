# Importar librerías
from PyQt6.QtWidgets import (QMainWindow, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QApplication, QLabel)


class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        # Layouts necesarios
        self.principal_layout = QVBoxLayout()
        self.vertical_layout1 = QVBoxLayout()
        self.vertical_layout2 = QVBoxLayout()
        self.encode_layout = QHBoxLayout()
        self.decode_layout = QHBoxLayout()

        # Label de codificación
        self.label1 = QLabel()
        self.label1.setText('Ingrese el mensaje para codificar:')
        self.vertical_layout1.addWidget(self.label1)

        # Textbox para ingresar un mensaje
        self.textbox1 = QLineEdit(self)
        self.vertical_layout1.addWidget(self.textbox1)

        self.encode_layout.addLayout(self.vertical_layout1)  # Layout para el cifrado

        # Botón para encriptar
        self.encode_button = QPushButton('Encriptar', self)
        # self.encode_button.clicked.connect()
        self.encode_layout.addWidget(self.encode_button)

        # Agregar al layout principal
        self.principal_layout.addLayout(self.encode_layout)

        # Label para mostrar la encriptación
        self.encrypted_message = QLabel()
        self.encrypted_message.setText('-')
        self.principal_layout.addWidget(self.encrypted_message)

        # Label de decodificación
        self.label2 = QLabel()
        self.label2.setText('\nIngrese el mensaje para decodificar:')
        self.vertical_layout2.addWidget(self.label2)

        # Textbox para ingresar un "código"
        self.textbox2 = QLineEdit(self)
        self.vertical_layout2.addWidget(self.textbox2)

        self.decode_layout.addLayout(self.vertical_layout2)

        # Botón para desencriptar
        self.decode_button = QPushButton('Desencriptar', self)
        # self.decode_button.clicked.connect()
        self.decode_layout.addWidget(self.decode_button)

        # Agregar al layout principal
        self.principal_layout.addLayout(self.decode_layout)

        # Label para mostrar el mensaje descifrado
        self.decrypted_message = QLabel()
        self.decrypted_message.setText('-')
        self.principal_layout.addWidget(self.decrypted_message)

        # Agregar layout principal a la ventana general
        widget = QWidget()
        widget.setLayout(self.principal_layout)
        self.setCentralWidget(widget)

    def load_ui(self):
        # Función para mostrar esta ventana
        self.show()

    def encode(self):
        # Se escribe el mensaje ya encriptado
        self.encrypted_message.setText('El mensaje encriptado es: ')

    def decode(self):
        # Se escribe el mensaje ya encriptado
        self.decrypted_message.setText('El mensaje desencriptado es: ')
