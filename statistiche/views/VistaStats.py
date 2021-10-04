import datetime

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTableWidget, QHeaderView, QListView
from PyQt5 import QtGui

from statistiche.controller.ControlloreStats import ControlloreStats
from matplotlib import pyplot as plt
import numpy as np


class VistaStats(QWidget):
    def __init__(self):
        super(VistaStats, self).__init__()

        self.nomi_prodotto = []
        self.data = []

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
        plt.show()


    def build_arrays(self, datascelta):

        for prodotto in self.controllerstats.get_lista_delle_stats():
            if prodotto.data_acquisto >= datascelta:
                j = 0
                for i in range(len(self.nomi_prodotto)):
                    if self.nomi_prodotto[i] == prodotto.id:
                        self.data[i] += prodotto.quantita_carrello
                        j = 1
                if j == 0:
                    self.nomi_prodotto.append(prodotto.id)
                    self.data.append(prodotto.quantita_carrello)
        print(self.nomi_prodotto)
        print(self.data)

    def update_ui(self):

        self.build_arrays(datetime.date.today())
        fig = plt.figure(figsize = (10,7))
        plt.pie(self.data, labels = self.nomi_prodotto)

