# api/main.py
from fastapi import FastAPI
from api.routes import predict, root
from api.models.model_loader import load_model

def create_app() -> FastAPI:

    app = FastAPI(
        title="ML Inference API",
        version="1.0.0"
    )

    # Routers
    app.include_router(root.router)
    app.include_router(predict.router)

    @app.on_event("startup")
    async def startup_event():
        load_model()  # ensure early load

    return app


app = create_app()
