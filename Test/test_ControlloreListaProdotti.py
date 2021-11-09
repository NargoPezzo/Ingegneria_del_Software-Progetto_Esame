from unittest import TestCase

from listaprodotti.controller.ControlloreListaProdotti import ControlloreListaProdotti
from prodotto.model.Prodotto import Prodotto


class TestControlloreListaProdotti(TestCase):
    def test_aggiungi_prodotto(self):
        self.controller = ControlloreListaProdotti()
        self.prodotto = Prodotto("appleiphone", "Apple", "iPhone", "Telefonia", "699", "100", "01/01/2021")
        self.controller.aggiungi_prodotto(self.prodotto)

    def test_get_lista_dei_prodotti(self):
        self.test_aggiungi_prodotto()
        self.assertNotEqual(self.controller.get_lista_dei_prodotti(), [])

    def test_elimina_prodotto_by_id(self):
        self.fail()
