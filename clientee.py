import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime

# Configura el puerto serial con un tiempo de espera más corto
port = serial.Serial("COM3", 9600, timeout=0.05)

# Función para leer el voltaje del puerto serial
def read_voltage():
    while True:
        try:
            dato = port.readline().decode().strip()
            if dato:
                parts = dato.split(":")
                if len(parts) == 2:
                    voltage_raw = parts[1].split("\\")[0]
                    voltage = (int(voltage_raw) * 5) / 4095
                    yield voltage
        except Exception as e:
            print(f"Error reading from serial port: {e}")

# Función para actualizar la gráfica
def animate(i, xs, ys):
    voltage = next(read_voltage_gen)
    xs.append(datetime.now())
    ys.append(voltage)

    xs = xs[-50:]  # Mantiene los últimos 50 puntos
    ys = ys[-50:]

    ax.clear()
    ax.plot(xs, ys)
    ax.set_ylim(0, 5)

    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Voltage over Time')
    plt.ylabel('Voltage (V)')

fig, ax = plt.subplots()
xs = []
ys = []

read_voltage_gen = read_voltage()

# Configura un intervalo de animación más corto para una mayor frecuencia de muestreo
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=50)
plt.show()
