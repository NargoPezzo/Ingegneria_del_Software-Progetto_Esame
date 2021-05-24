import os
import pickle

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QMessageBox, QPushButton
from PyQt5 import QtCore

from home.views.VistaHome import VistaHome
from home.views.VistaHomeDirettore import VistaHomeDirettore
from listadipendenti.model.ListaDipendenti import ListaDipendenti


class VistaLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.resize(400, 120)

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Dipendente </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Inserire nome Dipendente')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Inserire password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)


        if os.path.isfile('listadipendenti/data/lista_prodotti_salvata.pickle'):
            pickle_file = open('listadipendenti/data/lista_dipendenti_salvata.pickle', 'rb')
            self.objects = []
            while True:
                try:
                    self.objects.append(pickle.load(pickle_file))
                except EOFError:
                    break
                pickle_file.close()

    def check_password(self):
        msg = QMessageBox()
        lista = ListaDipendenti()

        if lista.verifica_id_dipendente(self.lineEdit_username.text(), self.lineEdit_password.text()):
            self.dialog = VistaHome()
            msg.setText('Accesso alla pagina dei dipendenti')
            msg.exec_()
            self.dialog.show()
            self.close()

        elif self.lineEdit_username.text() == '' and self.lineEdit_password.text() == '':
            self.dialog = VistaHomeDirettore()
            msg.setText('Accesso alla pagina del direttore')
            msg.exec_()
            self.dialog.show()
            self.close()

        else:
            msg.setText('ERRORE: Ricontrollare le credenziali')
            msg.exec_()

    def keyPressEvent(self, qKeyEvent):

        if qKeyEvent.key() == QtCore.Qt.Key_Return:
            self.check_password()
        else:
            super().keyPressEvent(qKeyEvent)
