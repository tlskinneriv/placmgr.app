# contains funcitons used to communicate to the Plaq device
import json
import base64
import HWFuncs
from Crypto import Random
from Crypto.Cipher import AES
import hashlib

class PlaqComm:
    def __init__(self, id, passkey):
        self.id = str(id)
        self.passkey = str(passkey)
        # ensure that the key is in face 256 bits by hashing
        self.passkey_256 = hashlib.sha256(self.passkey).digest()

    def send_data(self, **kwargs):
        print('Using plaq id "' + self.id + '" with passkey "' + self.passkey + '"')
        print(json.dumps(kwargs))

def __json_to_enc(json_string, key):
    raw = self._pad(raw)
    iv = Random.new().read(AES.block_size)

def __enc_to_bytes(enc_string):
    pass
