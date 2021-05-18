import sys
from PyQt5.QtWidgets import QApplication

from home.views.VistaHome import VistaHome
from login.views.VistaLogin import VistaLogin

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vista_login = VistaLogin()
    vista_login.show()
    vista_home = VistaHome()
    vista_home.show()

    sys.exit(app.exec())
