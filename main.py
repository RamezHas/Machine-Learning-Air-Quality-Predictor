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

if response["status"] == "ok":
    pm25 = response["data"]["iaqi"]["pm25"]["v"]
    timestamp = response["data"]["time"]["s"]
else:
    print("Error fetching data:", response.get("data", "Unknown error"))

air_quality_df = pd.DataFrame({
    "timestamp": [timestamp],
    "PM2.5": [pm25]
})
print(air_quality_df)