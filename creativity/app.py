

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import json
import numpy as np
from .topics import get_metrics
from .load_model import get_models
import os.path

class Source(BaseModel):
    text: str
    dataset: str = "climate_change"

class Answer(BaseModel):
    fluency: float
    flexibility: float
    originality: float
    topics: List[int]


app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)

@app.get("/")
def wake_up():
    thankyou=1
    return thankyou

@app.get("/models")
def load_models():
    response = "Error"
    # check if file exists
    if os.path.isfile('./models/climate_change_model'):
        response = "Files exists"
    else:
        get_models()
        response = "Downloaded files"
    return response


@app.get("/get-creativity/{text}")
def complete_test(text):
    
    print(text)

    fluency, flexibility, originality, topics  = get_metrics(text, dataset = "climate_change")
    print(fluency, flexibility, originality)

    answer = Answer(fluency=fluency, 
                    flexibility= flexibility, 
                    originality=originality,
                    topics = list(topics)
    )
    return answer


@app.post("/creativity/")
def complete_test(source: Source):
    text = source.text
    print(text)

    fluency, flexibility, originality  = get_metrics(text, dataset = source.dataset)
    print(fluency, flexibility, originality)

    answer = Answer(fluency=fluency, 
    flexibility= flexibility, originality=originality)
    return answer

