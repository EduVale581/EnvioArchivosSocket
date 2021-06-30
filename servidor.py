import socket
import struct
from datetime import datetime
import os

def archivoRecibido(socketCreado: socket.socket, archivo):
    # Leer la cantidad de bytes del archivo.

    fmt = "<Q"
    byteEsperado = struct.calcsize(fmt)
    byteRecibido = 0
    inicializacionByte = bytes()
    while byteRecibido < byteEsperado:
        particion = socketCreado.recv(byteEsperado - byteRecibido)
        inicializacionByte += particion
        byteRecibido += len(particion)
    tamarchivo = struct.unpack(fmt, inicializacionByte)[0]

    # Abrir un nuevo archivo para guardar los datos recibidos.
    with open(archivo, "wb") as f:
        byteRecibido = 0
        # Recibir los datos del archivo en bloques de 1024 bytes 
        # hasta llegar a la cantidad de bytes total.
        while byteRecibido < tamarchivo:
            particion = socketCreado.recv(1024)
            if particion:
                f.write(particion)
                byteRecibido += len(particion)


os.remove("file.log")
with socket.create_server(("192.168.1.83", 6080)) as server:
    print("Esperando al cliente...")
    conn, address = server.accept()
    print(f"{address[0]}:{address[1]} conectado.")
    print("Recibiendo archivo...")
    #Fecha actual
    now = datetime.now()
    fechaActual = format(now.day)+"_" + format(now.month)+"_"+format(now.year)+"__"+format(now.hour)+":"+format(now.minute)+":"+format(now.second)
    nombreArchivo = "file_"+fechaActual+".log"
    archivoRecibido(conn, nombreArchivo)
    print("Archivo recibido.")
print("Conexión cerrada.")