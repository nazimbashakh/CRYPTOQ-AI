from dataset_loader import DatasetLoader
from fraud_model import FraudDetectionModel
import joblib


def main():

    # ---------------------------
    # Load and preprocess dataset
    # ---------------------------
    loader = DatasetLoader("paysim.csv")

    df = loader.load_data(sample_size=200000)

    X_train, X_test, y_train, y_test = loader.preprocess()

    # ---------------------------
    # Save Feature Columns
    # ---------------------------
    joblib.dump(X_train.columns.tolist(), "feature_columns.pkl")

    # ---------------------------
    # Train Fraud Model
    # ---------------------------
    model = FraudDetectionModel()
    model.train(X_train, y_train)

    # ---------------------------
    # Evaluate Model
    # ---------------------------
    roc_auc = model.evaluate(X_test, y_test)

    # ---------------------------
    # Save Model
    # ---------------------------
    model.save_model("fraud_model.pkl")

    print("\n=== Training Pipeline Completed ===")


if __name__ == "__main__":
    main()