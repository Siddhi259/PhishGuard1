# src/models/train.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix
from joblib import dump
import os
from src.features.extract_features import extract_features

DATA_PATH = "data/processed/dataset.csv"  # expected input CSV
MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

def prepare_features(df, url_col='url'):
    rows = []
    for url in df[url_col].astype(str).tolist():
        feats = extract_features(url)
        rows.append(feats)
    feat_df = pd.DataFrame(rows)
    return feat_df

def main():
    # Expect dataset CSV with columns: url,label  (label: 1=phishing,0=legit)
    print("Loading dataset:", DATA_PATH)
    df = pd.read_csv(DATA_PATH)
    if 'label' not in df.columns or 'url' not in df.columns:
        raise ValueError("CSV must have 'url' and 'label' columns")

    X = prepare_features(df, url_col='url')
    y = df['label'].astype(int)

    # simple imputation for domain_age
    X['domain_age_days'] = X['domain_age_days'].replace(-1, X['domain_age_days'].median())

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    print("Training RandomForest...")
    rf = RandomForestClassifier(n_estimators=200, max_depth=20, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)

    y_pred = rf.predict(X_test)
    print("Classification report:\n", classification_report(y_test, y_pred))
    print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))

    model_path = os.path.join(MODEL_DIR, "rf_phish_model.joblib")
    dump(rf, model_path)
    print("Saved model to:", model_path)

if __name__ == "__main__":
    main()
