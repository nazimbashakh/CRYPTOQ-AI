import sys
import os
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Add project paths
sys.path.append(os.path.abspath("../core"))
sys.path.append(os.path.abspath("../ai_engine"))

from secure_pipeline import SecureTransactionPipeline

app = FastAPI(title="CRYPTOQ-AI API")

pipeline = SecureTransactionPipeline()


class TransactionRequest(BaseModel):
    step: int
    type: str
    amount: float
    nameOrig: str
    oldbalanceOrg: float
    newbalanceOrig: float
    nameDest: str
    oldbalanceDest: float
    newbalanceDest: float
    isFlaggedFraud: int


@app.post("/transaction")
def process_transaction(request: TransactionRequest):

    transaction_row = request.dict()

    result = {}

    try:
        # Convert to DataFrame for risk engine
        input_df = pd.DataFrame([transaction_row])

        fraud_prob, decision, reasons = pipeline.risk_engine.predict_risk(input_df)

        result["fraud_probability"] = float(fraud_prob)
        result["decision"] = decision
        result["risk_factors"] = reasons

        if decision == "BLOCK":
            result["secure_status"] = "FAILED"
        else:
            result["secure_status"] = "SECURE"

        return result

    except Exception as e:
        return {"error": str(e)}