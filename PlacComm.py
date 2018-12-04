# contains funcitons used to communicate to the Plac device
import json
import base64
import HWFuncs
from Crypto import Random
from Crypto.Cipher import AES
import hashlib
from base64 import b64encode as base64encode

class PlacComm:
    def __init__(self, id, passkey):
        self.id = str(id)
        # ensure that the key is in face 256 bits by hashing
        self.key = hashlib.sha256(str(passkey).encode()).digest()
        self.aes_mode = AES.MODE_CBC

    def send_data(self, **kwargs):
        try:
            json_data = json.dumps(kwargs)
            enc_data = self.__json_to_enc(json_data)
            packet = PlacPacket(self.id, enc_data)
            HWFuncs.send_packet(packet)
            return True
        except Exception as e:
            return e

    def __json_to_enc(self, json_string):
        iv = Random.new().read(16) # always 16 bytes of random for IV
        # iv = b'0123456789ABCDEF'
        encryptor = AES.new(self.key, self.aes_mode, iv)
        return iv + encryptor.encrypt(pad_data(json_string))

def pad_data(data):
    # adds extra chars such that the number of characters added is encoded into the end of the data
    padded_data = data + (16 - len(data) % 16) * chr(16 - len(data) % 16)
    return padded_data

class PlacPacket:
    def __init__(self, id, data):
        self.id = id
        self.data = data

    def __str__(self):
        return "{id:'" + str(self.id) + "',data:'" + str(self.data) + "'}"
