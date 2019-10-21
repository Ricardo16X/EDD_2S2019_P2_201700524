## Lista enlazada doble para almacenar la información del JSON
import json
class nodoLista():
    ## Elementos que contendrá el nodo de la lista enlazada
    def __init__(self,_str_json):
        self.str_json = _str_json
        self.index = 0
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
            nuevoBloque.index = self.ultimo.index + 1
            
            self.ultimo.siguiente = nuevoBloque
            nuevoBloque.anterior = self.ultimo
            self.ultimo = nuevoBloque

    def getLastIndex(self):
        if self.primero is None:
            return 0
        else:
            return int(self.ultimo.index)
    
    def getHash(self):
        if self.primero is None:
            return "0000"
        else:
            try:
                obtenerHash = json.loads(self.ultimo.str_json)
                return obtenerHash["HASH"]
            except Exception:
                print("Error al obtener el Hash Anterior")
