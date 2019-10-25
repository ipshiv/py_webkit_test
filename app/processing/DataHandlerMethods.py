#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import abc
import shutil

import os

class ListAllFilesBehaviourAbstract(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def listAllFiles(self, path):
        """Required Method"""

class UploadFileBehaviourAbstract(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def uploadFile(self, file, destination):
        """Required Method"""


class LocalListAllFilesBehaviour(ListAllFilesBehaviourAbstract):

    def listAllFiles(self, path):
        return os.listdir(path)


class LocalUploadFileBehaviour(UploadFileBehaviourAbstract):

    def uploadFile(self, file, destination):
        try:
            shutil.copy(file, destination)
        except:
            return 0
        else:
            return 1
