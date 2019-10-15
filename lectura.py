import csv
import json
import sys
import os

def lector_csv():
    ## Función para leer los archivos CSV
    print("\nEjecutando Lectura CSV...")
    nom_arch = input("Escribe el nombre del archivo: ")

    archivo = open(nom_arch)
    csv_file = csv.reader(archivo, delimiter=',')
    lista = []
    for linea in csv_file:
        lista += linea

    clase = lista[1]
    print(clase)
    datos = lista[3]
    print(datos)

def lector_json():
    ## Función para leer los archivos JSON
    print("Ejecutando Lectura JSON")