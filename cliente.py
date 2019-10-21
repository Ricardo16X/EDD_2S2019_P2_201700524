import json
import hashlib
import socket
import sys
import os
import time
import csv

import lectura
import arbol_avl

class Cliente(object):
    # Función Hash
    def sha_256(self, index_, timestamp_, class_, data_, pHash_):
        estado = str(index_).encode('utf-8') + str(timestamp_).encode('utf-8') + str(
            class_).encode('utf-8') + str(data_).encode('utf-8') + str(pHash_).encode('utf-8')
        sha = hashlib.sha256(estado).hexdigest()
        return str(sha)

    def reportes(self, copiaJson):
        ### Este reporte contendrá el árbol AVL y sus recorridos
        while True:
            os.system("cls")
            print("###REPORTES###")
            print("1. Visualizar Arbol")
            print("2. Mostrar Recorridos")
            print("3. Salir")
            op = int(input("Ingresa la opción que desees: "))
            if op == 1:
                obj = []
                datos = json.loads(copiaJson)
                data = json.dumps(datos["DATA"])
                data = data.replace("rigth","right")
                d = json.loads(data)
                lectura.lectura().objetosValue(obj, d)
                # Ya que tengo todos los nodos, los ingreso al árbol, y luego lo grafico
                arbol = arbol_avl.arbol_avl()
                raiz = None
                for item in obj:
                    raiz = arbol.insert(raiz, item)
                self.graficarArbolGeneral(raiz)
            if op == 2:
                while True:
                    print("###RECORRIDOS###")
                    print("1. In Order")
                    print("2. Pre Order")
                    print("3. Post Order")
                    print("4. Salir")
                    op = int(input("Elige una opción válida: "))
                    if op == 1:
                        obj = []
                        datos = json.loads(copiaJson)
                        data = json.dumps(datos["DATA"])
                        data = data.replace("rigth","right")
                        d = json.loads(data)
                        lectura.lectura().objetosValue(obj, d)
                        # Ya que tengo todos los nodos, los ingreso al árbol, y luego lo grafico
                        arbol = arbol_avl.arbol_avl()
                        raiz = None
                        for item in obj:
                            raiz = arbol.insert(raiz, item)
                        dot = []
                        dot.append("digraph G{\n rankdir = \"LR\"\n")
                        console_dot = []
                        console_dot.append("INICIO")
                        self.inOrder(raiz, dot, console_dot)
                        dot_file = open("inOrder.dot", "w")

                        c_item = ""
                        for item in dot:
                            c_item += item

                        c_item = c_item[0:len(c_item) - 3]
                        c_item += "}"
                        rep = ""
                        for item_c in console_dot:
                            rep += item_c + " -> "
                        rep += "FIN"
                        dot_file.write(c_item)
                        dot_file.close()
                        os.system("dot -Tpng inOrder.dot -o inOrder.png")
                        os.system("inOrder.png")
                        print(rep)
                    elif op == 2:
                        obj = []
                        datos = json.loads(copiaJson)
                        data = json.dumps(datos["DATA"])
                        data = data.replace("rigth","right")
                        d = json.loads(data)
                        lectura.lectura().objetosValue(obj, d)
                        # Ya que tengo todos los nodos, los ingreso al árbol, y luego lo grafico
                        arbol = arbol_avl.arbol_avl()
                        raiz = None
                        for item in obj:
                            raiz = arbol.insert(raiz, item)
                        dot = []
                        dot.append("digraph G{\n rankdir = \"LR\"\n")
                        console_dot = []
                        console_dot.append("INICIO")

                        self.preOrder(raiz, dot, console_dot)
                        dot_file = open("preOrder.dot", "w")
                        
                        c_item = ""
                        for item in dot:
                            c_item += item

                        c_item = c_item[0:len(c_item) - 3]
                        c_item += "}"
                        rep = ""
                        for item_c in console_dot:
                            rep += item_c + " -> "
                        rep += "FIN"

                        dot_file.write(c_item)
                        dot_file.close()
                        os.system("dot -Tpng preOrder.dot -o preOrder.png")
                        os.system("preOrder.png")
                        print(rep)
                        time.sleep(5)
                    elif op == 3:
                        obj = []
                        datos = json.loads(copiaJson)
                        data = json.dumps(datos["DATA"])
                        data = data.replace("rigth","right")
                        d = json.loads(data)
                        lectura.lectura().objetosValue(obj, d)
                        # Ya que tengo todos los nodos, los ingreso al árbol, y luego lo grafico
                        arbol = arbol_avl.arbol_avl()
                        raiz = None
                        for item in obj:
                            raiz = arbol.insert(raiz, item)
                        dot = []
                        dot.append("digraph G{\n rankdir = \"LR\"\n")
                        console_dot = []
                        console_dot.append("INICIO")
                        self.postOrder(raiz, dot, console_dot)
                        dot_file = open("postOrder.dot", "w")
                        c_dot_file = ""
                        for item in dot:
                            c_dot_file += item

                        c_dot_file = c_dot_file[0:len(c_dot_file) - 3]
                        c_dot_file += "}"
                        dot_file.write(c_dot_file)
                        rep = ""
                        for item_c in console_dot:
                            rep += item_c + " -> "
                        rep += "FIN"
                        
                        dot_file.close()
                        os.system("dot -Tpng postOrder.dot -o postOrder.png")
                        os.system("postOrder.png")
                        print(rep)
                        time.sleep(5)
                    elif op == 4:
                        break

                
    def graficarArbolGeneral(self,arbol_general):
        dot = []
        dot.append("digraph G{\n")
        id_ = 1
        self.apoyograficarArbolGeneral(arbol_general, dot, id_)
        dot.append("}")

        u_dot = ""
        for item in dot:
            u_dot += item 

        dot_file = open("arbolAVL.dot","w")
        dot_file.write(u_dot)
        dot_file.close()
        os.system("dot -Tjpg arbolAVL.dot -o arbolAVL.jpg")
        os.system("arbolAVL.jpg")
    
    def apoyograficarArbolGeneral(self, raiz, dot, id_):
        if raiz != None:
            dot.append( "\"" + raiz.carne + "-" + raiz.nombre + "\"" + "[label = \"" + "\\nCarne: " + raiz.carne + "\\nNombre:" + raiz.nombre + "\\nAltura: " + str(raiz.height) + "\\nFE: " + str(raiz.FE) + "\"];\n")
            id_ = id_ + 1
            self.apoyograficarArbolGeneral(raiz.left, dot, id_)
            self.apoyograficarArbolGeneral(raiz.right, dot, id_)

            if raiz.left is not None:
                dot.append("\"" + raiz.carne + "-" + raiz.nombre + "\"" + " -> " + "\"" + raiz.left.carne + "-" + raiz.left.nombre + "\"" + ";\n")

            if raiz.right is not None:
                dot.append("\"" + raiz.carne + "-" + raiz.nombre + "\"" + " -> " + "\"" + raiz.right.carne + "-" + raiz.right.nombre + "\"" + ";\n")

    def inOrder(self, raiz, dot, dot_c):
        if raiz is not None:
            self.inOrder(raiz.left, dot, dot_c)
            dot.append("\"" + raiz.carne + "\\n" + raiz.nombre + "\" -> ")
            dot_c.append(raiz.carne + "-" + raiz.nombre)
            self.inOrder(raiz.right, dot, dot_c)
    
    def preOrder(self, raiz, dot, dot_c):
        if raiz is not None:
            dot.append("\"" + raiz.carne + "\\n" + raiz.nombre + "\" -> ")
            dot_c.append(raiz.carne + "-" + raiz.nombre)
            self.preOrder(raiz.left, dot, dot_c)
            self.preOrder(raiz.right, dot, dot_c)

    def postOrder(self, raiz, dot, dot_c):
        if raiz is not None:
            self.postOrder(raiz.left, dot, dot_c)
            self.postOrder(raiz.right, dot, dot_c)
            dot.append("\"" + raiz.carne + "\\n" + raiz.nombre + "\" -> ")
            dot_c.append(raiz.carne + "-" + raiz.nombre)
