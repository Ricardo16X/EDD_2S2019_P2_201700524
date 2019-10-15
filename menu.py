import threading
import socket
import sys

import lectura
import arbol_avl

lectura.lector_csv()

mi_avl = arbol_avl.arbol_avl()

raiz = None
raiz = mi_avl.insert(raiz, 10)
raiz = mi_avl.insert(raiz, 20)
raiz = mi_avl.insert(raiz, 30)
raiz = mi_avl.insert(raiz, 40)
raiz = mi_avl.insert(raiz, 50)
raiz = mi_avl.insert(raiz, 25)

mi_avl.preOrder(raiz)

# Ingreso de IP y Host de Conexión:
#try:
    ## Intentar la conexión con el socket
#    conexion = socket.socket()
#    dir_ip = input("Ingrese la dirección IP del servidor.")
#    port = input("Ingrese el puerto de comunicación con el servidor.")
#    conexion.connect((dir_ip, int(port)))
    # Si la conexion se ha realizado con éxito, estar a la espera de información o cadenas de datos.
#except Exception:
#    print("Ha ocurrido un error en la comunicación cliente-servidor.")
# Menú Principal
