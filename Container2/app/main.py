from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import re
from sklearn.feature_extraction.text import CountVectorizer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class InputText(BaseModel):
    text: str

# Load your pre-trained models and necessary preprocessing objects here
path_cv = r'..\model\cv_feature.pkl'
path_model = r'..\model\cls_text_0.1.pkl'

cv = pickle.load(open(path_cv, 'rb'))
clf = pickle.load(open(path_model, 'rb'))

def preprocess_text(text):
    processed_text = re.sub(r'[!@#$%^&*(),:;0-9,\\n]', ' ', text)
    processed_text = re.sub(r'[[]]]', ' ', processed_text)
    processed_text = processed_text.lower()
    return processed_text

text_mapping = {0: "ham", 1: "spam"} 

def predict_text(model, cv, text):
    text_1 = re.sub(r'[!@#$%^&*(),:;0-9,\n]', ' ', text)
    text_2 = text_1.lower()
    x = cv.transform([text_2])
    lang = model.predict(x)
    return text_mapping[lang[0]]

# # CORS configuration to allow all origins, methods, and headers
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.post("/predict/")
def predict_spam(input_text: InputText):
    processed_text = preprocess_text(input_text.text)
    lang = predict_text(clf, cv, processed_text)
    # print("Input Text:", input_text.text)
    # print("Processed Text:", processed_text)
    # print("Predicted Label:", lang)
    return {"prediction": lang}
