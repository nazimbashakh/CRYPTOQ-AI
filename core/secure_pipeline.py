import uuid
import hashlib
import pandas as pd
import sys
import os

# Add ai_engine path
sys.path.append(os.path.abspath("../ai_engine"))

from risk_engine import RiskEngine


class SecureTransactionPipeline:

    def __init__(self):
        self.risk_engine = RiskEngine()

    def process_transaction(self, transaction_data: dict):

        print("\n=== CRYPTOQ-AI Hybrid Secure Transaction ===")

        # Convert to DataFrame for AI engine
        input_df = pd.DataFrame([transaction_data])

        # AI Fraud Detection
        fraud_prob, decision, reasons = self.risk_engine.predict_risk(input_df)

        print("Fraud Probability:", fraud_prob)
        print("AI Decision:", decision)
        print("Top Risk Factors:", reasons)

        if decision == "BLOCK":
            print("Transaction Blocked Due To High Risk.")
            return fraud_prob, decision, reasons

        # If approved → simulate quantum secure transaction

        transaction_id = str(uuid.uuid4())

        encrypted_reference = hashlib.sha256(
            str(transaction_data).encode()
        ).hexdigest()

        print("Transaction ID:", transaction_id)
        print("Encrypted Reference:", encrypted_reference[:32], "...")

        print("Transaction Status: SECURE")

        print("\n=== Hybrid Secure Transaction Completed ===")

        return fraud_prob, decision, reasons