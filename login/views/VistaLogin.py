
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QMessageBox, QPushButton, QApplication

from home.views.VistaHome import VistaHome


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
        self.dialog = VistaHome()

    def check_password(self):
        msg = QMessageBox()



        if self.lineEdit_username.text() == 'a' and self.lineEdit_password.text() == '000':
            msg.setText('Benvenuto')
            msg.exec_()
            self.dialog.show()
            self.close() #ciao


        else:
            msg.setText('ERRORE: Ricontrollare le credenziali')
            msg.exec_()
