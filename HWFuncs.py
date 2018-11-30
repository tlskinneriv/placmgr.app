
# contains funcitons needed to call to send messages via the hardware
import serial
from base64 import b64encode as base64encode

def send_packet(packet):
    print('Sending the following packet...')
    print(packet)
    ser = serial.Serial('/dev/ttyAMA0', 1200, timeout=1)
    encoded_bytes = base64encode(packet.id + ':') + packet.data
    ser.open()
    ser.write(encoded_bytes)
    ser.close()
