import datetime


class Prodotto:
    def __init__(self, id, marca, nome, categoria, prezzo, quantita, data_acquisto= datetime.date.today()):
        super(Prodotto, self).__init__()
        self.id = id
        self.marca = marca
        self.nome = nome
        self.categoria = categoria
        self.prezzo = prezzo
        self.quantita = quantita
        self.data_acquisto = data_acquisto