import serial
import serial.tools.list_ports
import keyboard
import time

def find_arduino_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if "Arduino" in port.description or "USB" in port.description:
            return port.device
    return None

def connect_arduino():
    while True:
        arduino_port = find_arduino_port()
        if arduino_port:
            try:
                ser = serial.Serial(arduino_port, 921600, timeout=1)
                print(f"Connected to {arduino_port}")
                return ser
            except serial.SerialException:
                print(f"Error opening serial port {arduino_port}. Retrying...")
        else:
            print("No Arduino found. Retrying in 2 seconds...")
        time.sleep(2)

ser = connect_arduino()
previous_char = 'b'

while True:
    try:
        if ser.in_waiting > 0:
            data = ser.read().decode('utf-8').strip()

            if data == 'a' and previous_char != 'a':
                keyboard.press('space')
                print("Space pressed!")
                previous_char = 'a'

            elif data == 'b' and previous_char != 'b':
                keyboard.release('space')
                print("Space released!")
                previous_char = 'b'

    except serial.SerialException:
        print("Arduino disconnected! Attempting to reconnect...")
        ser.close()
        ser = connect_arduino()
