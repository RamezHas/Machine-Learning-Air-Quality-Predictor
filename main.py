import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle
import os
import requests

api_key = "78e60a36daade4dff66f6f2b750dae5a3c830888"
city = "Hagen"

url = f"https://api.waqi.info/feed/{city}/?token={api_key}"
response = requests.get(url).json()
print(response)
if response["status"] == "ok":
    pm25 = response["data"]["iaqi"].get("pm25", {}).get("v", np.nan)
    timestamp = response["data"]["time"]["s"]
    temp = response["data"]["iaqi"].get("t", {}).get("v", np.nan)
    humidity = response["data"]["iaqi"].get("h", {}).get("v", np.nan)
else:
    print("Error fetching data:", response.get("data", "Unknown error"))


air_quality_df = pd.DataFrame({
    "timestamp": [timestamp],
    "PM2.5": [pm25],
    "Temperature": [temp],
    "Humidity": [humidity],
    "Status": "OK"
})
air_quality_df.to_csv("hagen_air_quality.csv", mode="a", header=False, index=False)
print(air_quality_df)