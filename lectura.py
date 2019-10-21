import csv
import json
import sys
import os
import time

import cliente

class lectura():

    def lector_csv(self, _index_, phash):
        # Función para leer los archivos CSV
        print("\nEjecutando Lectura CSV...")
        nom_arch = input("Escribe el nombre del archivo: ")

        archivo = open("bloques/" + nom_arch)
        csv_file = csv.reader(archivo, delimiter=',')
        elementos = []
        for linea in csv_file:
            elementos += linea

        json_generado = "{"

        json_generado += "\"INDEX\": " + str(_index_) + ","
        
        json_generado += "\"TIMESTAMP\": " + "\"" + \
            time.strftime(("%d-%m-%y-::%H:%M:%S")) + "\","
        
        json_generado += "\"CLASS\": " + "\"" + elementos[1] + "\","
        datos = str(elementos[3])
        datos = str(elementos[3]).replace(" ", "")
        datos = datos.replace("\n", "")
        
        json_generado += "\"DATA\": " + datos + ","
        
        json_generado += "\"PREVIOUSHASH\": " + "\"" + phash + "\"" + ","
        
        json_generado += "\"HASH\": " + "\"" + cliente.Cliente().sha_256(int(_index_), time.strftime(
            ("%d-%m-%y-::%H:%M:%S")), elementos[1], datos, phash) + "\""
        
        json_generado += "}"
        
        json_generado = json_generado.replace(": ", ":")

        return json_generado

    def objetosValue(self, obj, d):
        # Método para generar el árbol AVL cuando pueda insertar el bloque al blockchain
        if d["left"] is not None:
            self.objetosValue(obj, d["left"])
        obj.append(d["value"])
        if d["right"] is not None:
            self.objetosValue(obj, d["right"])
        return obj

    def lector_json(self, string_json, server):
        # Función para leer los archivos JSON
        try:
            data = json.loads(string_json)

            index = data["INDEX"]
            time_ = str(data["TIMESTAMP"])
            clase = str(data["CLASS"])
            datos = str(data["DATA"])
            datos = datos.replace(" ", "")
            datos = datos.replace("\n", "")
            datos = datos.replace("'", "\"")
            datos = datos.replace("None", "null")
            phash = str(data["PREVIOUSHASH"])
            _hash = str(data["HASH"])
            
            hash_obtenido = cliente.Cliente().sha_256(index, time_, clase, datos, phash)
            
            print(hash_obtenido)
            if hash_obtenido == _hash:
                # Envio de true si hash obtenido es igual a hash generado originalmente.
                server.sendall("true".encode('utf-8'))
            else:
                server.sendall("false".encode('utf-8'))
        except Exception:
            print("ERROR CON MENSAJE")

    def visualizar_json(self, string_json):
        # Obtengo todos los datos y luego lo separo en campos...
        campos = json.loads(string_json)
        os.system("cls")
        mensaje = "INDEX: " + str(campos["INDEX"]) + "\n"
        mensaje += "TIMESTAMP: " + str(campos["TIMESTAMP"]) + "\n"
        mensaje += "CLASS: " + str(campos["CLASS"]) + "\n"
        mensaje += "DATA: " + str(campos["DATA"])[0:50] + "\n"
        mensaje += "PREVIOUSHASH: " + str(campos["PREVIOUSHASH"]) + "\n"
        mensaje += "HASH: " + str(campos["HASH"]) + "\n"

        print(mensaje)
