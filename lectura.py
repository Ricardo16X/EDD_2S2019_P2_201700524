import csv
import json
import sys
import os

class lectura():

    def lector_csv(self):
        # Función para leer los archivos CSV
        print("\nEjecutando Lectura CSV...")
        nom_arch = input("Escribe el nombre del archivo: ")

        archivo = open("bloques/" + nom_arch)
        csv_file = csv.reader(archivo, delimiter=',')
        lista = []
        for linea in csv_file:
            lista += linea

        clase = lista[1]
        print(clase)
        datos = lista[3]
        print(datos)

    def lector_json(self, string_json):
        # Función para leer los archivos JSON
        print("Ejecutando Lectura JSON")
        
