from carrello.model.Carrello import Carrello


class ControlloreCarrello():
    def __init__(self):
        super(ControlloreCarrello, self).__init__()
        self.model = Carrello()

    def aggiungi_al_carrello(self, prodotto):
        self.model.aggiungi_prodotto(prodotto)

    def get_lista_dei_prodotti(self):
        return self.model.get_lista_prodotti()

    def get_prodotto_by_index(self, index):
        return self.model.get_prodotto_by_index(index)

    def elimina_prodotto_by_id(self, id):
        self.model.rimuovi_prodotto_by_id(id)

    def save_data(self):
        self.model.save_data()
