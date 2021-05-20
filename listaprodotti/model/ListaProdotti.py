import os
import pickle


class ListaProdotti():
    def __init__(self):
        super(ListaProdotti, self).__init__()
        self.lista_prodotti = []
        if os.path.isfile('listaprodotti/data/lista_prodotti_salvata.pickle'):
            with open('listaprodotti/data/lista_prodotti_salvata.pickle', 'rb') as f:
                self.lista_prodotti = pickle.load(f)

    def aggiungi_prodotto(self, prodotto):
        self.lista_prodotti.append(prodotto)

    def rimuovi_prodotto_by_id(self, id):
        def is_selected_prodotto(prodotto):
            if prodotto.id == id:
                return True
            return False
        self.lista_prodotti.remove(list(filter(is_selected_prodotto, self.lista_prodotti))[0])

    def get_prodotto_by_index(self, index):
        return self.lista_prodotti[index]

    def get_lista_prodotti(self):
        return self.lista_prodotti

    def save_data(self):
        with open('listaprodotti/data/lista_prodotti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_prodotti, handle, pickle.HIGHEST_PROTOCOL)