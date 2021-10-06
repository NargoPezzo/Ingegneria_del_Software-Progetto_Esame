import datetime

from PyQt5.QtChart import QChartView, QPieSeries, QChart
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidgetItem, QTableWidget, QListView, QHeaderView
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QPen, QStandardItemModel, QStandardItem, QFont

from statistiche.controller.ControlloreStats import ControlloreStats


class VistaStats(QWidget):
    def __init__(self, datascelta):
        super(VistaStats, self).__init__()
        self.datascelta = datascelta

        self.categoria = []
        self.quantita_categoria = []
        self.prodotti = []

        self.chartview = QChartView()


        self.controllerstats = ControlloreStats()
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))

        self.v_layout = QVBoxLayout()

        self.table_widget = QTableWidget()
        self.table_total = QListView()

        self.create_pie(datascelta)
        self.populate_table(datascelta)
        self.table_total.setMaximumHeight(self.table_total.sizeHintForRow(0))
        self.table_widget.setMaximumHeight(200)

        self.v_layout.addWidget(self.chartview)
        self.v_layout.addWidget(self.table_widget)
        self.v_layout.addWidget(self.table_total)



        self.setLayout(self.v_layout)
        self.setFixedSize(625, 700)
        self.setWindowTitle(self.setTitle(datascelta))
        self.chartview.setRenderHint(QtGui.QPainter.Antialiasing)


    def build_pie(self, datascelta):
        for prodotto in self.controllerstats.get_lista_delle_stats():
            if prodotto.data_acquisto >= datascelta:
                j = 0
                for i in range(len(self.categoria)):
                    if self.categoria[i] == prodotto.categoria:
                        self.quantita_categoria[i] += prodotto.quantita_carrello
                        j = 1
                if j == 0:
                    self.categoria.append(prodotto.categoria)
                    self.quantita_categoria.append(prodotto.quantita_carrello)

    def build_table(self, datascelta):

        for prodotto in self.controllerstats.get_lista_delle_stats():
            if prodotto.data_acquisto >= datascelta:
                j = 0
                for product in self.prodotti:
                    if product.id == prodotto.id:
                        product.quantita_carrello += prodotto.quantita_carrello
                        j = 1
                if j == 0:
                    self.prodotti.append(prodotto)

    def create_pie(self, data):
        series = QPieSeries()


        self.build_pie(data)


        slice = series.append(self.categoria[0], self.quantita_categoria[0])
        slice.setBrush(QtGui.QColor("#FF5631"))
        slice = series.append(self.categoria[1], self.quantita_categoria[1])
        slice.setBrush(QtGui.QColor("#31B1FF"))
        slice = series.append(self.categoria[2], self.quantita_categoria[2])
        slice.setBrush(QtGui.QColor("#31FF4D"))
        slice = series.append(self.categoria[3], self.quantita_categoria[3])
        slice.setBrush(QtGui.QColor("#DA31FF"))
        slice = series.append(self.categoria[4], self.quantita_categoria[4])
        slice.setBrush(QtGui.QColor("#FFEC31"))


        chart = QChart()
        font = QFont()
        font.setPointSize(18)
        chart.addSeries(series)
        chart.setTitleFont(font)
        chart.setTitle(self.setTitle(data))

        self.chartview = QChartView(chart)

    def setTitle(self, datascelta):

        if datascelta == datetime.date.today():
            return "Vendite Giornaliere"

        if datascelta == datetime.date.today() - datetime.timedelta(weeks = 1):
            return "Vendite Settimanali"

        return "Vendite Mensili"

    def populate_table(self, datascelta):

        self.build_table(datascelta)

        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(4)
        self.create_table(0, "Quantità")
        self.create_table(1, "Marca")
        self.create_table(2, "Nome Prodotto")
        self.create_table(3, "Categoria")

        prezzofinalecarrello = 0
        row = 0
        for prodotto in self.prodotti:

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
        self.table_widget.setColumnWidth(index, 140)

