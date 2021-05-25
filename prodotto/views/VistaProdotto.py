from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QGridLayout, \
    QHBoxLayout

from prodotto.controller.ControlloreProdotto import ControlloreProdotto
from carrello.controller.ControlloreCarrello import ControlloreCarrello
from prodotto.views.VistaModificaProdotto import VistaModificaProdotto


class VistaProdotto(QWidget):
    def __init__(self, prodotto, elimina_prodotto, elimina_callback, parent=None):
        super(VistaProdotto, self).__init__(parent)
        self.controller = ControlloreProdotto(prodotto)
        self.elimina_prodotto = elimina_prodotto
        self.elimina_callback = elimina_callback
        self.prodotto = prodotto
        #self.modifica = modifica
        #self.aggiungi_carrello = aggiungi_carrello

        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        label_nome = QLabel(self.controller.get_marca_prodotto() + " " + self.controller.get_nome_prodotto())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome, )

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_label_info("Prezzo", self.controller.get_prezzo_prodotto()))
        v_layout.addWidget(self.get_label_info("Categoria", self.controller.get_categoria_prodotto()))
        v_layout.addWidget(self.get_label_info("Quantità", self.controller.get_quantita_disp()))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton(" RIMUOVI DAL MAGAZZINO ")
        btn_elimina.clicked.connect(self.elimina_prodotto_click)
        btn_elimina.setStyleSheet("background-color: red")
        h_layout.addWidget(btn_elimina)

        btn_carrello = QPushButton("Aggiungi al Carrello")
        #btn_carrello.clicked.connect(self.aggiungi_carrello)
        h_layout.addWidget(btn_carrello)

        btn_modify = QPushButton("Modifica Quantità e Prezzo")
        btn_modify.clicked.connect(self.show_modifica_prodotto)
        h_layout.addWidget(btn_modify)

        v_layout.addLayout(h_layout)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_marca_prodotto() + " " + self.controller.get_nome_prodotto())

    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(17)
        current_label.setFont(current_font)
        return current_label

    def elimina_prodotto_click(self):
        self.elimina_prodotto(self.controller.get_id_prodotto())
        self.elimina_callback()
        self.close()

    def show_modifica_prodotto(self):
        self.vista_modifica_prodotto = VistaModificaProdotto(self.prodotto)
        self.vista_modifica_prodotto.show()
