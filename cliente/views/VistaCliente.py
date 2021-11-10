from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton
from PyQt5 import QtGui
from cliente.controller.ControlloreCliente import ControlloreCliente

"""
La classe VistaCliente apre una finestra a schermo che si occupa di mostrare all'utente le informazioni del cliente.
La classe VistaCliente estende la classe QWidget
"""


class VistaCliente(QWidget):
    def __init__(self, cliente, elimina_cliente, elimina_callback, parent=None):
        super(VistaCliente, self).__init__(parent)
        self.controller = ControlloreCliente(cliente)
        self.elimina_cliente = elimina_cliente
        self.elimina_callback = elimina_callback
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))

        v_layout = QVBoxLayout()

        #Impostazioni generali per titolo finestra
        label_nome = QLabel(self.controller.get_nome_cliente() + " " + self.controller.get_cognome_cliente())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #Aggiunge tramite metodo get_label_info il titolo di una informazione e l'informazione stessa tramite controller
        v_layout.addWidget(self.get_label_info("Codice ID", self.controller.get_id_cliente()))
        v_layout.addWidget(self.get_label_info("Codice Fiscale", self.controller.get_cf_cliente()))
        v_layout.addWidget(self.get_label_info("Indirizzo", self.controller.get_indirizzo_cliente()))
        v_layout.addWidget(self.get_label_info("Email", self.controller.get_email_cliente()))
        v_layout.addWidget(self.get_label_info("Telefono", self.controller.get_telefono_cliente()))
        v_layout.addWidget(self.get_label_info("Età", self.controller.get_eta_cliente()))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #Bottone per eliminare un cliente
        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_cliente_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_cliente() + " " + self.controller.get_cognome_cliente())

    #Metodo che prende come parametri il testo di una informazione e il valore assegnato come sopra tramite il controller
    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(17)
        current_label.setFont(current_font)
        return current_label

    #Metodo che si occupa di eliminare il cliente
    def elimina_cliente_click(self):
        self.elimina_cliente(self.controller.get_id_cliente())
        self.elimina_callback()
        self.close()
