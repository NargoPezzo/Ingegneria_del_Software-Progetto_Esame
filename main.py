import sys
from PyQt5.QtWidgets import QApplication

from carrello.model.Carrello import Carrello
from carrello.views.VistaListaCarrello import VistaListaCarrello
from listaprodotti.model.ListaProdotti import ListaProdotti
from login.views.VistaLogin import VistaLogin
from prodotto.views.VistaAggiungiQuantita import VistaAggiungiQuantita

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = VistaLogin()
    main.show()
#    print(VistaListaCarrello().totale_prodotti)
#    print(ListaProdotti().lista_prodotti) #prova
#    print(Carrello().carrello)
    sys.exit(app.exec())

