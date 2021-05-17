from res.ui import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QPlainTextEdit, QLabel
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Ui_Form()
    win.setFixedSize(750, 450)
    win.show()
    sys.exit(app.exec_())


