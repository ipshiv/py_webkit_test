#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os
import unittest

from app.app import get_all_files


class TestGetFilesHandler(unittest.TestCase):

    def test_from_upload(self):
        test_result = "<ul><li>test.txt</li></ul>"
        path = os.getcwd() + "/app/upload/"
        result = get_all_files(path)
        self.assertEqual(test_result, result)
