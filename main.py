import sys
from PyQt6.QtWidgets import QApplication
from window import StartWindow

app = QApplication(sys.argv)  # Crear la aplicación
start_window = StartWindow()


def load_window():
    start_window.show()  # Mostrar ventana


def main():
    start_window.hide()
    load_window()

    app.exec()  # Inicializar


main()
