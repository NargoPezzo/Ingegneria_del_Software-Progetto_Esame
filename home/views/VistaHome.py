from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QMainWindow

from carrello.views.VistaListaCarrello import VistaListaCarrello
from listaclienti.views.VistaListaClienti import VistaListaClienti
from listaprodotti.views.VistaListaProdotti import VistaListaProdotti
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

from statistiche.views.VistaStats import VistaStats


class VistaHome(QMainWindow):

    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)

        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_icon('logos/home logos/magazzino.png'), 0, 0)
        grid_layout.addWidget(self.get_icon('logos/home logos/clienti.png'), 0, 1)
        grid_layout.addWidget(self.get_icon('logos/home logos/carrello.png'), 0, 2)

        grid_layout.addWidget(self.get_generic_button("Lista Prodotti", self.go_lista_prodotti), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Lista Clienti", self.go_lista_clienti), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Carrello", self.go_carrello), 1, 2)

        self.setLayout(grid_layout)
        self.setFixedSize(400, 200)
        self.setWindowTitle("Negozio di Elettronica")
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))


    '''
    Questa funzione restituisce un bottone generico dato il titolo
    '''
    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
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

    def go_statistiche(self):
        self.vista_statistiche = VistaStats()
        self.vista_statistiche.show()



