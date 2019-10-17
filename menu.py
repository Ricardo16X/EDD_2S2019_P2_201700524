import threading

import lectura
import arbol_avl
import cliente
import blocks


lector = lectura.lectura()
avl = arbol_avl.arbol_avl()
cli = cliente.Cliente()
block = blocks.listaDoble()
## Muestreo de Menú
cli.menu()
## Creación de Menú
