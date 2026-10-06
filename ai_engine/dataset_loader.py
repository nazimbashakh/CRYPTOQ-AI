import pandas as pd
from sklearn.model_selection import train_test_split


class DatasetLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None

    def load_data(self, sample_size=200000):
        print("Loading dataset...")
        self.df = pd.read_csv(self.filepath)

        print("Original Shape:", self.df.shape)

        # Sample data for performance
        if sample_size and sample_size < len(self.df):
            self.df = self.df.sample(sample_size, random_state=42)

        print("Sampled Shape:", self.df.shape)
        return self.df

    def preprocess(self):
        print("Preprocessing dataset...")

        # Encode transaction type (categorical)
        self.df = pd.get_dummies(self.df, columns=["type"], drop_first=True)

        # Drop non-useful columns
        self.df = self.df.drop(["nameOrig", "nameDest", "isFlaggedFraud"], axis=1)

        X = self.df.drop("isFraud", axis=1)
        y = self.df["isFraud"]

        return train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )