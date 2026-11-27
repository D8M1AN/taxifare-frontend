import streamlit as st
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'Hello World!'}

@app.get('/predict')
def predict(
    pickup_datetime : str,
    pickup_longitude : float,
    pickup_latitude: float,
    dropoff_longitude: float,
    dropoff_latitud: float,
    passenger_count: int):
    return {'fare': 15.0}
