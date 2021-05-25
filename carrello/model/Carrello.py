import os
import pickle


class Carrello():
    def __init__(self):
        super(Carrello, self).__init__()
        self.carrello = []
        if os.path.isfile('carrello/data/carrello_salvato.pickle'):
            with open('carrello/data/carrello_salvato.pickle', 'rb') as f:
                self.carrello= pickle.load(f)

    def aggiungi_al_carrello(self, prodotto):
        self.carrello.append(prodotto)

    def rimuovi_prodotto_by_id(self, id):
        def is_selected_prodotto(prodotto):
            if prodotto.id == id:
                return True
            return False
        self.carrello.remove(list(filter(is_selected_prodotto, self.carrello))[0])

    def get_prodotto_by_index(self, index):
        return self.carrello[index]

    def get_lista_prodotti(self):
        return self.carrello

    def save_data(self):
        with open('carrello/data/carrello_salvato.pickle', 'wb') as handle:
            pickle.dump(self.carrello, handle, pickle.HIGHEST_PROTOCOL)
