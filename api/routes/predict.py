# api/routes/predict.py
from fastapi import APIRouter, HTTPException
from api.schemas.predict import PredictRequest, PredictResponse
from api.services.inference import predict

router = APIRouter(prefix="/predict", tags=["Prediction"])

@router.post("", response_model=PredictResponse)
async def predict_endpoint(request: PredictRequest):
    try:
        result = predict(request.features)

    except ValueError as e:
        # Error Validating the input
        raise HTTPException(status_code=422, detail=str(e))

    return PredictResponse(prediction=result)
