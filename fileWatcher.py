#Revisar los archivos en la carpeta (fileWatcher) 
#           ->resive la ruta a revisar
#           ->vector de archivos ordenadaos por fecha de modificacion 
#           ->Manda los archivos con extencion diferente de *.xls a la carpeta N/A
#           ->retorna el ultimo archivo modificado 

import glob
import os
import shutil

class FileWatcher:
    
    def __init__(self, folderPath):
        self.folderPath = folderPath

    def naFiles(self, naFilesPath):
        self.allFiles = glob.glob( self.folderPath + os.path.sep + '*.*')
        self.naFiles = self.allFiles
        self.excelFiles = glob.glob( self.folderPath + os.path.sep + '*.xls')

        for i in self.excelFiles:
            self.naFiles.remove(i)

        for i in self.naFiles:
            shutil.move(i, naFilesPath, copy_function = shutil.copy)

    def lastModifyFile(self):
        self.excelFiles.sort(key=os.path.getmtime)
        return self.excelFiles[-1]