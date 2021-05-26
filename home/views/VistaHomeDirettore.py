from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from carrello.views.VistaCarrello import VistaCarrello
from listaclienti.views.VistaListaClienti import VistaListaClienti
from listadipendenti.views.VistaListaDipendenti import VistaListaDipendenti
from listaprodotti.views.VistaListaProdotti import VistaListaProdotti


class VistaHomeDirettore(QWidget):

    def __init__(self, parent=None):
        super(VistaHomeDirettore, self).__init__(parent)


        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_generic_button("Magazzino Prodotti", self.go_lista_prodotti), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Gestione Clienti", self.go_lista_clienti), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Gestione Dipendenti", self.go_lista_dipendenti), 1, 2)
        grid_layout.addWidget(self.get_generic_button("Carrello", self.go_carrello), 1, 3)
        grid_layout.addWidget(self.get_generic_button("Statistiche sulle vendite", self.go_statistiche), 1, 4)

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

    def go_carrello(self):
        self.vistacarrello = VistaCarrello()
        self.vistacarrello.show()


    def go_lista_dipendenti(self):
        self.vista_lista_dipendenti = VistaListaDipendenti()
        self.vista_lista_dipendenti.show()

    def go_statistiche(self):
        return

