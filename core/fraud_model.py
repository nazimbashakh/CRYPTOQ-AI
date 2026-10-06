from xgboost import XGBClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score
)
import joblib


class FraudDetectionModel:
    def __init__(self):

        # XGBoost tuned for imbalanced fraud detection
        self.model = XGBClassifier(
            n_estimators=300,
            max_depth=6,
            learning_rate=0.05,
            subsample=0.8,
            colsample_bytree=0.8,
            scale_pos_weight=50,  # important for imbalance
            random_state=42,
            eval_metric="logloss",
            use_label_encoder=False
        )

    def train(self, X_train, y_train):
        print("Training XGBoost model...")
        self.model.fit(X_train, y_train)
        print("Training completed.")

    def evaluate(self, X_test, y_test):
        print("\nEvaluating model...")

        y_pred = self.model.predict(X_test)
        y_prob = self.model.predict_proba(X_test)[:, 1]

        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))

        print("\nConfusion Matrix:")
        print(confusion_matrix(y_test, y_pred))

        roc_auc = roc_auc_score(y_test, y_prob)
        print("\nROC-AUC Score:", roc_auc)

        return roc_auc

    def save_model(self, filepath="fraud_model.pkl"):
        joblib.dump(self.model, filepath)
        print(f"\nModel saved to {filepath}")