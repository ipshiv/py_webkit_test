#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import sys
from shutil import copy
# import PySide
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWebEngine import *
from PySide2.QtWebEngineWidgets import *
from PySide2.QtWebChannel import *
from config import GLOBAL_STATIC_FOLDER, GLOBAL_UPLOAD_FOLDER
from processing.DataHandler import LocalDataHandler

dataHandler = LocalDataHandler(GLOBAL_UPLOAD_FOLDER)

def getFilesHTML(path):
    files = dataHandler.listAllFiles(path)
    return_tag = "<ul><li>"
    return_tag += "</li><li>".join(files)
    return_tag += "</li></ul>"
    return return_tag


def copy_file(full_path):
    copy(full_path, GLOBAL_UPLOAD_FOLDER)
    return get_all_files(GLOBAL_UPLOAD_FOLDER)



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        '''  Create webbrowser frame '''
        self.browser = QWebEngineView(self)
        self.setCentralWidget(self.browser)  # centralize
        self.browser.load(QUrl.fromLocalFile(GLOBAL_STATIC_FOLDER + "index.html"))  # open .html located in static)

        '''  Create webchannel to communicate between pyqt and js '''
        self.web = WebClass(self)  # must be instance of QObject!
        self.channel = QWebChannel(self)
        self.channel.registerObject("server", self.web)  # register object. check the static/qtconnector.js file
        self.browser.page().setWebChannel(self.channel)  # set channel to page

        self.mainToolBar = QToolBar(self)
        self.addToolBar(self.mainToolBar)
        showBtn = QPushButton("Показать файлы", self)
        self.mainToolBar.addWidget(showBtn)
        showBtn.clicked.connect(lambda: self.web.value_changed.emit(getFilesHTML(GLOBAL_UPLOAD_FOLDER)))

        uploadBtn = QPushButton("Загрузить файлы", self)
        self.mainToolBar.addWidget(uploadBtn)
        uploadBtn.clicked.connect(lambda: self.web.file_open())


class WebClass(QObject):
    value_changed = Signal(str)
    new_list = Signal(str)

    def file_open(self):
        name = QFileDialog.getOpenFileName()
        result = dataHandler.uploadFile(name[0])
        if result:
            self.value_changed.emit(getFilesHTML(GLOBAL_UPLOAD_FOLDER))
            # print ("OK!")
        else:
            print ("Error: %s" % name[0])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("File uploader")
    available_geometry = app.desktop().availableGeometry(window)
    window.resize(available_geometry.width() * 2 / 3, available_geometry.height() * 2 / 3)
    window.show()
    sys.exit(app.exec_())
