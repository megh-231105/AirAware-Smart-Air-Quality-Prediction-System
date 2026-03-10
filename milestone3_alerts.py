# ==========================================
# AIRAWARE SMART - MILESTONE 3
# AQI Category & Alert System
# ==========================================

import pandas as pd

# 1. SAMPLE PREDICTED AQI DATA

data = {
    "Date":[
        "2024-01-11",
        "2024-01-12",
        "2024-01-13",
        "2024-01-14",
        "2024-01-15"
    ],

    "Predicted_AQI":[85,120,175,220,45]
}

df = pd.DataFrame(data)

print("Predicted AQI")
print(df)

# 2. AQI CATEGORY FUNCTION

def get_category(aqi):

    if aqi <= 50:
        return "Good"

    elif aqi <= 100:
        return "Moderate"

    elif aqi <= 200:
        return "Unhealthy"

    elif aqi <= 300:
        return "Very Unhealthy"

    else:
        return "Hazardous"


# 3. APPLY CATEGORY

df["Category"] = df["Predicted_AQI"].apply(get_category)

print("\nAQI Categories")
print(df)

# 4. ALERT SYSTEM

def generate_alert(aqi):

    if aqi > 200:
        return "HIGH ALERT - Avoid outdoor activities"

    elif aqi > 150:
        return "Warning - Wear mask outside"

    else:
        return "Air quality safe"


df["Alert"] = df["Predicted_AQI"].apply(generate_alert)

print("\nAlert Report")
print(df)