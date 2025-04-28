import pandas as pd
import requests
import numpy as np
import os
from datetime import datetime

# ---- Configuration ----
API_KEY = "78e60a36daade4dff66f6f2b750dae5a3c830888"  # Replace with your API key
CITY = "london"
DATA_FILE = "../outputFiles/air_quality.csv"


# ---- Fetch Real-Time Data (WAQI API) ----
def fetch_waqi_data():
    url = f"https://api.waqi.info/feed/{CITY}/?token={API_KEY}"
    response = requests.get(url).json()

    if response["status"] == "ok":
        iaqi = response["data"]["iaqi"]
        # Safely extract data with default NaN for missing values
        pm25 = iaqi.get("pm25", {}).get("v", np.nan)
        temp = iaqi.get("t", {}).get("v", np.nan)
        humidity = iaqi.get("h", {}).get("v", np.nan)
        timestamp = response["data"]["time"]["s"]

        return {
            "timestamp": timestamp,
            "temperature": temp,
            "humidity": humidity,
            "pm25": pm25
        }
    else:
        print(f"Error: {response.get('data', 'Unknown error')}")
        return None


# ---- Save Data to CSV ----
def save_data(data):
    df = pd.DataFrame([data])
    # Write headers only if the file is new
    if not os.path.exists(DATA_FILE):
        df.to_csv(DATA_FILE, index=False)
    else:
        df.to_csv(DATA_FILE, mode="a", header=False, index=False)
    print(f"Data saved: {data}")


# ---- Main Execution ----
if __name__ == "__main__":
    data = fetch_waqi_data()
    if data:
        save_data(data)