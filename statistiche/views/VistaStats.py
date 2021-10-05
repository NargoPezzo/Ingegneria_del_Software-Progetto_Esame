from PyQt5.QtChart import QChartView, QPieSeries, QChart
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5 import QtGui
from statistiche.controller.ControlloreStats import ControlloreStats


class VistaStats(QWidget):
    def __init__(self):
        super(VistaStats, self).__init__()

        self.nomi_prodotto = []
        self.data = []

        self.setFixedSize(700, 300)
        self.chartview = QChartView

        self.controllerstats = ControlloreStats()
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))

        self.v_layout = QVBoxLayout()
        self.update_ui()


        self.v_layout.addWidget(self.chartview)



        self.setLayout(self.v_layout)
        self.resize(600, 300)
        self.setWindowTitle("Statistiche sulle vendite")


    def update_ui(self):
        series = QPieSeries()
        for prodotto in self.controllerstats.get_lista_delle_stats():
            series.append(prodotto.id, prodotto.quantita_carrello)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Vendite totali")

        self.chartview = QChartView(chart)



