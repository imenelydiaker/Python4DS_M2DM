from code import clf
from code import vectorizer
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/prediction/{restaurant_name}")
def read_item(restaurant_name: str):
    prediction = clf.predict(vectorizer.transform([restaurant_name]))
    return {"restaurant_name": restaurant_name,"prediction": str(prediction)}