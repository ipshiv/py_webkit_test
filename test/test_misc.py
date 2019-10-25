#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os
import unittest

from app.app import getFilesHTML
from app.config import GLOBAL_STATIC_FOLDER, GLOBAL_UPLOAD_FOLDER


class TestGetFilesHandler(unittest.TestCase):

    def test_from_upload(self):
        test_result = "<ul><li>test.txt</li></ul>"
        path = GLOBAL_UPLOAD_FOLDER
        result = getFilesHTML(path)
        self.assertEqual(test_result, result)


if __name__ == '__main__':
    unittest.main()
