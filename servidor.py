import socket
import struct
import os
from threading import Timer
from pathlib import Path




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

def iniciarServidor():
    while True:
        fileObj = Path("file.log")
    
        if fileObj.exists():
            os.remove("file.log")
        with socket.create_server(("192.168.1.83", 6080)) as server:
            print("Esperando al cliente...")
            conn, address = server.accept()
            print(f"{address[0]}:{address[1]} conectado.")
            print("Recibiendo archivo...")
            nombreArchivo = "file.log"
            archivoRecibido(conn, nombreArchivo)
            print("Archivo recibido.")
        print("Conexión cerrada.")



timer = Timer(interval=10, function=iniciarServidor)
#timer.daemon=True
timer.start()
