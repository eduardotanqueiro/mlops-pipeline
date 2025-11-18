from fastapi import FastAPI
from .predict import router as predict_router
from .root import router as root_router

def register_routes(app: FastAPI):
    app.include_router(root_router)
    app.include_router(predict_router, prefix="/predict")
