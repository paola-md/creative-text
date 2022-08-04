

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import json
import numpy as np
from .topics import get_metrics


class Source(BaseModel):
    text: str
    dataset: str = "climate_change"

class Answer(BaseModel):
    fluency: float
    flexibility: float
    originality: float


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

@app.post("/creativity/")
def complete_test(source: Source):
    text = source.text
    print(text)

    fluency, flexibility, originality  = get_metrics(text, dataset = source.dataset)
    print(fluency, flexibility, originality)

    answer = Answer(fluency, flexibility, originality)
    return answer

@app.get("/get-creativity/{text}")
def complete_test(text):
    
    print(text)

    fluency, flexibility, originality  = get_metrics(text, dataset = "climate_change")
    print(fluency, flexibility, originality)

    answer = Answer(fluency, flexibility, originality)
    return answer