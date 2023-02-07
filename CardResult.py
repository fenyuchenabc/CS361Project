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
        self.ui = uic.loadUi("./CardResultUI.ui")
        confirm_btn = self.ui.pushButton
        confirm_btn.clicked.connect(self.close_self)
        get_another_btn = self.ui.pushButton_2
        get_another_btn.clicked.connect(self.get_another)

    def close_self(self, arg):
        """
        slot function, close this interface
        """
        sys.exit()

    def get_another(self, arg):
        """
        slot function, reopen this program and closing current one.
        """
        subprocess.Popen(['/Users/yuchenfeng/opt/anaconda3/envs/pyqt5/bin/python',
                          '/Users/yuchenfeng/Desktop/OSU/CS361/pyqt/CardResult.py'])
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # make a new window using MyWindow class
    w = MyWindow()
    w.ui.show()
    app.exec()