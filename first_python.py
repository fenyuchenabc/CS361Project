import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    # set my window title
    w.setWindowTitle("first pyqt program")
    # add a push button
    btn = QPushButton("This is a button")
    # set w as the parent of the button
    btn.setParent(w)
    # show the window
    w.show()
    # program exec and get into a continuous loop
    app.exec()