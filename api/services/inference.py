# api/services/inference.py
from api.models.model_loader import load_model
import numpy as np

def predict(features: list[float]) -> float:
    model = load_model()
    X = np.array(features).reshape(1, -1)

    prediction = model.predict(X)
    
    return int(prediction[0])
