# ==========================================
# AIRAWARE SMART - MILESTONE 2
# AQI Forecasting using Prophet
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

# 1. CREATE SAMPLE AQI DATA

data = {
    "Date": [
        "2024-01-01","2024-01-02","2024-01-03","2024-01-04",
        "2024-01-05","2024-01-06","2024-01-07","2024-01-08",
        "2024-01-09","2024-01-10"
    ],
    "AQI": [120,130,128,140,150,160,155,165,170,175]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

# 2. PREPROCESSING

df["Date"] = pd.to_datetime(df["Date"])

df = df.rename(columns={
    "Date":"ds",
    "AQI":"y"
})

print("\nPrepared Data")
print(df)

# 3. TRAIN MODEL

model = Prophet()

model.fit(df)

# 4. CREATE FUTURE DATES

future = model.make_future_dataframe(periods=7)

print("\nFuture Dates")
print(future.tail())

# 5. PREDICTIONS

forecast = model.predict(future)

print("\nPredicted AQI")
print(forecast[["ds","yhat"]].tail(7))

# 6. FORECAST GRAPH

model.plot(forecast)
plt.title("AQI Prediction")
plt.show()

# 7. TREND COMPONENTS

model.plot_components(forecast)
plt.show()