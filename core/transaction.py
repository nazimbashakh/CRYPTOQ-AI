import uuid
import time
import json


class Transaction:
    def __init__(self, sender: str, receiver: str, amount: float):
        self.transaction_id = str(uuid.uuid4())
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time.time()
        self.status = "CREATED"

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "timestamp": self.timestamp,
            "status": self.status
        }

    def to_bytes(self):
        return json.dumps(self.to_dict()).encode()

    def mark_secure(self):
        self.status = "SECURE"

    def mark_failed(self):
        self.status = "FAILED"