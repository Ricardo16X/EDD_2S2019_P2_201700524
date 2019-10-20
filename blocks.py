## Lista enlazada doble para almacenar la información del JSON
class nodoLista(object):
    ## Elementos que contendrá el nodo de la lista enlazada
    def __init__(self,_str_json):
        self.str_json = _str_json
        self.index = 0
        # puntadores
        self.siguiente = None
        self.anterior = None

class listaDoble(object):
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
            nuevoBloque.index = self.ultimo.index + 1