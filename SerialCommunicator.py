import time
import serial

# ARDUINO = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=0.2)

def write_read(x, arduino):
	print("Writing:", x)
	arduino.write(bytes(x, 'utf-8'))
	time.sleep(0.05)
	data = arduino.readline()
	return data.decode('utf-8')


# string = input("Enter a string: ")
# value = write_read(string, ARDUINO)

# value = write_read("HELLO", ARDUINO)
# print(value)
