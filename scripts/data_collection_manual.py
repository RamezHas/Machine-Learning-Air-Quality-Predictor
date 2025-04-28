import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate synthetic data for 7 days (hourly)
np.random.seed(42)
timestamps = [datetime(2024, 1, 1) + timedelta(hours=i) for i in range(168)]  # 7 days * 24 hours
temperature = np.random.uniform(15, 30, 168)  # Random temps between 15°C and 30°C
humidity = np.random.uniform(30, 80, 168)     # Random humidity between 30% and 80%
pm25 = np.random.normal(35, 10, 168)          # PM2.5 around 35 µg/m³ (±10)

# Add some outliers and trends
pm25[10:15] = 80  # Simulate a pollution spike
pm25[100:110] = 10 # Simulate clean air

# Create DataFrame
test_data = pd.DataFrame({
    "timestamp": timestamps,
    "temperature": temperature,
    "humidity": humidity,
    "pm25": pm25
})

# Save to CSV
test_data.to_csv("test_air_quality.csv", index=False)
print("Test data generated: test_air_quality.csv")