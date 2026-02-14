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

