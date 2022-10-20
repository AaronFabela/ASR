# Funciones auxiliares
from fileinput import filename
from getSNMP import consultaSNMP
import os


class File:

    # Valida si el archivo existe en el dispositivo
    def validarArchivo(self, archivo):
        if os.path.isfile(archivo) and os.stat(archivo).st_size > 0:
            return True
        else:
            print('\n\tNo se ha encontrado el archivo o esta vacio\n')
            return False

    # Valida si el archivo no ha sido creado anteriormente

    def existeArchivo(self, archivo):
        if archivo in self.reportes:
            print("\t\t\nArchivo con el mismo nombre YA EXISTENTE")
        else:
            self.reportes.append(archivo)
