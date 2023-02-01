"""
using qt designer to load ui
"""
import subprocess
import sys
import webbrowser

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
        self.ui = uic.loadUi("./ResourseUI.ui")
        web_btn = self.ui.pushButton
        web_btn.clicked.connect(self.open_web)
        home_btn = self.ui.pushButton_2
        home_btn.clicked.connect(self.open_home)

    def open_web(self, arg):
        """
        slot function, open webpage of source code
        """
        webbrowser.open("https://github.com/fenyuchenabc/CS361Project")

    def open_home(self, arg):
        """
        slot function, open home page and close current one
        """
        subprocess.Popen(['/Users/yuchenfeng/opt/anaconda3/envs/pyqt5/bin/python',
                          '/Users/yuchenfeng/Desktop/OSU/CS361/pyqt/first_python.py'])
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # make a new window using MyWindow class
    w = MyWindow()
    w.ui.show()
    app.exec()