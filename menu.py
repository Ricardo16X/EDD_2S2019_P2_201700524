import threading
import time
import sys
import socket

import lectura
import arbol_avl
import cliente
import blocks
import select


lector = lectura.lectura()
avl = arbol_avl.arbol_avl()
cli = cliente.Cliente()
block = blocks.listaDoble()

def connect():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if len(sys.argv) != 3:
        print("Ingresa los parámetros de esta manera: script ip puerto")
 
    ip = sys.argv[1]
    puerto = int(sys.argv[2])
    conexion = socket.socket()
    conexion.connect((ip,puerto))

    while True:
        socket_enlinea = select.select([server],[],[],1)[0]
        import msvcrt
        if msvcrt.kbhit(): socket_enlinea.append(sys.stdin)

        for socks in socket_enlinea:
            if socks == server:
                mensaje = socks.recv(2048)
                print("Mensaje Recibido: " + mensaje.decode('utf-8'))
            else:
                



hilo = threading.Thread()

cli.menu(block)
hilo.start()
