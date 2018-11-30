# contains funcitons used to communicate to the Plaq device
import json
import base64
import HWFuncs
from Crypto import Random
from Crypto.Cipher import AES

class PlaqComm:
    def __init__(self, enc_key):
        if len(enc_key) != 32:
            raise Exception('Incorrect key length! Key must be 32 bytes (256-bit)')
        self.enc_key = enc_key

    def send_data(self, **kwargs):
        print(json.dumps(kwargs))

def __json_to_enc(json_string, key):
    raw = self._pad(raw)
    iv = Random.new().read(AES.block_size)

def __enc_to_bytes(enc_string):
    pass
