import os
import hashlib
import time


class DigitalSignature:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_keys(self):
        start = time.time()

        self.private_key = os.urandom(32)
        self.public_key = hashlib.sha256(self.private_key).digest()

        end = time.time()
        return end - start

    def sign(self, message: bytes):
        start = time.time()

        signature = hashlib.sha256(self.private_key + message).digest()

        end = time.time()
        return signature, (end - start)

    def verify(self, message: bytes, signature: bytes):
        start = time.time()

        expected_signature = hashlib.sha256(self.private_key + message).digest()
        is_valid = signature == expected_signature

        end = time.time()
        return is_valid, (end - start)