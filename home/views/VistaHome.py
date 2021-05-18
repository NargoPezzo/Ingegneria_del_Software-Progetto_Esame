from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from listaclienti.views.VistaListaClienti import VistaListaClienti
from listadipendenti.views.VistaListaDipendenti import VistaListaDipendenti
from listaprodotti.views.VistaListaProdotti import VistaListaProdotti


class VistaHome(QWidget):

    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_generic_button("Lista Prodotti", self.go_lista_prodotti), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Lista Clienti", self.go_lista_clienti), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Lista Dipendenti", self.go_lista_dipendenti), 0, 2)
        #grid_layout.addWidget(self.get_generic_button("Carrello", self.go_carrello), 0, 2)

        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle("Negozio di Elettronica")

    '''
    Questa funzione restituisce un bottone generico dato il titolo
    '''
    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_lista_prodotti(self):
        self.vista_lista_prodotti = VistaListaProdotti()
        self.vista_lista_prodotti.show()

    def go_lista_clienti(self):
        self.vista_lista_clienti = VistaListaClienti()
        self.vista_lista_clienti.show()

    def go_lista_dipendenti(self):
        self.vista_lista_dipendenti = VistaListaDipendenti()
        self.vista_lista_dipendenti.show()

