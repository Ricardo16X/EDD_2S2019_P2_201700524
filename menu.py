import threading
import socket
import sys

import lectura
import arbol_avl

lectura.lector_csv()

mi_avl = arbol_avl.arbol_avl()

raiz = None


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
