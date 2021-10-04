from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTableWidget, QHeaderView, QListView
from PyQt5 import QtGui

from statistiche.controller.ControlloreStats import ControlloreStats
from matplotlib import pyplot as plt
import numpy as np


class VistaStats(QWidget):
    def __init__(self):
        super(VistaStats, self).__init__()

        self.setFixedSize(700, 300)

        self.controllerstats = ControlloreStats()
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))

        self.main_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()



        self.update_ui()




        self.main_layout.addLayout(self.v_layout)

        self.setLayout(self.main_layout)
        self.resize(600, 300)
        self.setWindowTitle("Statistiche sulle vendite")


    def update_ui(self):


        nomi_prodotto = []
        data = []
        for prodotto in self.controllerstats.get_lista_delle_stats():

            j = 0
            for i in range(len(nomi_prodotto)):
                if nomi_prodotto[i] == prodotto.id:
                    data[i] += prodotto.quantita_carrello
                    j = 1

            if j == 0:
                nomi_prodotto.append(prodotto.id)
                data.append(prodotto.quantita_carrello)


        print(nomi_prodotto)
        print(data)
