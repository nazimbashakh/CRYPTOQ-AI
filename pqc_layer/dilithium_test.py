import os
import hashlib

# Simulate private key
private_key = os.urandom(32)

# Derive public key (simulation)
public_key = hashlib.sha256(private_key).digest()

# Message to sign
message = b"Secure Financial Transaction"

# Create signature (simulate Dilithium signing)
signature = hashlib.sha256(private_key + message).digest()

# Verify signature
verification = hashlib.sha256(private_key + message).digest()

print("Public Key:", public_key.hex())
print("Signature:", signature.hex())
print("Signature Valid:", signature == verification)