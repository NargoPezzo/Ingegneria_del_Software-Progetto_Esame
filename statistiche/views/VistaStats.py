from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTableWidget, QHeaderView
from PyQt5 import QtGui

from statistiche.controller.ControlloreStats import ControlloreStats


class VistaStats(QWidget):
    def __init__(self):
        super(VistaStats, self).__init__()

        self.setFixedSize(700, 300)

        self.controllerstats = ControlloreStats()
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))

        self.main_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.table_widget = QTableWidget()
        self.update_ui()

        self.table_total.setMaximumHeight(self.table_total.sizeHintForRow(0))
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.v_layout.addWidget(self.table_widget)
        self.v_layout.addWidget(self.table_total)
        self.main_layout.addLayout(self.v_layout)

        self.setLayout(self.main_layout)
        self.resize(600, 300)
        self.setWindowTitle("Carrello")