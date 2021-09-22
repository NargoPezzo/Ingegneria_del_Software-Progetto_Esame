from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, \
    QComboBox


from prodotto.model.Prodotto import Prodotto
from PyQt5 import QtGui


class VistaInserisciProdotto(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciProdotto, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(QLabel("Categoria"))
        self.combo_categoria = QComboBox()
        self.combo_categoria_model = QStandardItemModel(self.combo_categoria)

        self.add_combobox_item("Telefonia")
        self.add_combobox_item("Informatica")
        self.add_combobox_item("Piccoli Elettrodomestici")
        self.add_combobox_item("Elettrodomestici")
        self.add_combobox_item("TV e Hi-Fi")

        self.combo_categoria.setModel(self.combo_categoria_model)
        self.v_layout.addWidget(self.combo_categoria)

        self.get_form_entry("Marca")
        self.get_form_entry("Nome")
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

    def add_combobox_item(self, tipo):
        item = QStandardItem()
        item.setText(tipo)
        item.setEditable(False)
        self.combo_categoria_model.appendRow(item)

    def add_prodotto(self):

        marca = self.info["Marca"].text()
        nome = self.info["Nome"].text()
        categoria = self.combo_categoria.currentText()

        prezzo = self.info["Prezzo"].text()
        quantita = self.info["Quantità"].text()

        if marca == "" or nome == "" or categoria == "" or prezzo == "" or quantita == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)


        else:
            self.controller.aggiungi_prodotto(Prodotto((marca+nome).lower(), marca, nome, categoria, prezzo, quantita, 0))
            self.callback()
            self.close()
