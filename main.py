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
import openpyxl

# crear directorios
current_directory = os.getcwd()
master_directory = os.path.join(current_directory, r'Master')
na_directory = os.path.join(current_directory, r'Not Applicable')
processed_directory = os.path.join(current_directory, r'Processed')
watcherPath = os.path.join(current_directory, r'Monitor')
if not os.path.exists(master_directory):
    os.makedirs(master_directory)
if not os.path.exists(na_directory):
    os.makedirs(na_directory)
if not os.path.exists(processed_directory):
    os.makedirs(processed_directory)
if not os.path.exists(watcherPath):
    os.makedirs(watcherPath)

#crear Master File
masterPath = master_directory + r'\MasterFile.xlsx'
if not os.path.exists(masterPath):
    masterWB = openpyxl.Workbook()
    masterWB.save(masterPath)

while True:
    res = input("Do you want to change the folder to watch? (y/n)")
    
    if res == 'y':
        watcherPath = input("Enter the directory to check: ")
        
    #Revisar carpeta Monitor
    monitor = FileWatcher(watcherPath)
    monitor.naFiles(na_directory)
    lastFile = monitor.lastModifyFile()
    
    #Copiar a MasterFile
    if not lastFile:
        print("No files in directory")
    else:
        masterfile = XFile(lastFile, masterPath)
        masterfile.copySheets()
        masterfile.sendFile(processed_directory)


    
