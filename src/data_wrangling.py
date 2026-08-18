"""Basic preparation helpers used by the capstone."""
import pandas as pd

def create_binary_class(outcome):
    text = str(outcome).lower()
    return int("true" in text or "success" in text)

def prepare_features(df, categorical=None, numeric=None):
    categorical = categorical or []
    numeric = numeric or []
    x = df[categorical + numeric].copy()
    return pd.get_dummies(x, columns=categorical, dtype=float)
