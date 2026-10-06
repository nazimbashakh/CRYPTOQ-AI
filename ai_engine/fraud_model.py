from xgboost import XGBClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score,
    precision_score,
    recall_score
)
import joblib


class FraudDetectionModel:

    def __init__(self):

        self.model = XGBClassifier(
            n_estimators=400,
            max_depth=6,
            learning_rate=0.05,
            subsample=0.8,
            colsample_bytree=0.8,
            scale_pos_weight=70,
            random_state=42,
            eval_metric="logloss"
        )

    def train(self, X_train, y_train):
        print("Training XGBoost model...")
        self.model.fit(X_train, y_train)
        print("Training completed.")

    def evaluate(self, X_test, y_test):
        print("\nEvaluating model...")

        y_prob = self.model.predict_proba(X_test)[:, 1]

        # Default threshold
        threshold = 0.5
        y_pred = (y_prob >= threshold).astype(int)

        print("\nClassification Report (Threshold 0.5):")
        print(classification_report(y_test, y_pred))

        print("\nConfusion Matrix:")
        print(confusion_matrix(y_test, y_pred))

        roc_auc = roc_auc_score(y_test, y_prob)
        print("\nROC-AUC Score:", roc_auc)

        print("\n--- Threshold Comparison ---")
        thresholds_to_test = [0.3, 0.4, 0.5, 0.6, 0.7]

        for t in thresholds_to_test:
            y_pred_t = (y_prob >= t).astype(int)
            p = precision_score(y_test, y_pred_t)
            r = recall_score(y_test, y_pred_t)
            print(f"Threshold {t:.2f} | Precision: {p:.3f} | Recall: {r:.3f}")

        return roc_auc

    def save_model(self, filepath="fraud_model.pkl"):
        joblib.dump(self.model, filepath)
        print(f"\nModel saved to {filepath}")