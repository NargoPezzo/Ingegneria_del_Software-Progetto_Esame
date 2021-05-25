from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton

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
        self.setLayout(self.v_layout)

    def get_form_entry(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit