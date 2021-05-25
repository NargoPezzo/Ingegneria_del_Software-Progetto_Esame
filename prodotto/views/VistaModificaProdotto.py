from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from prodotto.controller.ControlloreProdotto import ControlloreProdotto


class VistaModificaProdotto(QWidget):
    def __init__(self, prodotto, parent=None):
        super(VistaModificaProdotto, self).__init__(parent)
        self.controller = ControlloreProdotto(prodotto)
        self.info = {}

        self.v_layout = QVBoxLayout()

        self.get_form_entry("Nuovo Prezzo")
        self.get_form_entry("Nuova Quantità")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_conferma = QPushButton("Conferma")
        self.v_layout.addWidget(btn_conferma)
        btn_conferma.clicked.connect(self.modifica_prodotto)
        self.setLayout(self.v_layout)

    def get_form_entry(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    def modifica_prodotto(self):

        prezzo = self.info["Nuovo Prezzo"].text()
        quantita = self.info["Nuova Quantità"].text()

        if prezzo == "" or quantita == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)

        else:
            self.controller.set_prezzo_prodotto(prezzo)
            self.controller.set_quantita_prodotto(quantita)

            #self.callback()
            self.close()
