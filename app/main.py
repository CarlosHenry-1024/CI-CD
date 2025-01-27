from fastapi import FastAPI
from pydantic import BaseModel
from .preprocess import clean_text
from .model import predict
from .metrics import calculate_accuracy

app = FastAPI()

# 请求体模
class TextInput(BaseModel):
    text: str

@app.post("/predict")
async def predict_sentiment(input: TextInput):
    cleaned_text = clean_text(input.text)
    prediction = predict(cleaned_text)
    return {"text": input.text, "prediction": prediction}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}