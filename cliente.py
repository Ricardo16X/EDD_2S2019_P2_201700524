import json
import hashlib
import socket
import sys
import os
import time
import csv

import lectura

class Cliente(object):
    # Función Hash
    def sha_256(self, index_, timestamp_, class_, data_, pHash_):
        estado = str(index_).encode('utf-8') + str(timestamp_).encode('utf-8') + str(
            class_).encode('utf-8') + str(data_).encode('utf-8') + str(pHash_).encode('utf-8')
        sha = hashlib.sha256(estado).hexdigest()
        return str(sha)
