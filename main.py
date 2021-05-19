import sys
from PyQt5.QtWidgets import QApplication
from login.views.VistaLogin import VistaLogin



app = QApplication(sys.argv)
main = VistaLogin()
main.show()

sys.exit(app.exec())

if __name__ == '__main__':
    main()
