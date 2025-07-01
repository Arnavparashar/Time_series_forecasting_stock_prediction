# 📈 Time Series Forecasting - Apple Stock Prediction using LSTM

An interactive and visually rich Streamlit dashboard that forecasts **Apple's stock closing prices** using an LSTM model trained on 8 years of historical data. Users can explore short-term stock trends for the next 7, 15, or 30 days with clean, intuitive visualizations.

🔗 **Live Demo:[Launch the App ](https://timeseriesforecastingstockprediction-omxqm3us5rrkpy25lywjhk.streamlit.app/)

---

## 🧠 Tech Stack

| Layer         | Technology                         |
|---------------|-------------------------------------|
| 🖥️ Interface   | [Streamlit](https://streamlit.io/)   |
| 📊 Charts      | [Plotly](https://plotly.com/)       |
| 📁 Data        | Pandas, CSV (AAPL stock data)      |
| 🔮 Model       | Pre-trained LSTM (external to repo) |
| ☁️ Deployment  | Streamlit Cloud                    |

---

## Features

- 📅 Forecasts Apple stock price for:
  - Next 7 Days
  - Next 15 Days
  - Next 30 Days
- 📈 Line charts comparing historical vs predicted prices
- 🔍 Forecast trend metric with % change indicator
- 🌙 Dark-themed Plotly visualization
- ⚡ Simple, fast, and mobile-responsive UI

---

## Folder Structure
Time_series_forecasting_stock_prediction/
├── app.py # Streamlit app source code
├── lstm_forecast.csv # LSTM model forecast output (30 days)
├── aapl_enhanced_features.csv # Historical Apple stock data
├── requirements.txt # Project dependencies
└── README.md # Project overview and usage
