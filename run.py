#!/usr/bin/python3

import sys
from starterController import StarterController
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QHBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from starterController import StarterController

class ServiceStarter(QWidget):

    def __init__(self):
        super().__init__()
        self.controller = StarterController()
        self.services = None
        self.selectedService = None

        self.initUI()


    def initUI(self):
        self.centerWindow()
        self.resize(640, 480)
        self.setWindowTitle('Menedżer usług')
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

        self.refreshTable()

        self.table.clicked.connect(self.on_click)

        hbox = QHBoxLayout()

        refreshBtn = QPushButton(QIcon('assets/refresh.png'), 'Odśwież', self)
        refreshBtn.resize(refreshBtn.sizeHint())
        refreshBtn.move(25, 250)
        refreshBtn.clicked.connect(self.btnRefreshClicked)
        hbox.addWidget(refreshBtn)

        restart = QPushButton(QIcon('assets/restart.png'), 'Restart', self)
        restart.resize(restart.sizeHint())
        restart.move(25, 250)
        restart.clicked.connect(self.btnRestartClicked)
        hbox.addWidget(restart)

        startBtn = QPushButton(QIcon('assets/play.png'), 'Start', self)
        startBtn.resize(startBtn.sizeHint())
        startBtn.move(25, 250)
        startBtn.clicked.connect(self.btnStartClicked)
        hbox.addWidget(startBtn)

        stopBtn = QPushButton(QIcon('assets/stop.png'), 'Stop', self)
        stopBtn.resize(stopBtn.sizeHint())
        stopBtn.move(25, 250)
        stopBtn.clicked.connect(self.btnStopClicked)
        hbox.addWidget(stopBtn)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.table)
        vbox.addWidget(QLabel("Designed by HTRI 2020. MIT License"))

        self.setLayout(vbox)

    
    def refreshTable(self):
        self.services = self.controller.getServices()
        i = 0
        for service in self.services: 
            self.table.setItem(i,0, QTableWidgetItem(service.getServiceName()))
            self.table.setItem(i,1, QTableWidgetItem(service.getServiceStatus()))
            self.table.setItem(i,2, QTableWidgetItem(service.getEnabled()))
            i = i + 1


    @pyqtSlot()
    def on_click(self):
        self.selectedService = self.services[self.table.selectedItems()[0].row()]


    def btnStartClicked(self):
        if self.selectedService != None:
            self.selectedService.runService()
            self.refreshTable()

    
    def btnStopClicked(self):
        if self.selectedService != None:
            self.selectedService.killService()
            self.refreshTable()


    def btnRestartClicked(self):
        if self.selectedService != None:
            self.selectedService.restartService()
            self.refreshTable()


    def btnRefreshClicked(self):
        self.refreshTable()


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