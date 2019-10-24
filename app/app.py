#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import sys
# import PySide
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWebEngine import *
from PySide2.QtWebEngineWidgets import *
from PySide2.QtWebChannel import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        '''  Create webbrowser frame '''
        self.browser = QWebEngineView(self)
        self.setCentralWidget(self.browser)  # centralize
        self.browser.load(QUrl.fromLocalFile(os.getcwd() + "/static/index.html"))  # open .html located in static)

        '''  Create webchannel to communicate between pyqt and js '''
        self.web = WebClass(self)  # must be instance of QObject!
        self.channel = QWebChannel(self)
        self.channel.registerObject("server", self.web)  # register object. check the static/qtconnector.js file
        self.browser.page().setWebChannel(self.channel)  # set channel to page

        self.mainToolBar = QToolBar(self)
        self.addToolBar(self.mainToolBar)
        randBtn = QPushButton("Случайное число", self)
        self.mainToolBar.addWidget(randBtn)
        randBtn.clicked.connect(lambda: self.web.value_changed.emit(100))

        textBtn = QPushButton("Текст", self)
        self.mainToolBar.addWidget(textBtn)
        textBtn.clicked.connect(lambda: self.web.new_list.emit("<ul><li>one</li><li>second</li></ul>"))


class WebClass(QObject):
    value_changed = Signal(int)
    new_list = Signal(str)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("File uploader")
    window.web.new_list.emit("<ul><li>1</li><li>22</li></ul>")
    window.show()
    sys.exit(app.exec_())
