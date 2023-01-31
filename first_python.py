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
        self.ui = uic.loadUi("./HomeScreen.ui")
        inventory_btn = self.ui.pushButton
        profile_btn = self.ui.pushButton_2
        get_cards_btn = self.ui.pushButton_4
        resources_btn = self.ui.pushButton_3
        help_btn = self.ui.pushButton_5


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # make a new window using MyWindow class
    w = MyWindow()
    w.ui.show()
    app.exec()
