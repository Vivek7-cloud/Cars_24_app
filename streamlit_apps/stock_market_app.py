import streamlit as st
import yfinance as yf
import datetime

# App title
st.title("Stock Market App")

# User input for stock ticker
ticker_symbol = st.text_input("Enter Stock Ticker", "AAPL")

# Create two columns
col1, col2 = st.columns(2)

# Start date input
with col1:
    start_date = st.date_input(
        "Start Date",
        datetime.date(2019, 1, 1)
    )

# End date input
with col2:
    end_date = st.date_input(
        "End Date",
        datetime.date(2023, 12, 31)
    )

# Download stock data
data = yf.download(
    ticker_symbol,
    start=start_date,
    end=end_date
)

# Show dataframe
st.write(data)

# Plot closing price chart
if not data.empty:
    st.line_chart(data["Close"])
else:
    st.warning("No data found for the selected ticker/date range.")