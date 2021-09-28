from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel

from carrello.views.VistaAcquistoCarrello import VistaProdottoCarrello
from carrello.views.VistaListaCarrello import VistaListaCarrello
from listaclienti.views.VistaListaClienti import VistaListaClienti
from listadipendenti.views.VistaListaDipendenti import VistaListaDipendenti
from listaprodotti.views.VistaListaProdotti import VistaListaProdotti
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

from statistiche.view.VistaStatistiche import VistaStatistiche


class VistaHomeDirettore(QWidget):

    def __init__(self, parent=None):
        super(VistaHomeDirettore, self).__init__(parent)


        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_icon('logos/home logos/magazzino.png'), 0, 0)
        grid_layout.addWidget(self.get_icon('logos/home logos/clienti.png'), 0, 1)
        grid_layout.addWidget(self.get_icon('logos/home logos/dipendenti.png'), 0, 2)
        grid_layout.addWidget(self.get_icon('logos/home logos/carrello.png'), 0, 3)
        grid_layout.addWidget(self.get_icon('logos/home logos/statistiche.png'), 0, 4)

        grid_layout.addWidget(self.get_generic_button("Magazzino Prodotti", self.go_lista_prodotti), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Gestione Clienti", self.go_lista_clienti), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Gestione Dipendenti", self.go_lista_dipendenti), 1, 2)
        grid_layout.addWidget(self.get_generic_button("Carrello", self.go_carrello), 1, 3)
        grid_layout.addWidget(self.get_generic_button("Statistiche", self.go_statistiche), 1, 4)


        self.setLayout(grid_layout)
        self.setFixedSize(700, 200)
        self.setWindowTitle("Negozio di Elettronica")
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))

    '''
    Questa funzione restituisce un bottone generico dato il titolo
    '''
    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setFixedWidth(120)
        button.clicked.connect(on_click)
        return button

    def get_icon(self, path):
        label_logo = QLabel(self)
        pixmap = QPixmap(path)
        pixmap = pixmap.scaledToWidth(120)
        pixmap = pixmap.scaledToHeight(120)
        label_logo.setPixmap(pixmap)
        label_logo.setFixedSize(120, 120)
        label_logo.setAlignment(Qt.AlignCenter)
        return label_logo



    def go_lista_prodotti(self):
        self.vista_lista_prodotti = VistaListaProdotti()
        self.vista_lista_prodotti.show()

    def go_lista_clienti(self):
        self.vista_lista_clienti = VistaListaClienti()
        self.vista_lista_clienti.show()

    def go_carrello(self):
        self.vistacarrello = VistaListaCarrello()
        self.vistacarrello.show()


    def go_lista_dipendenti(self):
        self.vista_lista_dipendenti = VistaListaDipendenti()
        self.vista_lista_dipendenti.show()

    def go_statistiche(self):
        self.vista_statistiche = VistaStatistiche()
        self.vista_statistiche.show()

