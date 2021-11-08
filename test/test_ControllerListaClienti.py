import os
import pickle
from unittest import TestCase

from cliente.model.Cliente import Cliente
from listaclienti.controller.ControlloreListaClienti import ControlloreListaClienti


class TestControllerListaClienti(TestCase):

    def test_aggiungi_cliente(self):
        self.controller = ControlloreListaClienti()
        self.cliente = Cliente("mariorossi", "Mario", "Rossi", "RSSMRA66A02A271R", "via Roma 14", "mariorossi@outlook.it", "3458256745" , "45")
        self.controller.aggiungi_cliente(self.cliente)

    def test_rimuovi_cliente_by_index(self):
        self.test_aggiungi_cliente()
        if os.path.isfile('data/lista_clienti.pickle'):
            with open('data/lista_clienti.pickle', 'rb') as f:
                self.lista_clienti = pickle.load(f)
                a = self.lista_clienti.index(self.cliente)
                self.assertFalse(self.controller.rimuovi_cliente_by_index(10000))
                self.assertTrue(self.controller.rimuovi_cliente_by_index(a))

    def test_get_lista_clienti(self):
        self.test_aggiungi_cliente()
        self.assertNotEqual(self.controller.get_lista_clienti(), [])
