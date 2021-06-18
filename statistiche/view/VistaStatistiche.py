from PyQt5.QtWidgets import QWidget


class VistaStatistiche(QWidget):
    def __init__(self,prodotto, parent=None):
        super(VistaStatistiche, self).__init__(parent)
        self.prodotto = prodotto
        self.controller = ControlloreStatistiche()
