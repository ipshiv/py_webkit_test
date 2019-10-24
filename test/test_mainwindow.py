#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import unittest

from PySide2.QtTest import QTest
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWebEngine import *
from PySide2.QtWebEngineWidgets import *
from PySide2.QtWebChannel import *

# from app.config import GLOBAL_STATIC_FOLDER, GLOBAL_UPLOAD_FOLDER

import app

class TestGuiHandler(unittest.TestCase):

    def setUp(self):
        self.app = QApplication([])
        self.web = app.app.MainWindow()

    def tearDown(self):
        pass

    def test_url(self):
        test_url = QUrl.fromLocalFile(app.config.GLOBAL_STATIC_FOLDER + "index.html")
        self.assertEqual(self.web.browser.url(), test_url)


if __name__ == '__main__':
    unittest.main()
