import os
import pickle




class Statistiche():
    def __init__(self):
        super(Statistiche, self).__init__()

        self.statistiche = []

        if os.path.isfile('statistiche/data/statistiche_salvate.pickle'):
            with open('statistiche/data/statistiche_salvato.pickle', 'rb') as f:
                self.statistiche= pickle.load(f)

    def get_statistiche_by_index(self, index):
        return self.statistiche[index]

    def get_lista_statistiche(self):
        return self.statistiche

    def save_data(self):
        with open('carrello/data/carrello_salvato.pickle', 'wb') as handle:
            pickle.dump(self.statistiche, handle, pickle.HIGHEST_PROTOCOL)