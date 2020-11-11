#!/usr/bin/python3

import sys
import starterController
from PyQt5.QtWidgets import QAction, QApplication, QDesktopWidget, QHBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class ServiceStarter(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.centerWindow()
        self.resize(640, 480)
        self.setWindowTitle('Odpalacz')
        self.setWindowIcon(QIcon('assets/switch.png'))
        self.createTable()

    def createTable(self):
        self.table = QTableWidget()
        self.table.setRowCount(2)
        self.table.setColumnCount(3)

        headers = ['Usługa', 'Status', 'Włączona']
        self.table.setHorizontalHeaderLabels(headers)
        self.table.setColumnWidth(0, 300)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 100)
 
        self.table.setItem(0,0, QTableWidgetItem("MySQL"))
        self.table.setItem(0,1, QTableWidgetItem("zatrzymany"))
        self.table.setItem(0,2, QTableWidgetItem("TAK"))

        self.table.setItem(1,0, QTableWidgetItem("Apache2"))
        self.table.setItem(1,1, QTableWidgetItem("zatrzymany"))
        self.table.setItem(1,2, QTableWidgetItem("NIE"))

        self.table.clicked.connect(self.on_click)

        hbox = QHBoxLayout()

        refreshBtn = QPushButton(QIcon('assets/refresh.png'), 'Odśwież', self)
        refreshBtn.resize(refreshBtn.sizeHint())
        refreshBtn.move(25, 250)
        refreshBtn.clicked.connect(QApplication.instance().quit)
        hbox.addWidget(refreshBtn)

        startBtn = QPushButton(QIcon('assets/play.png'), 'Start', self)
        startBtn.resize(startBtn.sizeHint())
        startBtn.move(25, 250)
        startBtn.clicked.connect(QApplication.instance().quit)
        hbox.addWidget(startBtn)

        stopBtn = QPushButton(QIcon('assets/stop.png'), 'Stop', self)
        stopBtn.resize(stopBtn.sizeHint())
        stopBtn.move(25, 250)
        stopBtn.clicked.connect(QApplication.instance().quit)
        hbox.addWidget(stopBtn)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.table)
        vbox.addWidget(QLabel("Designed by HTRI 2020. MIT License"))

        self.setLayout(vbox)

    
    @pyqtSlot()
    def on_click(self):
        print('\n')
        for current in self.table.selectedItems():
            print(current.row(), current.column(), current.text())


    def centerWindow(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



def main():
    app = QApplication(sys.argv)
    start = ServiceStarter()
    start.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()