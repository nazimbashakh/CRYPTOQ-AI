import os
import hashlib

# Simulate client private key
client_private = os.urandom(32)

# Simulate server private key
server_private = os.urandom(32)

# Simulate shared secret derivation
client_shared = hashlib.sha256(client_private + server_private).digest()
server_shared = hashlib.sha256(client_private + server_private).digest()

print("Client Shared Secret:", client_shared.hex())
print("Server Shared Secret:", server_shared.hex())
print("Secrets Match:", client_shared == server_shared)