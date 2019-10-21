import threading
import time
import sys
import socket
import os
import select
import msvcrt

import lectura
import arbol_avl
import cliente
import blocks

lector = lectura.lectura()
avl = arbol_avl.arbol_avl()
cli = cliente.Cliente()
block = blocks.listaDoble()

ip = sys.argv[1]    ## Variables Globales IP
puerto = int(sys.argv[2])   ## Variables Globales Port
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
json_volando = ""

def connect():
    if len(sys.argv) != 3:
        print("Ingresa los parámetros de esta manera: script ip puerto")
    else:
        ip = sys.argv[1]
        puerto = sys.argv[2]
        server.connect((ip, int(puerto)))
        mensaje = ""
        while True:
            try:
                read_sockets = select.select([server], [], [], 0)[0]
                for socks in read_sockets:
                    if socks == server:
                        ## Aqui estoy recibiendo información del server...
                        mensaje = str(server.recv(4096))
                        if mensaje.find("true") != -1:
                            if json_volando != "" and not json_volando.find("Welcome") != -1:
                                block.insert(str(json_volando))
                                print("Bloque Insertado")
                        else:
                            # json
                            mensaje = mensaje[2:len(mensaje) - 1]
                            json_volando = mensaje
                            lector.lector_json(mensaje, server)
            except Exception:
                break
        server.close()

def menu():
    while True:
        print("1. Insertar Bloque")
        print("2. Seleccionar Bloque")
        print("3. Reportes")
        print("4. Salir")
        op = int(input("Seleccione una opción: "))
        # Selección de Acción
        if op == 1:
            # Insertar un bloque
            os.system("cls")
            print("Insertar Bloque ##Seleccionado")
            indice = block.getLastIndex()
            phash = block.getHash()
            json = lector.lector_csv(indice, phash)
            server.sendall(json.encode('utf-8'))
            mensaje = str(server.recv(2048))
            if mensaje.find("true") != 1:
                block.insert(json)
        elif op == 2:
            # Seleccionar un bloque
            if block.primero is not None:
                # Genero un bloque copia para poder obtener su izquierdo o su derecho...
                copia = block.primero
                lector.visualizar_json(copia.str_json)
                while True:
                    key = msvcrt.kbhit()
                    if key:
                        ret = ord(msvcrt.getch())
                        if ret == 27:   # ESC se sale del programa
                            break
                        elif ret == 75:
                            # Pintar el izquierdo del objeto actual en el blockchain
                            if copia.anterior is not None:
                                copia = copia.anterior
                            lector.visualizar_json(copia.str_json)
                        elif ret == 77:
                            # Pintar el derecho del objeto actual en el blockchain
                            if copia.siguiente is not None:
                                copia = copia.siguiente
                                lector.visualizar_json(copia.str_json)
                        elif ret == 13:  # Ingreso de ENTER
                            cli.reportes(copia.str_json)
            else:
                print("El bloque no contiene datos...")

        elif op == 3:
            # Generar Reportes de...
            print("Generar Reportes ##Seleccionado")
            block.graphic()
        elif op == 4:
            # Salir
            print("Salir ##Seleccionado")
            server.close()
            hilo_m._delete()
            hilo_c._delete()
            break
        else:
            print("No ha seleccionado una opción válida. \nIntente nuevamente... ")
            time.sleep(5.5)

hilo_c = threading.Thread(target=connect)
hilo_m = threading.Thread(target=menu)

hilo_c.start()
hilo_m.start()
