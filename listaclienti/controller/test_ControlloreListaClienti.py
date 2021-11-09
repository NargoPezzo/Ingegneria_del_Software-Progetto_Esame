import os
import pickle
from unittest import TestCase

from cliente.model.Cliente import Cliente
from listaclienti.controller.ControlloreListaClienti import ControlloreListaClienti


class TestControlloreListaClienti(TestCase):
    def test_aggiungi_cliente(self):
        self.controller = ControlloreListaClienti()
        self.cliente = Cliente("mariorossi", "Mario", "Rossi", "RSSMRA66A02A271R", "via Roma 14", "mariorossi@outlook.it", "3458256745", "45")
        self.controller.aggiungi_cliente(self.cliente)

    def test_get_lista_dei_clienti(self):
        self.test_aggiungi_cliente()
        self.assertNotEqual(self.controller.get_lista_dei_clienti(), [])

    def test_elimina_cliente_by_id(self):
        self.test_aggiungi_cliente()
        if os.path.isfile('listaclienti/data/lista_clienti_salvata.pickle'):
            with open('listaclienti/data/lista_clienti_salvata.pickle', 'rb') as f:
                self.lista_clienti = pickle.load(f)
                a = self.lista_clienti.id(self.cliente)
                b = "marcoverdi"
                self.assertFalse(self.controller.elimina_cliente_by_id(b))
                self.assertTrue(self.controller.elimina_cliente_by_id(a))
