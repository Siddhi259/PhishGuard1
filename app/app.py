# app/app.py
from flask import Flask, render_template, request, jsonify
import os
import sys
# allow import src package
proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(proj_root)

from src.predict.predict import Predictor

app = Flask(__name__, template_folder="templates", static_folder="static")
PRED = None

@app.before_first_request
def load_model():
    global PRED
    try:
        PRED = Predictor(model_path=os.path.join(proj_root, "models", "rf_phish_model.joblib"))
    except Exception as e:
        PRED = None
        app.logger.error(f"Failed to load model: {e}")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", result=None, error=None)

@app.route("/predict", methods=["POST"])
def predict():
    if PRED is None:
        return render_template("index.html", error="Model not loaded. Train the model first and place it in /models.", result=None)
    url = request.form.get("url", "").strip()
    if not url:
        return render_template("index.html", error="Please enter a URL.", result=None)
    # normalize basic
    if not url.startswith("http"):
        url = "http://" + url
    try:
        res = PRED.predict(url)
        label = "Phishing" if res["label"] == 1 else "Legitimate"
        prob = res.get("probability", None)
        return render_template("index.html", result={"label": label, "probability": prob, "features": res["features"]}, error=None)
    except Exception as e:
        return render_template("index.html", error=f"Prediction failed: {e}", result=None)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
