from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5 import QtGui
from carrello.controller.ControlloreCarrello import ControlloreCarrello
from carrello.model.Carrello import Carrello
from carrello.views.VistaProdottoCarrello import VistaProdottoCarrello
from prodotto.views.VistaProdotto import VistaProdotto
from statistiche.view.VistaStatistiche import VistaStatistiche


class VistaListaCarrello(QWidget):
    def __init__(self,  parent=None):
        super(VistaListaCarrello, self).__init__(parent)

        self.controller = ControlloreCarrello()
        self.carrello = Carrello()
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))

        main_layout = QHBoxLayout()

        self.table_widget = QTableWidget()
        self.update_ui()


        main_layout.addWidget(self.table_widget)









        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton("Checkout")
        new_button.clicked.connect(self.aggiungi_alle_statistiche)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(new_button)

        self.setLayout(main_layout)
        self.resize(600, 300)
        self.setWindowTitle("Carrello")

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
        prodotto_selezionato = self.controller.get_prodotto_by_index(selected)
        self.vista_prodotto = VistaProdottoCarrello(prodotto_selezionato, self.controller.elimina_prodotto_by_id, self.update_ui, self.carrello)
        self.vista_prodotto.show()

    def aggiungi_alle_statistiche(self):
        self.vista_statistiche = VistaStatistiche()
        self.vista_statistiche.show()
        self.close()

    def update_ui(self):
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderItem(0, QTableWidgetItem("Quantità"))
        self.table_widget.setHorizontalHeaderItem(1, QTableWidgetItem("Marca"))
        self.table_widget.setHorizontalHeaderItem(2, QTableWidgetItem("Nome Prodotto"))
        self.table_widget.setHorizontalHeaderItem(3, QTableWidgetItem("Prezzo"))
        print(self.controller.get_lista_carrello())

        row = 0
        for prodotto in self.controller.get_lista_carrello():
            self.table_widget.insertRow(row)
            self.table_widget.setItem(row, 0, QTableWidgetItem(prodotto.quantita_carrello))
            row = row + 1

    def closeEvent(self, event):
        self.controller.save_data()







