import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

st.title("AirAware Smart Dashboard")
st.write("Air Quality Prediction System")

data = {
"Date": [
"2024-01-01","2024-01-02","2024-01-03","2024-01-04",
"2024-01-05","2024-01-06","2024-01-07","2024-01-08",
"2024-01-09","2024-01-10"
],
"AQI": [120,130,128,140,150,160,155,165,170,175]
}

df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"])

df = df.rename(columns={"Date":"ds","AQI":"y"})

model = Prophet()
model.fit(df)

future = model.make_future_dataframe(periods=5)

forecast = model.predict(future)

st.subheader("AQI Forecast")

fig1 = model.plot(forecast)
st.pyplot(fig1)

latest_prediction = forecast["yhat"].iloc[-1]

st.subheader("Predicted AQI (Next Day)")
st.write(round(latest_prediction))

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

category = get_category(latest_prediction)

st.subheader("AQI Category")
st.write(category)

if latest_prediction > 200:
    st.error("HIGH ALERT! Avoid outdoor activities")
elif latest_prediction > 150:
    st.warning("Warning! Wear a mask outside")
else:
    st.success("Air quality is safe")

st.subheader("Historical AQI Data")
st.write(df)