import datetime


class Prodotto:
    def __init__(self, id, marca, nome, categoria, prezzo, quantita_magazzino, quantita_carrello, data_acquisto= datetime.date.today()):
        super(Prodotto, self).__init__()
        self.id = id
        self.marca = marca
        self.nome = nome
        self.categoria = categoria
        self.prezzo = prezzo
        self.quantita_magazzino = quantita_magazzino
        self.quantita_carrello = quantita_carrello
        self.data_acquisto = data_acquisto




