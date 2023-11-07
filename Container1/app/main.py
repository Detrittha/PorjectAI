from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS configuration to allow all origins, methods, and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputText(BaseModel):
    text: str

def preprocess_text(text):
    return text.lower()

def get_prediction_from_container2(text):
    container2_url = 'http://127.0.0.1:5000/predict/'
    data = {"text": text}
    response = requests.post(container2_url, json=data)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error from Container 2")
    return response.json()["prediction"]

@app.post("/api/process/")
def process_text(input_text: InputText):
    processed_text = preprocess_text(input_text.text)
    prediction_from_container2 = get_prediction_from_container2(processed_text)
    return {"prediction_from_container1": prediction_from_container2}
