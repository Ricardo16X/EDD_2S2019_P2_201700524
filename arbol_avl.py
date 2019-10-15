class nodoArbol(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class arbol_avl(object):
    def insert(self, raiz, valor):
        if not raiz:
            return nodoArbol(valor)
        elif valor < raiz.val:
            raiz.left = self.insert(raiz.left, valor)
        else:
            raiz.right = self.insert(raiz.right, valor)

        # Actualización de la altura del padre
        raiz.height = 1 + max(self.getHeight(raiz.left),
                              self.getHeight(raiz.right))

        # Obtener el Factor de Equilibrio
        balance = self.getBalance(raiz)

        # Si el nodo está desbalanceado
        # entonces se intentará los 4 casos de inserción
        # Caso 1 - Izq Izq
        if balance > 1 and valor < raiz.left.val:
            return self.RotacionDerecha(raiz)
        # Caso 2 - Der Der
        if balance < -1 and valor > raiz.right.val:
            return self.RotacionIzquierda(raiz)
        # Caseo 3 - Izq Der
        if balance > 1 and valor > raiz.left.val:
            raiz.left = self.RotacionIzquierda(raiz.left)
            return self.RotacionDerecha(raiz)
        # Caso 4 - Der Izq
        if balance < -1 and valor < raiz.right.val:
            raiz.right = self.RotacionDerecha(raiz.right)
            return self.RotacionIzquierda(raiz)

        return raiz

    def RotacionDerecha(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Retornamos la nueva raiz.
        return y

    def RotacionIzquierda(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left),
                                self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                                self.getHeight(y.right))
        # Retornamos la nueva raiz después del balanceo o movimiento
        # hacia la izquierda.
        return y

    def getHeight(self, raiz):
        if not raiz:
            return 0
        return raiz.height

    def getBalance(self, raiz):
        if not raiz:
            return 0
        return self.getHeight(raiz.left) - self.getHeight(raiz.right)

    def preOrder(self, raiz):
        if not raiz:
            return
        print("{0} ".format(raiz.val), end="")
        self.preOrder(raiz.left)
        self.preOrder(raiz.right)