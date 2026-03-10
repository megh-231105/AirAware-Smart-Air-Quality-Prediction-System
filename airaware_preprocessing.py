# ==========================================
# AIRAWARE SMART - MILESTONE 1 DEMO CODE
# Data Preprocessing & Basic Analysis
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# 1. CREATE SAMPLE DATA

data = {
    "Date": ["2024-01-01", "2024-01-02", "2024-01-03",
             "2024-01-04", "2024-01-05", "2024-01-06"],
    "PM25": [120, 150, None, 80, 70, 65],
    "PM10": [200, 240, 220, None, 150, 140],
    "NO2": [40, 55, 50, 45, None, 30]
}

df = pd.DataFrame(data)

print("ORIGINAL DATA")
print(df)

# 2. DATA PREPROCESSING

df["Date"] = pd.to_datetime(df["Date"])

df["PM25"] = df["PM25"].fillna(df["PM25"].mean())
df["PM10"] = df["PM10"].fillna(df["PM10"].mean())
df["NO2"] = df["NO2"].fillna(df["NO2"].mean())

print("\nAFTER CLEANING")
print(df)

# 3. FEATURE ENGINEERING

df["Day"] = df["Date"].dt.day
df["Weekday"] = df["Date"].dt.day_name()

print("\nAFTER FEATURE ENGINEERING")
print(df)

# 4. STATISTICAL SUMMARY

print("\nSTATISTICAL SUMMARY")
print(df.describe())

# 5. VISUALIZATION

plt.title("PM2.5 Trend")
plt.plot(df["Date"], df["PM25"])
plt.xlabel("Date")
plt.ylabel("PM2.5")
plt.show()
