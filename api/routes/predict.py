# api/routes/predict.py
from fastapi import APIRouter
from api.schemas.predict import PredictRequest, PredictResponse
from api.services.inference import predict

router = APIRouter(prefix="/predict", tags=["Prediction"])

@router.post("", response_model=PredictResponse)
async def predict_endpoint(request: PredictRequest):
    result = predict(request.features)

    return PredictResponse(prediction=result)
