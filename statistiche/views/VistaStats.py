import datetime

from PyQt5.QtChart import QChartView, QPieSeries, QChart
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QPen

from statistiche.controller.ControlloreStats import ControlloreStats


class VistaStats(QWidget):
    def __init__(self, datascelta):
        super(VistaStats, self).__init__()
        self.datascelta = datascelta
        self.nomi_prodotto = []
        self.data = []

        self.chartview = QChartView()

        self.controllerstats = ControlloreStats()
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))

        self.v_layout = QVBoxLayout()

        self.update_ui(datascelta)


        self.v_layout.addWidget(self.chartview)



        self.setLayout(self.v_layout)
        self.resize(600, 300)
        self.setWindowTitle(self.setTitle(datascelta))

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



    def update_ui(self, data):
        series = QPieSeries()

        self.build_arrays(data)

        for i in range(len(self.nomi_prodotto)):
            series.append(self.nomi_prodotto[i], self.data[i])

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Vendite totali")

        self.chartview = QChartView(chart)

    def setTitle(self, datascelta):

        if datascelta =




