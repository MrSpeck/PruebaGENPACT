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
import os

# crear directorios
current_directory = os.getcwd()
master_directory = os.path.join(current_directory, r'/Master')
na_directory = os.path.join(current_directory, r'/Not Applicable')
processed_directory = os.path.join(current_directory, r'/Processed')
if not os.path.exists(master_directory):
    os.makedirs(master_directory)
if not os.path.exists(na_directory):
    os.makedirs(na_directory)
if not os.path.exists(processed_directory):
    os.makedirs(processed_directory)

#crear Master File
masterPath = master_directory + r'/MasterFile.xls'

def loop():
    res = input("Do you want to change the folder to watch? (y/n)")
    
    if res == 'y':
        watcherPath = input("Enter the directory to check: ")


    
