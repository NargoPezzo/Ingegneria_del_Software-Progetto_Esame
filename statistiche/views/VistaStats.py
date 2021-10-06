import datetime

from PyQt5.QtChart import QChartView, QPieSeries, QChart
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidgetItem, QTableWidget, QListView, QHeaderView
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QPen, QStandardItemModel, QStandardItem

from statistiche.controller.ControlloreStats import ControlloreStats


class VistaStats(QWidget):
    def __init__(self, datascelta):
        super(VistaStats, self).__init__()
        self.datascelta = datascelta
        self.nomi_prodotto = []
        self.data = []

        self.chartview = QChartView()
        self.chartview.setRenderHint(QPainter.Antialiasing)

        self.controllerstats = ControlloreStats()
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))

        self.v_layout = QVBoxLayout()

        self.table_widget = QTableWidget()
        self.table_total = QListView()

        self.create_pie(datascelta)
        self.create_table(datascelta)
        self.table_total.setMaximumHeight(self.table_total.sizeHintForRow(0))
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.v_layout.addWidget(self.chartview)
        self.v_layout.addWidget(self.table_widget)
        self.v_layout.addWidget(self.table_total)



        self.setLayout(self.v_layout)
        self.resize(600, 900)
        self.setWindowTitle(self.setTitle(datascelta))

    def build_arrays(self, datascelta):
        for prodotto in self.controllerstats.get_lista_delle_stats():
            if prodotto.data_acquisto >= datascelta:
                j = 0
                for i in range(len(self.nomi_prodotto)):
                    if self.nomi_prodotto[i] == prodotto.categoria:
                        self.data[i] += prodotto.quantita_carrello
                        j = 1
                if j == 0:
                    self.nomi_prodotto.append(prodotto.categoria)
                    self.data.append(prodotto.quantita_carrello)



    def create_pie(self, data):
        series = QPieSeries()

        self.build_arrays(data)

        for i in range(len(self.nomi_prodotto)):
            series.append(self.nomi_prodotto[i], self.data[i])

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(self.setTitle(data))

        self.chartview = QChartView(chart)


    def setTitle(self, datascelta):

        if datascelta == datetime.date.today():
            return "Vendite Giornaliere"

        if datascelta == datetime.date.today() - datetime.timedelta(weeks = 1):
            return "Vendite Settimanali"

        return "Vendite Mensili"

    def create_table(self, datascelta):

        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderItem(0, QTableWidgetItem("Quantità"))
        self.table_widget.setHorizontalHeaderItem(1, QTableWidgetItem("Marca"))
        self.table_widget.setHorizontalHeaderItem(2, QTableWidgetItem("Nome Prodotto"))
        self.table_widget.setHorizontalHeaderItem(3, QTableWidgetItem("Categoria"))

        prezzofinalecarrello = 0
        row = 0
        for prodotto in self.controllerstats.get_lista_delle_stats():
            self.table_widget.insertRow(row)
            self.table_widget.setItem(row, 0, QTableWidgetItem(str(prodotto.quantita_carrello)))
            self.table_widget.setItem(row, 1, QTableWidgetItem(prodotto.marca))
            self.table_widget.setItem(row, 2, QTableWidgetItem(prodotto.nome))
            self.table_widget.setItem(row, 3, QTableWidgetItem(prodotto.categoria))

            acquistototale = int(prodotto.quantita_carrello) * int(prodotto.prezzo)
            row = row + 1
            prezzofinalecarrello += int(acquistototale)

        self.table_total_model = QStandardItemModel(self.table_total)
        item = QStandardItem()
        item.setText("Totale: " + str(prezzofinalecarrello) + "€")
        item.setEditable(False)
        font = item.font()
        font.setPointSize(14)
        item.setFont(font)
        self.table_total_model.appendRow(item)
        self.table_total.setModel(self.table_total_model)




