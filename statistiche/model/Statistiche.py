import os
import pickle




class Statistiche():
    def __init__(self):
        super(Statistiche, self).__init__()

        self.statistiche = []

        if os.path.isfile('statistiche/data/statistiche_salvate.pickle'):
            with open('statistiche/data/statistiche_salvato.pickle', 'rb') as f:
                self.statistiche= pickle.load(f)

    def aggiungi_alle_statistiche(self,prodotto, quantita):
        if self.verifica_presenza_prodotto_by_id(prodotto.id, quantita) is False:
            prodotto.set_quantita_carrello(quantita)
            self.statistiche.append(prodotto)

    def get_statistiche_by_index(self, index):
        return self.statistiche[index]

    def get_lista_statistiche(self):
        return self.statistiche

    def save_data(self):
        with open('carrello/data/carrello_salvato.pickle', 'wb') as handle:
            pickle.dump(self.statistiche, handle, pickle.HIGHEST_PROTOCOL)

    def get_lista_prodotti_statistiche(self):
        return self.statistiche

    def get_prodotto_by_index(self, index):
        return self.statistiche[index]

    def rimuovi_prodotto_by_id(self, id):
        def is_selected_prodotto(prodotto):
            if prodotto.id == id:
                return True
            return False
        self.statistiche.remove(list(filter(is_selected_prodotto, self.statistiche))[0])

    def verifica_presenza_prodotto_by_id(self, id,quantita):
        for(i,prodotto) in enumerate(self.statistiche):
            if prodotto.id == id:
                self.statistiche[i].set_quantita_carrello(quantita+self.statistiche[i].quantita_carrello)
                return True
        return False