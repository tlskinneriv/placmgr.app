
# contains funcitons needed to call to send messages via the hardware
import serial
from base64 import b64encode as base64encode
import pigpio
import time

class HWFuncException(Exception):
    def __init__(self, error_text, old_error=None):
        self.error_text = error_text
        self.old_error = old_error

    def __str__(self):
        string = self.error_text
        if self.old_error != None:
            string += '\n' + str(self.old_error)
        return string

serial_port = '/dev/tty'
def send_packet(packet):
    encoded_bytes = base64encode((packet.id + ':' + str(len(packet.data)) + ':').encode() + packet.data)
    tmr_string = b'[[[' + encoded_bytes + b']]][[[' + encoded_bytes + b']]][[[' + encoded_bytes + b']]]'
    try:
        ser = serial.Serial(serial_port, 4800, timeout=0)
        if ser.isOpen() == False:
            ser.open()
        ser.write(tmr_string)
        ser.flush()
        ser.close()
    except Exception as e:
        raise HWFuncException('Could not send via the serial port "' + serial_port + '"', e)
