import serial


def eduardo():
    port = serial.Serial("COM3", 9600, timeout=1)

    dato = port.readline()
    dato1 = str(dato)
    dato2 = dato1.split(":")[1]
    dato3 = dato2.split("\\")[0]
    voltage = (int(dato3)*5)/4095
    voltage2 = "{:.3f}".format(voltage)
    print(voltage2)
    return voltage2
    port.close()
