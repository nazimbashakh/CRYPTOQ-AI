from risk_engine import RiskEngine
import pandas as pd

# Load one sample row
df = pd.read_csv("paysim.csv", nrows=1)

engine = RiskEngine()

prob, decision = engine.predict_risk(df)

print("Fraud Probability:", prob)
print("Decision:", decision)