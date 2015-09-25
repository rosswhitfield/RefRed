from PyQt4 import QtGui
import os
from RefRed.configuration.export_xml_config import ExportXMLConfig
from RefRed.utilities import makeSureFileHasExtension


class SavingConfiguration(object):
    
    parent = None
    
    def __init__(self, parent=None, filename=''):
        self.parent = parent
        self.filename = filename
        
    def run(self):
        if self.filename == '':
            _path = self.parent.path_config
            self.filename = str(QtGui.QFileDialog.getSaveFileName(self.parent,
                                                         'Save Configuration File',
                                                         _path))
            
            if self.filename == '':
                return

            self.parent.path_config = os.path.dirname(self.filename)
            self.filename = makeSureFileHasExtension(self.filename)
            o_export = ExportXMLConfig(parent = self.parent,
                                       filename = self.filename)
            
            
        
            
