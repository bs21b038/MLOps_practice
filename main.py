from fastapi import FastAPI
from pydantic import BaseModel
from config import config

# Load configuration
api_config = config.get_api_config()

# Initialize FastAPI app with config values
app = FastAPI(
    title=api_config.get("title", "FastAPI Application"),
    version=api_config.get("version", "1.0.0"),
    description=api_config.get("description", "A FastAPI application")
)

@app.get("/")
def home():
    return {"message": "Hello Keerthana"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/square")
def square(x: int):
    return {"result": x**2}

class InputData(BaseModel):
    feature: float

@app.post("/predict")
def predict(data: InputData):
    # Dummy prediction logic
    prediction = (data.feature * 2) + 1  # Replace with actual model prediction
    return {"prediction": prediction}

