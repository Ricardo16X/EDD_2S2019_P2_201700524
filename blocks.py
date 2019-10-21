## Lista enlazada doble para almacenar la información del JSON
import json
import os

class nodoLista():
    ## Elementos que contendrá el nodo de la lista enlazada
    def __init__(self,_str_json):
        self.str_json = _str_json
        # puntadores
        self.siguiente = None
        self.anterior = None
        self.primero = None
        self.ultimo = None

class listaDoble():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insert(self, bloque):
        if self.primero is None:
            # No hay ningun dato:
            nuevoBloque = nodoLista(bloque)
            self.primero = self.ultimo = nuevoBloque
            nuevoBloque.index = 0
        else:
            # Si hay datos en el blockchain
            nuevoBloque = nodoLista(bloque)

            self.ultimo.siguiente = nuevoBloque
            nuevoBloque.anterior = self.ultimo
            self.ultimo = nuevoBloque

    def getLastIndex(self):
        if self.primero is None:
            return -1
        else:
            try:
                obtenerIndex = json.loads(self.ultimo.str_json)
                return int(obtenerIndex["INDEX"])
            except Exception:
                print("Error al obtener el Hash Anterior")
    
    def getHash(self):
        if self.primero is None:
            return "0000"
        else:
            try:
                obtenerHash = json.loads(self.ultimo.str_json)
                return obtenerHash["HASH"]
            except Exception:
                print("Error al obtener el Hash Anterior")

    def graphic(self):
        if self.primero is None:
            print("No puedo generar el reporte aún")
            print("No tengo bloques")
        else:
            temporal = self.primero
            nuevoArchivo = open("BlockChain.dot","w")
            nuevoArchivo.write("digraph G{\n")
            nuevoArchivo.write("rankdir = \"TB\"\n")
            nuevoArchivo.write("node [shape = record];\n")

            numNodo = 1
            while temporal is not None:
                dato = json.loads(temporal.str_json)
                nuevoArchivo.write("n" + str(numNodo) + " [label=\"" + "Clase: " + str(dato["CLASS"]) + "\\n" + "TimeStamp: " + str(dato["TIMESTAMP"]) + "\\n" + "Previous Hash: " + str(dato["PREVIOUSHASH"])[0:10] + " Hash: " + str(dato["HASH"])[0:10] + " \"];\n")
                numNodo += 1
                temporal = temporal.siguiente
            numNodo -= 1
            i = 1
            while i < numNodo:
                nuevoArchivo.write("n" + str(i) + " -> " + "n" + str(i + 1) + " [dir=both];\n")
                i += 1
            nuevoArchivo.write("}")
            nuevoArchivo.close()
            os.system("dot -Tjpg BlockChain.dot -o BlockChain.jpg")
            os.system("BlockChain.jpg")