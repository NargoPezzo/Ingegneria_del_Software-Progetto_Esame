from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton


from prodotto.controller.ControlloreProdotto import ControlloreProdotto


class VistaCliente(QWidget):
    def __init__(self, prodotto, elimina_prodotto, elimina_callback, aggiungi_carrello, parent=None):
        super(VistaCliente, self).__init__(parent)
        self.controller = ControlloreProdotto(prodotto)
        self.elimina_cliente = elimina_prodotto
        self.elimina_callback = elimina_callback
        self.aggiungi_carrello = aggiungi_carrello

        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_marca_prodotto() + " " + self.controller.get_nome_prodotto())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_label_info("Prezzo", self.controller.get_prezzo_prodotto()))
        v_layout.addWidget(self.get_label_info("Categoria", self.controller.get_categoria_prodotto))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_prodotto_click)
        v_layout.addWidget(btn_elimina)

        btn_aggiungi = QPushButton("Aggiungi al Carrello")
        btn_aggiungi.clicked.connect(self.aggiungi_carrello_click)
        v_layout.addWidget(btn_aggiungi)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_marca_prodotto() + " " + self.controller.get_nome_prodotto())

    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(17)
        current_label.setFont(current_font)
        return current_label

    def elimina_cliente_click(self):
        self.elimina_cliente(self.controller.get_id_cliente())
        self.elimina_callback()
        self.close()
