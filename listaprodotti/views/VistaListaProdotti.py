from PyQt5.QtCore import QSortFilterProxyModel, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QLineEdit, QSpacerItem, \
    QMessageBox

from carrello.controller.ControlloreCarrello import ControlloreCarrello
from listaprodotti.controller.ControlloreListaProdotti import ControlloreListaProdotti
from listaprodotti.views.VistaInserisciProdotto import VistaInserisciProdotto
from prodotto.views.VistaProdotto import VistaProdotto
from PyQt5 import QtGui


class VistaListaProdotti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaProdotti, self).__init__(parent)

        self.carrello = ControlloreCarrello()
        self.controller = ControlloreListaProdotti()
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))
        main_layout = QHBoxLayout()

        v_layout = QVBoxLayout()

        self.list_view = QListView()
        self.update_ui()

        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setSourceModel(self.listview_model)
        self.filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.filter_proxy_model.setFilterKeyColumn(0)

        search_field = QLineEdit()
        search_field.setStyleSheet('font-size: 15px; height: 30px;')
        search_field.textChanged.connect(self.filter_proxy_model.setFilterRegExp)
        v_layout.addWidget(search_field)

        self.list_view.setModel(self.filter_proxy_model)

        v_layout.addWidget(self.list_view)
        main_layout.addLayout(v_layout)

        buttons_layout = QVBoxLayout()

        buttons_layout.addItem(QSpacerItem(40, 40))

        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton("Nuovo")
        new_button.clicked.connect(self.show_new_prodotto)
        new_button.setStyleSheet("background-color: lightgreen")
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)
        self.resize(600,300)
        self.setWindowTitle("Lista Prodotti")

    def show_selected_info(self):
        try:
            selected = self.list_view.selectedIndexes()[0]
            sourceindex = self.toSourceIndex(selected)
            prodotto_selezionato = self.controller.get_prodotto_by_index(sourceindex)
            self.vista_prodotto = VistaProdotto(prodotto_selezionato, self.controller.elimina_prodotto_by_id, self.update_ui, self.carrello)
            self.vista_prodotto.show()
        except IndexError:
            QMessageBox.critical(self, 'Errore', 'Per favore, seleziona un prodotto', QMessageBox.Ok, QMessageBox.Ok)

    def show_new_prodotto(self):
        self.vista_inserisci_prodotto = VistaInserisciProdotto(self.controller, self.update_ui)
        self.vista_inserisci_prodotto.show()

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

    def toSourceIndex(self, index):
        return self.filter_proxy_model.mapToSource(index).row()


