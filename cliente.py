import json
import hashlib
import socket
import sys
import os
import time
import csv


class Cliente(object):
    # Función Hash
    def sha_256(self, index_, timestamp_, class_, data_, pHash_):
        estado = str(index_).encode('utf-8') + str(timestamp_).encode('utf-8') + str(
            class_).encode('utf-8') + str(data_).encode('utf-8') + str(pHash_).encode('utf-8')
        print(data_)
        sha = hashlib.sha256(estado).hexdigest()
        return str(sha)

    def menu(self):
        while True:
            print("1. Insertar Bloque")
            print("2. Seleccionar Bloque")
            print("3. Reportes")
            print("4. Salir")
            op = int(input("Seleccione una opción: "))
            # Selección de Acción
            if op == 1:
                # Insertar un bloque
                print("Insertar Bloque ##Seleccionado")
                nom_csv = input("Ingrese el nombre del archivo csv: ")
                csv_file = open("bloques/" + nom_csv, "r")
                lector = csv.reader(csv_file, delimiter=",")
                elementos = []
                for linea in lector:
                    elementos += linea

                ########## CREACION DE DICCIONARIO ALMACENADOR DE JSON ##########
                # Generando json sin json.load()
                json_generado = "{"
                json_generado += "\"INDEX\": " + "\"" + str(0) + "\","
                json_generado += "\"TIMESTAMP\": " + "\"" + time.strftime(("%d-%m-%y-::%H:%M:%S")) + "\","
                json_generado += "\"CLASS\": " + "\"" + elementos[1] + "\","
                datos = str(elementos[3]).replace(" ","")
                datos = datos.replace("\n","")
                json_generado += "\"DATA\": " + datos + ","
                json_generado += "\"PREVIOUSHASH\": " + "\"" + "0000" + "\"" + ","
                json_generado += "\"HASH\": " + "\"" + self.sha_256(0, time.strftime(
                    ("%d-%m-%y-::%H:%M:%S")), elementos[1], datos, "0000") + "\""
                json_generado += "}\n"
                json_generado = json_generado.replace(": ",":")
                
                print(json_generado)

                ## Leyendo el json generado
                with open('ENVIO_BLOQUE.json') as f:
                    data = json.load(f)
                
                index = str(data["INDEX"])
                index = index.replace("'", "\"")
                index = index.replace(": ", ":")
                print(index)
                time_ = str(data["TIMESTAMP"])
                time_ = time_.replace("'", "\"")
                time_ = time_.replace(": ", ":")
                print(time_)
                clase = str(data["CLASS"])
                clase = clase.replace("'", "\"")
                clase = clase.replace(": ", ":")
                print(clase)
                datos = str(data["DATA"])
                datos = datos.replace(" ", "")
                datos = datos.replace("\n","")
                datos = datos.replace("'", "\"")
                datos = datos.replace(": ", ":")
                print(datos)
                phash = str(data["PREVIOUSHASH"])
                phash = phash.replace("'", "\"")
                phash = phash.replace(": ", ":")
                print(phash)
                _hash = str(data["HASH"])
                _hash = _hash.replace("'", "\"")
                _hash = _hash.replace(": ", ":")
                print(_hash)
                print(index+time_+clase+datos+phash)
                hash_obtenido = self.sha_256(index,time_,clase,datos,phash)
                print(hash_obtenido)

            elif op == 2:
                # Seleccionar un bloque
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
