import serial

port = serial.Serial("COM3", 9600, timeout=1)

try:
    while True:
        command = input(
        "Escribe un carácter y presiona Enter para enviarlo al dispositivo (o Ctrl+C para salir): ")
        # Convierte el carácter a bytes y envíalo al dispositivo
        port.write(command.encode())
        datos = port.readline()

except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    pass
finally:
    port.close()
