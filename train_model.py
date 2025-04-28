import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import pickle

df = pd.read_csv("outputFiles/cleaned_air_quality.csv")
x = df[["temperature", "humidity"]]
y = df["pm25"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

print("Model Coefficients:")
print(f"Temperature: {model.coef_[0]}")
print(f"Humidity: {model.coef_[1]}")
print(f"Intercept: {model.intercept_}")

y_pred = model.predict(x_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\nModel Performance:")
print(f"Mean Absolute Error (MAE): {mae} µg/m³")
print(f"Root Mean Squared Error (RMSE): {rmse} µg/m³")

plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], "--r")
plt.xlabel("Actual PM2.5")
plt.ylabel("Predicted PM2.5")
plt.show()

with open("outputFiles/pm25_predictor.pkl", "wb") as f:
    pickle.dump(model, f)