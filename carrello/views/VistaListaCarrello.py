from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from carrello.controller.ControlloreCarrello import ControlloreCarrello
from carrello.model.Carrello import Carrello
from carrello.views.VistaCarrello import VistaCarrello
from prodotto.views.VistaProdotto import VistaProdotto


class VistaListaCarrello(QWidget):
    def __init__(self, parent=None):
        super(VistaListaCarrello, self).__init__(parent)

        self.controller = ControlloreCarrello()
        self.carrello = Carrello()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton("Checkout")
        new_button.clicked.connect(self.show_checkout)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600,300)
        self.setWindowTitle("Carrello")

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
        prodotto_selezionato = self.controller.get_prodotto_by_index(selected)
        self.vista_prodotto = VistaCarrello(prodotto_selezionato, self.controller.elimina_prodotto_by_id, self.update_ui, self.carrello) ###VA CAMBIATA
        self.vista_prodotto.show()

    def show_checkout(self):
        return

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for prodotto in self.controller.get_lista_dei_prodotti():
            item = QStandardItem()
            item.setText(prodotto.marca + " " + prodotto.nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()