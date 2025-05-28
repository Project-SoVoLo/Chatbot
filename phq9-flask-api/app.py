from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import json
import os

# Flask 초기화
app = Flask(__name__)
CORS(app)

# 모델, 벡터라이저, 키워드, 임계값 로딩
MODEL_DIR = "model"
model = joblib.load(os.path.join(MODEL_DIR, "logistic_regression_model.pkl"))
vectorizer = joblib.load(os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl"))

with open(os.path.join(MODEL_DIR, "phq_keywords.json"), "r") as f:
    phq_keywords = json.load(f)

with open(os.path.join(MODEL_DIR, "optimal_thresholds.json"), "r") as f:
    optimal_thresholds = json.load(f)

labels = list(phq_keywords.keys())

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        text = data.get("text", "")

        tfidf = vectorizer.transform([text])
        probs = model.predict_proba(tfidf)[0]

        result = {}
        for label, prob in zip(labels, probs):
            prob = round(prob, 4)
            pred = prob >= optimal_thresholds.get(label, 0.5)
            result[label] = {
                "probability": prob,
                "predicted": int(pred)
            }

        return jsonify({
            "status": "success",
            "result": result
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(port=5050)