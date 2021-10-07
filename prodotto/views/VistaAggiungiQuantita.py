from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpinBox, QPushButton, QMessageBox
from PyQt5 import QtGui



class VistaAggiungiQuantita(QWidget):
    def __init__(self, prodotto, carrello, parent=None):
        super(VistaAggiungiQuantita, self).__init__(parent)
        self.prodotto = prodotto
        self.msg = QMessageBox()

        self.carrello = carrello
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))

        self.setWindowTitle("Aggiungi al Carrello")
        self.resize(300, 100)

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
        btn_conferma.clicked.connect(self.aggiungi_al_carrello)
        self.setLayout(self.v_layout)
        self.close()


    def aggiungi_al_carrello(self):
        if self.carrello.verifica_quantita_prodotto(self.prodotto, int(self.spin.text())) is True:
            self.carrello.aggiungi_al_carrello(self.prodotto)
            self.carrello.save_data()
            self.close()
        else:
            self.msg.setText("ERRORE: la quantità selezionata non è presente in magazzino")
            self.msg.exec_()


















