import os
import hashlib
import time


class QuantumKeyExchange:
    def __init__(self):
        self.client_private = None
        self.server_private = None
        self.shared_secret = None

    def generate_keys(self):
        start = time.time()

        self.client_private = os.urandom(32)
        self.server_private = os.urandom(32)

        end = time.time()
        return end - start

    def derive_shared_secret(self):
        start = time.time()

        self.shared_secret = hashlib.sha256(
            self.client_private + self.server_private
        ).digest()

        end = time.time()
        return end - start

    def get_shared_secret(self):
        return self.shared_secret