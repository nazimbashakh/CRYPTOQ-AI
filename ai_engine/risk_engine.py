import joblib
import pandas as pd
import numpy as np
import os


class RiskEngine:
    def __init__(self,
                 threshold=0.40):

        # Get current directory of this file
        base_path = os.path.dirname(os.path.abspath(__file__))

        model_path = os.path.join(base_path, "fraud_model.pkl")
        feature_path = os.path.join(base_path, "feature_columns.pkl")

        self.model = joblib.load(model_path)
        self.feature_columns = joblib.load(feature_path)
        self.threshold = threshold

    def predict_risk(self, input_dataframe: pd.DataFrame):

        input_dataframe = pd.get_dummies(
            input_dataframe,
            columns=["type"],
            drop_first=True
        )

        input_dataframe = input_dataframe.drop(
            ["nameOrig", "nameDest", "isFlaggedFraud"],
            axis=1,
            errors="ignore"
        )

        input_dataframe = input_dataframe.reindex(
            columns=self.feature_columns,
            fill_value=0
        )

        fraud_probability = self.model.predict_proba(input_dataframe)[0][1]

        if fraud_probability >= self.threshold:
            decision = "BLOCK"
        elif fraud_probability >= 0.20:
            decision = "FLAG"
        else:
            decision = "APPROVE"

        feature_importances = self.model.feature_importances_
        feature_values = input_dataframe.iloc[0].values

        contribution_scores = feature_importances * feature_values
        top_indices = np.argsort(contribution_scores)[::-1][:3]

        explanations = []
        for idx in top_indices:
            if contribution_scores[idx] > 0:
                explanations.append(self.feature_columns[idx])

        return fraud_probability, decision, explanations