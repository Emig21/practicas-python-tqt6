import sys
from PyQt6.QtWidgets import QApplication, QWidget

class Ventana(QWidget):
    
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(600, 250, 250, 250)
        self.setWindowTitle("Mi Primera Ventana")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana1 = Ventana()
    sys.exit(app.exec())