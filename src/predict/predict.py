# src/predict/predict.py
from joblib import load
import os
from src.features.extract_features import extract_features
import pandas as pd

MODEL_PATH = "models/rf_phish_model.joblib"

class Predictor:
    def __init__(self, model_path=MODEL_PATH):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model not found at {model_path}. Please train the model first.")
        self.model = load(model_path)

    def predict(self, url):
        feats = extract_features(url)
        # ensure same ordering as training
        df = pd.DataFrame([feats])
        # simple imputation if needed
        if 'domain_age_days' in df.columns:
            df['domain_age_days'] = df['domain_age_days'].replace(-1, df['domain_age_days'].median())
        prob = self.model.predict_proba(df)[0][1] if hasattr(self.model, "predict_proba") else None
        label = int(self.model.predict(df)[0])
        return {"label": label, "probability": float(prob) if prob is not None else None, "features": feats}

# quick CLI test
if __name__ == "__main__":
    p = Predictor()
    url = "http://example.com/login"
    print(p.predict(url))
