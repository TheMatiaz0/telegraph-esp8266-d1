import serial
import keyboard

ser = serial.Serial('COM6', 921600, timeout=1)

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
