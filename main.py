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

# crear el archivo Master

def loop():
    res = input("Do you want to change the folder to watch? (y/n)")
    
    if res == 'y':
        watcherPath = input("Enter the directory to check: ")


    
