from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpinBox, QPushButton, QMessageBox
from PyQt5 import QtGui

from carrello.model.Carrello import Carrello
from listaprodotti.model.ListaProdotti import ListaProdotti
from prodotto.controller.ControlloreProdotto import ControlloreProdotto


class VistaAggiungiQuantita(QWidget):
    def __init__(self, prodotto, carrello, parent=None):
        super(VistaAggiungiQuantita, self).__init__(parent)
        self.prodotto = prodotto

        self.carrello = carrello
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))

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

      #  self.lista_carrello = Carrello()  #aggiunta
      #  self.lista_prodotti = ListaProdotti() #aggiunta

        btn_conferma = QPushButton("Conferma")
        self.v_layout.addWidget(btn_conferma)
        btn_conferma.clicked.connect(self.aggiungi_al_carrello) #aggiunta
        self.setLayout(self.v_layout)
        self.close() #aggiunta


    def aggiungi_al_carrello(self):#DA FARE E RIVEDERE
        if int(self.spin.text()) > int(self.prodotto.quantita_magazzino):
            QMessageBox.critical(self, 'Errore', 'La domanda è maggiore della possibilità',
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.carrello.aggiungi_al_carrello(self.prodotto, int(self.spin.text()))
            self.prodotto.quantita_magazzino = int(self.prodotto.quantita_magazzino) - int(self.spin.text())
            self.carrello.save_data()
            self.close()
      #  if  self.prodotto.quantita_magazzino == 0: DA VEDERE



















