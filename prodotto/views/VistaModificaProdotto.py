from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

class VistaModificaProdotto(QWidget):
    def __init__(self, prodotto, update, parent=None):
        super(VistaModificaProdotto, self).__init__(parent)
        self.prodotto = prodotto
        self.info = {}
        self.update = update
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

        nuovoprezzo = self.info["Nuovo Prezzo"].text()
        nuovaquantita = self.info["Nuova Quantità"].text()

        if nuovoprezzo == "" or nuovaquantita == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)

        else:
            self.prodotto.prezzo = nuovoprezzo
            self.prodotto.quantita = nuovaquantita
            self.update()
            self.close()
