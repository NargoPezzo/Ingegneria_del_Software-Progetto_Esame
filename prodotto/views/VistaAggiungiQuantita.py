from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpinBox, QPushButton


class VistaAggiungiQuantita(QWidget):
    def __init__(self, prodotto, parent=None):
        super(VistaAggiungiQuantita, self).__init__(parent)
        self.prodotto = prodotto

        self.setWindowTitle("Aggiungi Prodotto al Carrello")
        self.resize(250, 100)

        self.v_layout = QVBoxLayout()

        label = QLabel("Quantità da acquistare")
        self.v_layout.addWidget(label)

        self.spin = QSpinBox(self)
        self.spin.setGeometry(100, 100, 250, 40)
        self.spin.setRange(1, 99)
        self.spin.setSizeIncrement(1, 1)
        self.v_layout.addWidget(self.spin)

        btn_conferma = QPushButton("Conferma")
        self.v_layout.addWidget(btn_conferma)
        self.setLayout(self.v_layout)
