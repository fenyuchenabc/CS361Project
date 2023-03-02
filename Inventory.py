"""
using qt designer to load ui
"""
import subprocess
import sys

import numpy as np
import pandas as pd

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
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
        self.ui = uic.loadUi("./Inventory.ui")
        home_btn = self.ui.pushButton
        home_btn.clicked.connect(self.open_home)
        # read all data in csv and display in tableWidget
        table = self.ui.tableWidget
        table.clear()
        input_table = pd.read_csv('inventory.csv')
        input_table_rows = input_table.shape[0]
        input_table_columns = input_table.shape[1]
        input_table_header = input_table.columns.values.tolist()
        # read the table and set header
        table.setColumnCount(input_table_columns)
        table.setRowCount(input_table_rows)
        table.setHorizontalHeaderLabels(input_table_header)
        # iterate the csv and add to table
        for i in range(input_table_rows):
            input_table_rows_values = input_table.iloc[[i]]
            input_table_rows_values_array = np.array(input_table_rows_values)
            input_table_rows_values_list = input_table_rows_values_array.tolist()[0]
            for j in range(input_table_columns):
                input_table_items_list = input_table_rows_values_list[j]
                input_table_items = str(input_table_items_list)
                newItem = QTableWidgetItem(input_table_items)
                table.setItem(i, j, newItem)

    def open_home(self, arg):
        """
        slot function, open home interface and close current one
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