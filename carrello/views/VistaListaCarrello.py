from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, \
    QWidgetItem, QHeaderView, QMessageBox
from PyQt5 import QtGui, QtCore
from carrello.controller.ControlloreCarrello import ControlloreCarrello
from carrello.views.VistaAcquistoCarrello import VistaAcquistoCarrello
import datetime

from statistiche.controller.ControlloreStats import ControlloreStats


class VistaListaCarrello(QWidget):
    def __init__(self,  parent=None):
        super(VistaListaCarrello, self).__init__(parent)

        self.setFixedSize(702, 300)

        self.controller = ControlloreCarrello()
        self.controllerstats = ControlloreStats()
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))

        self.main_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.table_widget = QTableWidget()
        self.table_total = QListView()
        self.update_ui()


        self.table_total.setMaximumHeight(self.table_total.sizeHintForRow(0))

        self.v_layout.addWidget(self.table_widget)
        self.v_layout.addWidget(self.table_total)
        self.main_layout.addLayout(self.v_layout)


        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton("Checkout")
        new_button.setStyleSheet("background-color: lightgreen")
        new_button.clicked.connect(self.aggiungi_alle_statistiche)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        self.main_layout.addLayout(buttons_layout)
        self.main_layout.addWidget(new_button)

        self.setLayout(self.main_layout)
        self.setWindowTitle("Carrello")

    def show_selected_info(self):
        try:
            selected = self.table_widget.selectedIndexes()[0].row()
            acquisto_selezionato = self.controller.get_acquisto_by_index(selected)
            self.vista_prodotto = VistaAcquistoCarrello(acquisto_selezionato, self.controller.elimina_acquisto_by_id, self.update_ui)
            self.vista_prodotto.show()
        except IndexError:
            QMessageBox.critical(self, 'Errore', 'Per favore, seleziona un prodotto', QMessageBox.Ok, QMessageBox.Ok)

    def aggiungi_alle_statistiche(self):
        msg = QMessageBox()

        if self.controller.get_lista_carrello():

            reply = QMessageBox.question(self, "Conferma", "Vuoi confermare l'acquisto?",
                                     QMessageBox.Yes, QMessageBox.No)

            if reply == QMessageBox.Yes:
                for prodotto in self.controller.get_lista_carrello():
                    prodotto.data_acquisto = datetime.date.today()
                    self.controllerstats.aggiungi_stat(prodotto)
                self.controller.clearall()
                self.controller.save_data()
                self.controllerstats.save_data()
                msg.setText('Acquisto confermato  :D')
                msg.exec_()
                self.close()
            else:
                return
        else:
            QMessageBox.critical(self, 'Errore', 'Il carrello non contiene alcun prodotto', QMessageBox.Ok, QMessageBox.Ok)

    def update_ui(self):
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(5)
        self.create_table(0, "Quantità")
        self.create_table(1, "Marca")
        self.create_table(2, "Nome Prodotto")
        self.create_table(3, "Categoria")
        self.create_table(4, "Prezzo")

        prezzofinalecarrello = 0
        row = 0
        for prodotto in self.controller.get_lista_carrello():
            self.table_widget.insertRow(row)
            self.inserisci_elemento_in_tabella(prodotto.quantita_carrello, row, 0)
            self.inserisci_elemento_in_tabella(prodotto.marca, row, 1)
            self.inserisci_elemento_in_tabella(prodotto.nome, row, 2)
            self.inserisci_elemento_in_tabella(prodotto.categoria, row, 3)

            acquistototale = float(prodotto.quantita_carrello) * float(prodotto.prezzo)
            prezzofinalecarrello += float(acquistototale)
            acquistototale = str(acquistototale) + "€"
            self.inserisci_elemento_in_tabella(acquistototale, row, 4)
            row = row + 1


        self.table_total_model = QStandardItemModel(self.table_total)
        item = QStandardItem()
        item.setText("Totale: " + str(prezzofinalecarrello) + "€")
        item.setEditable(False)
        font = item.font()
        font.setPointSize(14)
        font.setBold(True)
        item.setFont(font)
        self.table_total_model.appendRow(item)
        self.table_total.setModel(self.table_total_model)


    def create_table(self, index, label):

        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        item.setFont(font)
        item.setText(label)
        self.table_widget.setHorizontalHeaderItem(index, item)
        self.table_widget.setColumnWidth(index, 100)

    def closeEvent(self, event):
        self.controller.save_data()

    def inserisci_elemento_in_tabella(self, elemento, row, index):
        item = QTableWidgetItem()
        item.setText(str(elemento))
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.table_widget.setItem(row, index, item)







