from pathlib import Path

import pandas as pd
from fastapi import FastAPI

from taxifare.pipeline import load_model, predict

app = FastAPI()

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "linreg_pipeline.joblib"
model = load_model(MODEL_PATH)  # load once at startup


@app.get("/")
def root():
    return {"greeting": "Hello"}


@app.get("/predict")
def predict_endpoint(
    pickup_datetime: str,
    pickup_longitude: float,
    pickup_latitude: float,
    dropoff_longitude: float,
    dropoff_latitude: float,
    passenger_count: int,
):
    X_pred = pd.DataFrame(
        [[pd.Timestamp(pickup_datetime, tz="US/Eastern"),
          pickup_longitude, pickup_latitude,
          dropoff_longitude, dropoff_latitude, passenger_count]],
        columns=["pickup_datetime", "pickup_longitude", "pickup_latitude",
                 "dropoff_longitude", "dropoff_latitude", "passenger_count"],
    )
    fare = predict(model, X_pred)
    return {"fare": float(fare[0])}
