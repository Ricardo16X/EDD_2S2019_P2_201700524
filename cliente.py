import json
import hashlib
import socket
import sys
import os
import time
import csv

import lectura

class Cliente(object):
    # Función Hash
    def sha_256(self, index_, timestamp_, class_, data_, pHash_):
        estado = str(index_).encode('utf-8') + str(timestamp_).encode('utf-8') + str(
            class_).encode('utf-8') + str(data_).encode('utf-8') + str(pHash_).encode('utf-8')
        sha = hashlib.sha256(estado).hexdigest()
        return str(sha)

    def menu(self, block):
        while True:
            print("1. Insertar Bloque")
            print("2. Seleccionar Bloque")
            print("3. Reportes")
            print("4. Salir")
            op = int(input("Seleccione una opción: "))
            # Selección de Acción
            if op == 1:
                # Insertar un bloque
                # Generando json sin json.load()
                print("Insertar Bloque ##Seleccionado")
                if block.primero is None:
                    ## No hay bloques ingresados.
                    json = lectura.lectura().lector_csv(0)
                else:
                    json = lectura.lectura().lector_csv(block.ultimo.index)
                # Retornando el json del archivo csv leido
                return json

            elif op == 2:
                # Seleccionar un bloque
                os.system("cls")
                print("Seleccionar Bloque ##Seleccionado")

            elif op == 3:
                # Generar Reportes de...
                print("Generar Reportes ##Seleccionado")
            elif op == 4:
                # Salir
                print("Salir ##Seleccionado")
                break
            else:
                print("No ha seleccionado una opción válida. \nIntente nuevamente... ")
                time.sleep(5000)
