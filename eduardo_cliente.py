import socket
import time
from seriall import eduardo
from datetime import datetime

mi_socket = socket.socket()
mi_socket.connect(('10.13.2.48', 81))


while True:
    voltage2 = eduardo()

    Timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    mensaje = f"{voltage2},{Timestamp}"
    mi_socket.send(mensaje.encode("ascii"))

    time.sleep(5)  # Espera de 5 segundos

mi_socket.close()
