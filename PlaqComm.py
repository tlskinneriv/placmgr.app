# contains funcitons used to communicate to the Plaq device
import json
import base64
import HWFuncs
from Crypto import Random
from Crypto.Cipher import AES
import hashlib
from base64 import b64encode as base64encode
from base64 import b64decode as base64decode

class PlaqComm:
    def __init__(self, id, passkey):
        self.id = str(id)
        # ensure that the key is in face 256 bits by hashing
        self.key = hashlib.sha256(str(passkey).encode()).digest()
        self.aes_mode = AES.MODE_CBC

    def send_data(self, **kwargs):
        try:
            json_data = json.dumps(kwargs)
            enc_data = self.__json_to_enc(json_data)
            packet = PlaqPacket(self.id, enc_data)
            HWFuncs.send_packet(packet)
            return True
        except Exception as e:
            return e

    def __json_to_enc(self, json_string):
        #iv = Random.new().read(16) # always 16 bytes of random for IV
        iv = bytearray(16)
        encryptor = AES.new(self.key, self.aes_mode, iv)
        return iv + encryptor.encrypt(pad_data(json_string))

    # included method to check against for decrypting data
    # def __enc_to_json(self, enc_data):
    #     enc_data = base64decode(enc_data)
    #     print('edlen=' + str(len(enc_data)))
    #     iv = enc_data[:16]
    #     decryptor = AES.new(self.key, self.aes_mode, iv)
    #     return unpad_data(decryptor.decrypt(enc_data[16:])).decode()

def pad_data(data):
    # adds extra chars such that the number of characters added is encoded into the end of the data
    padded_data = data + (16 - len(data) % 16) * chr(16 - len(data) % 16)
    return padded_data

# included method to check against for decrypting data
# def unpad_data(padded_data):
#     # removes the extra padding from the json_string
#     data = padded_data[:-ord(padded_data[-1:])]
#     return data


class PlaqPacket:
    def __init__(self, id, data):
        self.id = id
        self.data = data

    def __str__(self):
        return "{id:'" + str(self.id) + "',data:'" + str(self.data) + "'}"
