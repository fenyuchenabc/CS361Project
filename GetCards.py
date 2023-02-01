"""
using qt designer to load ui
"""
import subprocess
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
        self.ui = uic.loadUi("./GetCards.ui")
        home_btn = self.ui.pushButton
        home_btn.clicked.connect(self.open_home)
        card_result_btn = self.ui.pushButton_2
        card_result_btn.clicked.connect(self.open_card_result)


    def open_home(self, arg):
        """
        slot function, open home interface and close current one
        """
        subprocess.Popen(['/Users/yuchenfeng/opt/anaconda3/envs/pyqt5/bin/python',
                          '/Users/yuchenfeng/Desktop/OSU/CS361/pyqt/first_python.py'])
        sys.exit()

    def open_card_result(self, arg):
        """
        slot function, open card results interface
        """
        subprocess.Popen(['/Users/yuchenfeng/opt/anaconda3/envs/pyqt5/bin/python',
                          '/Users/yuchenfeng/Desktop/OSU/CS361/pyqt/CardResult.py'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # make a new window using MyWindow class
    w = MyWindow()
    w.ui.show()
    app.exec()