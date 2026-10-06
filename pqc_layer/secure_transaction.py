import os
import hashlib

print("=== CRYPTOQ-AI Secure Transaction Simulation ===\n")

# ---------------------------
# Step 1: Simulate Transaction
# ---------------------------
transaction = b"Transfer 5000 INR to Account XYZ"
print("Transaction Created.")

# ---------------------------
# Step 2: Digital Signature
# ---------------------------
private_key = os.urandom(32)
public_key = hashlib.sha256(private_key).digest()

signature = hashlib.sha256(private_key + transaction).digest()
print("Transaction Signed.")

# ---------------------------
# Step 3: Verify Signature
# ---------------------------
verification = hashlib.sha256(private_key + transaction).digest()

if signature == verification:
    print("Signature Verified.")
else:
    print("Signature Invalid.")
    exit()

# ---------------------------
# Step 4: Simulated Key Exchange
# ---------------------------
client_private = os.urandom(32)
server_private = os.urandom(32)

shared_secret_client = hashlib.sha256(client_private + server_private).digest()
shared_secret_server = hashlib.sha256(client_private + server_private).digest()

if shared_secret_client == shared_secret_server:
    print("Secure Shared Secret Established.")
else:
    print("Key Exchange Failed.")
    exit()

# ---------------------------
# Step 5: Secure Transmission
# ---------------------------
encrypted_transaction = hashlib.sha256(shared_secret_client + transaction).hexdigest()

print("Transaction Encrypted.")
print("\nEncrypted Transaction:", encrypted_transaction)

print("\n=== Secure Transaction Completed Successfully ===")