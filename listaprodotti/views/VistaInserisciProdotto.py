from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from prodotto.model.Prodotto import Prodotto


class VistaInserisciProdotto(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciProdotto, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}

        self.v_layout = QVBoxLayout()

        self.get_form_entry("Marca")
        self.get_form_entry("Nome")
        self.get_form_entry("Categoria")
        self.get_form_entry("Prezzo")
        self.get_form_entry("Quantità")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_prodotto)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Prodotto")

    def get_form_entry(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    def add_prodotto(self):
        marca = self.info["Marca"].text()
        nome = self.info["Nome"].text()
        categoria = self.info["Categoria"].text()
        prezzo = self.info["Prezzo"].text()
        quantita = self.info["Quantità"].text()

        if marca == "" or nome == "" or categoria == "" or prezzo == "" or quantita == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_prodotto(Prodotto((marca+nome).lower(), marca, nome, categoria, prezzo, quantita))
            self.callback()
            self.close()