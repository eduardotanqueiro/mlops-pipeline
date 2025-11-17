# api/models/model_loader.py
import joblib
from functools import lru_cache
from api.core.config import settings

# Cache the loaded model to avoid reloading on every request
@lru_cache
def load_model():
    model = joblib.load(settings.MODEL_PATH)
    return model