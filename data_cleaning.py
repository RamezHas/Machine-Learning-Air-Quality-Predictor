import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


# ---- Load Data ----
def clean_data():
    try:
        df = pd.read_csv("test_air_quality.csv")
    except FileNotFoundError:
        raise FileNotFoundError("CSV file not found. Run data_collection.py first.")

    # ---- Validate Columns ----
    required_columns = ["timestamp", "temperature", "humidity", "pm25"]
    if not all(col in df.columns for col in required_columns):
        raise ValueError("CSV file is missing required columns. Check data_collection.py.")

    # ---- Handle Missing Values ----
    # Drop rows where PM2.5 (pm25) is missing
    df = df.dropna(subset=["pm25"])
    # Fill missing temperature/humidity with column means
    df["temperature"] = df["temperature"].fillna(df["temperature"].mean())
    df["humidity"] = df["humidity"].fillna(df["humidity"].mean())

    # ---- Normalize Data ----
    scaler = MinMaxScaler()
    df[["temperature", "humidity"]] = scaler.fit_transform(df[["temperature", "humidity"]])

    # ---- Save Cleaned Data ----
    df.to_csv("cleaned_air_quality.csv", index=False)
    print("Cleaned data saved to cleaned_air_quality.csv")
    return df


if __name__ == "__main__":
    clean_data()