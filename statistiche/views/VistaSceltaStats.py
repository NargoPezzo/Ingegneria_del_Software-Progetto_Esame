import datetime

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from PyQt5 import QtGui

from statistiche.views.VistaStats import VistaStats


class VistaSceltaStats(QWidget):
    def __init__(self):
        super(VistaSceltaStats, self).__init__()

        self.today = datetime.date.today()
        self.week = datetime.date.today() - datetime.timedelta(weeks = 1)
        self.month = datetime.date.today() - datetime.timedelta(days = 30)
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_generic_button("Vendite Giornaliere", self.go_daily_stats), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Vendite Settimanali", self.go_weekly_stats), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Vendite Mensili", self.go_monthly_stats), 1, 2)

        self.setLayout(grid_layout)
        self.setFixedSize(400, 200)
        self.setWindowTitle("Statistiche")
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_daily_stats(self):
        self.vista_statistiche = VistaStats(self.today)
        self.vista_statistiche.show()

    def go_weekly_stats(self):
        self.vista_statistiche = VistaStats(self.week)
        self.vista_statistiche.show()

    def go_monthly_stats(self):
        self.vista_statistiche = VistaStats(self.month)
        self.vista_statistiche.show()