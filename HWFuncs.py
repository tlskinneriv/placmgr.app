
# contains funcitons needed to call to send messages via the hardware
import serial
from base64 import b64encode as base64encode

def send_packet(packet):
    print('Sending the following packet...')
    print(packet)
    serial_port = '/dev/ttyAMA0'
    ser = serial.Serial(serial_port, 1200, timeout=1)
    encoded_bytes = base64encode((packet.id + ':').encode()) + packet.data
    print(encoded_bytes)
    if ser.isOpen() == False:
        try:
            ser.open()
        except Exception as e:
            print(e)
    ser.write(encoded_bytes)
    ser.close()
