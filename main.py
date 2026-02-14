from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello Keerthana"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/square")
def square(x: int):
    return {"result": x**2}

from pydantic import BaseModel

class InputData(BaseModel):
    feature: float

@app.post("/predict")
def predict(data: InputData):
    # Dummy prediction logic
    prediction = (data.feature * 2) + 1 # Replace with actual model prediction
    return {"prediction": prediction}

