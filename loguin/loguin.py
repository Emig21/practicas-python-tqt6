import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import(QApplication,
QLabel, QWidget, QLineEdit, QPushButton,
QMessageBox, QCheckBox)

class Loguin(QWidget):

    def __init__(self):
        super.__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setGeometry(600, 250, 350,250)
        self.setWindowTitle("Loguin")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        self.logged = False

        user_label 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    loguin = Loguin()
    sys.exit(loguin.exec())