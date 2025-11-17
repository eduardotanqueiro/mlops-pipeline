# app/schemas/predict.py
from pydantic import BaseModel, Field

class PredictRequest(BaseModel):
    features: list[float] = Field(..., example=[2, 39.5, 16.7, 178.0, 3250.0, 1], alias="input_features (island,culmen_length_mm,culmen_depth_mm,flipper_length_mm,body_mass_g,sex)")

class PredictResponse(BaseModel):
    prediction: int