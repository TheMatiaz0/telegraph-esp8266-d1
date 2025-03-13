import serial
import serial.tools.list_ports
import keyboard

def find_arduino_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if "Arduino" in port.description or "USB" in port.description:
            return port.device
    return None

arduino_port = find_arduino_port()

if not arduino_port:
    print("No Arduino found. Please check your connection.")
    exit()

ser = serial.Serial(arduino_port, 921600, timeout=1)
print(f"Connected to {arduino_port}")
   
previous_char = 'b'

while True:
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