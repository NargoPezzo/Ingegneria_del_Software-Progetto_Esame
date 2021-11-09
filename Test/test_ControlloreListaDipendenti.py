import os
import pickle
from unittest import TestCase

from dipendente.model.Dipendente import Dipendente
from listadipendenti.controller.ControlloreListaDipendenti import ControlloreListaDipendenti


class TestControlloreListaDipendenti(TestCase):
    def test_aggiungi_dipendente(self):
        self.controller = ControlloreListaDipendenti()
        self.dipendente = Dipendente("paolobianchi", "Paolo", "Bianchi", "BNCPLO66A02A271R", "via Roma 14",
                               "paolobianchi@outlook.it", "3458256745", "45", "Paolino45")
        self.controller.aggiungi_dipendente(self.dipendente)


    def test_get_lista_dei_dipendenti(self):
        self.test_aggiungi_dipendente()
        self.assertNotEqual(self.controller.get_lista_dei_dipendenti(), [])

    def test_elimina_dipendente_by_id(self):
        self.test_aggiungi_dipendente()
        if os.path.isfile('listadipendenti/data/lista_dipendenti_salvata.pickle'):
            with open('listadipendenti/data/lista_dipendenti_salvata.pickle', 'r') as f:
                self.lista_dipendenti = pickle.load(f)
                a = self.lista_dipendenti.id(self.dipendente)
                self.assertFalse(self.controller.elimina_dipendente_by_id(10000))
                self.assertTrue(self.controller.elimina_dipendente_by_id(a))
