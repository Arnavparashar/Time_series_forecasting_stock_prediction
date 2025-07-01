import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- Load Data ---
forecast = pd.read_csv("lstm_forecast.csv")
forecast['Date'] = pd.to_datetime(forecast['Date'])

historical = pd.read_csv("aapl_enhanced_features.csv")
historical['Date'] = pd.to_datetime(historical['Date'])

# --- Sidebar Controls ---
st.sidebar.header("Forecast Settings")
model_option = st.sidebar.selectbox("Model", ["LSTM "], index=0)
period_option = st.sidebar.selectbox("Forecast Length", ["Next 7 Days", "Next 15 Days", "Next 30 Days"], index=2)

# Map user choice to days
days_map = {"Next 7 Days": 7, "Next 15 Days": 15, "Next 30 Days": 30}
forecast_days = days_map[period_option]
forecast_subset = forecast.iloc[:forecast_days]

# --- Title & Description ---
st.title("Apple Stock Forecast")
st.markdown("Powered by an **LSTM model** trained on 8 years of AAPL data to forecast the next 30 days.")

# --- Plot: Historical + Forecast ---
fig = go.Figure()

# Historical
fig.add_trace(go.Scatter(x=historical['Date'], y=historical['Close'],
                         mode='lines', name='Historical',
                         line=dict(color='gray')))

# Forecast
fig.add_trace(go.Scatter(x=forecast_subset['Date'], y=forecast_subset['Predicted Close'],
                         mode='lines+markers', name='Forecast',
                         line=dict(color='deepskyblue', width=3)))

fig.update_layout(
    title="AAPL Forecasted Close Price",
    template="plotly_dark",
    xaxis_title="Date",
    yaxis_title="Price (USD)",
    hovermode="x unified",
    height=500
)
st.plotly_chart(fig, use_container_width=True)

# --- Metric Summary ---
change_pct = ((forecast_subset['Predicted Close'].iloc[-1] - forecast_subset['Predicted Close'].iloc[0]) / forecast_subset['Predicted Close'].iloc[0]) * 100
change_color = "green" if change_pct >= 0 else "red"
st.metric(label=f"{period_option} Forecast Change", value=f"{change_pct:.2f}%", delta=f"{change_pct:.2f}%", delta_color="normal")
