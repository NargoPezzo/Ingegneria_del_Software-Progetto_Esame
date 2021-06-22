from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton
from PyQt5 import QtGui

from statistiche.controller.ControlloreStatistiche import ControlloreStatistiche


class VistaStatistiche(QWidget):
    def __init__(self, parent=None):
        super(VistaStatistiche, self).__init__(parent)
    #    self.prodotto = prodotto
    #    self.controller = ControlloreStatistiche()

        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))
        self.controller = ControlloreStatistiche()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
    #    self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
    #    open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton("Nuovo")
    #    new_button.clicked.connect(self.show_new_cliente)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle("Statistiche")

    '''def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for cliente in self.controller.get_lista_dei_clienti():
            item = QStandardItem()
            item.setText(cliente.nome + " " + cliente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
    '''