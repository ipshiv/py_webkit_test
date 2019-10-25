#!/usr/bin/env python2
# -*- coding: utf-8 -*

from DataHandlerMethods import *

localFilesList = LocalListAllFilesBehaviour()
localUploadFile = LocalUploadFileBehaviour()

class DataHandler(object):

    """Base interface for file worker"""

    def __init__(self, upload_destination, listAllFiles_behaviour, uploadFile_behaviour):
        self._listAllFiles_behaviour = listAllFiles_behaviour
        self._uploadFile_behaviour = uploadFile_behaviour
        self.upload_destination = upload_destination

    def listAllFiles(self, path):
        return self._listAllFiles_behaviour.listAllFiles(path)

    def uploadFile(self, file):
        return self._uploadFile_behaviour.uploadFile(file, self.upload_destination)


class LocalDataHandler(DataHandler):

    def __init__(self, uploadFolder):
        super(LocalDataHandler, self).__init__(uploadFolder, localFilesList, localUploadFile)
