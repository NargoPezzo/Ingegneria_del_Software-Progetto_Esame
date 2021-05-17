class Prodotto:
    def __init__(self, id, marca, nome, categoria, prezzo):
        super(Prodotto, self).__init__()
        self.id = id
        self.marca = marca
        self.nome = nome
        self.categoria = categoria
        self.prezzo = prezzo