import serial
import time

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

infected_plants = []
good_plants = []
interrupt = 1


def writetoArduino(x):
    arduino.write(bytes(x, 'utf-8'))


def write_read(x):
    
    #time.sleep(0.05)
    data = arduino.readline().decode('utf-8').rstrip()
    return data
while True:
    num = 0
    value = write_read(num)

    print(value)

    if(value=="90" or value=="160"):
        print("1")
        time.sleep(6)
        writetoArduino("0");