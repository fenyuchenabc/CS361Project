"""
using qt designer to load ui
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = None
        self.init_ui()

    def init_ui(self):
        """
        get all the widgets from ui and bind signals and slots if needed
        """
        # load ui file
        self.ui = uic.loadUi("./CardResultUI.ui")
        confirm_btn = self.ui.pushButton
        confirm_btn.clicked.connect(self.close_self)

    def close_self(self, arg):
        """
        slot function, close this interface
        """
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # make a new window using MyWindow class
    w = MyWindow()
    w.ui.show()
    app.exec()