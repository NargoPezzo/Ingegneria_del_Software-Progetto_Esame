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
        if self.verifica_presenza_prodotto_by_id(prodotto) is False:
            self.carrello.append(prodotto)


    def rimuovi_prodotto_by_id(self, id):
        def is_selected_prodotto(prodotto):
            if prodotto.id == id:
                return True
            return False
        self.carrello.remove(list(filter(is_selected_prodotto, self.carrello))[0])

    def get_prodotto_by_index(self, index):
        return self.carrello[index]

    def get_lista_carrello(self):
        return self.carrello

    def save_data(self):
        with open('carrello/data/carrello_salvato.pickle', 'wb') as handle:
            pickle.dump(self.carrello, handle, pickle.HIGHEST_PROTOCOL)

    def verifica_quantita_prodotto(self, prodotto, quantita):

        if quantita <= int(prodotto.quantita_magazzino):
            prodotto.quantita_carrello = quantita
            prodotto.quantita_magazzino = int(prodotto.quantita_magazzino) - prodotto.quantita_carrello
            return True
        return False

    def verifica_presenza_prodotto_by_id(self, prodottoscelto):

        for(i, prodotto) in enumerate(self.carrello):
            if prodotto.id == prodottoscelto.id:
                self.carrello[i].quantita_carrello = prodottoscelto.quantita_carrello + self.carrello[i].quantita_carrello
                return True
        return False

    def ritorna_quantita_al_carrello(self,prodotto,quantita): # METODO PER FAR TORNARE PRODOTTI DAL CARRELLO DI NUOVO AL MAGAZZINO
        prodotto.quantita_carrello = quantita
        prodotto.quantita_magazzino = int(prodotto.quantita_magazzino) + int(prodotto.quantita_carrello)  #ci sono quaasi
