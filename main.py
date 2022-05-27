#Revisar los archivos en la carpeta (fileWatcher) 
#           ->resive la ruta a revisar
#           ->Manda los archivos con extencion diferente de *.xls a la carpeta N/A
#           ->retorna el ultimo archivo modificado 
#Abrir el archivo (xFile)
#           ->resives la ruta del archivo de fileWatcher
#           ->copias cada sheet a el master file
#           ->mandas el archivo a la carpeta Processed

from fileWatcher import FileWatcher
from xFile import XFile

def loop():
    masterPath = input("Enter master file path: ")

