"""
using qt designer to load ui
"""
import sys
import os
import subprocess

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
        # get all the buttons on the home screen
        inventory_btn = self.ui.pushButton
        profile_btn = self.ui.pushButton_2
        get_cards_btn = self.ui.pushButton_4
        resources_btn = self.ui.pushButton_3
        help_btn = self.ui.pushButton_5

        inventory_btn.clicked.connect(self.open_inventory)

    def open_inventory(self, arg):
        """
        slot function, open inventory interface and close current one
        """
        subprocess.Popen(['/Users/yuchenfeng/opt/anaconda3/envs/pyqt5/bin/python', '/Users/yuchenfeng/Desktop/OSU/CS361/pyqt/Profile.py'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # make a new window using MyWindow class
    w = MyWindow()
    w.ui.show()
    app.exec()
