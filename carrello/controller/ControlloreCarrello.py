from carrello.model.Carrello import Carrello


class ControlloreCarrello():
    def __init__(self):
        super(ControlloreCarrello, self).__init__()
        self.model = Carrello()

    def get_lista_carrello(self):
        return self.model.get_lista_carrello()

    def get_acquisto_by_index(self, index):
        return self.model.get_acquisto_by_index(index)

    def elimina_acquisto_by_id(self, id):
        self.model.rimuovi_acquisto_by_id(id)

    def save_data(self):
        self.model.save_data()

