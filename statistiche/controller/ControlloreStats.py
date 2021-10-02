from statistiche.model.Stats import Stats


class ControlloreStats():
    def __init__(self):
        super(ControlloreStats, self).__init__()
        self.model = Stats()

    def save_data(self):
        self.model.save_data()

    def aggiungi_stat(self, acquisto):
        self.model.aggiungi_stat(acquisto)

    def get_lista_dei_prodotti(self):
        return self.model.get_lista_prodotti()